from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Tag

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    # This field handles the input as a string (comma-separated)
    tag_input = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter tags separated by commas'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content'] # We exclude 'tags' here to handle it manually

    # Override init to pre-fill tags when editing a post
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # Join the tag names with commas
            self.fields['tag_input'].initial = ', '.join(
                [t.name for t in self.instance.tags.all()]
            )

    # Override save to handle the tag logic
    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
            # 1. Clear existing tags
            post.tags.clear()
            
            # 2. Process the input string
            tag_names = self.cleaned_data['tag_input'].split(',')
            for name in tag_names:
                name = name.strip()
                if name:
                    # 3. Create tag if it doesn't exist, or get it if it does
                    tag, created = Tag.objects.get_or_create(name=name)
                    post.tags.add(tag)
        return post 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']