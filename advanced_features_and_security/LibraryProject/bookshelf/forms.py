from django import forms
from .models import Book

class ExampleForm(forms.Form):
    """
    A standard Django Form for general input.
    Using forms ensures that user inpur is validated before use.
    """
    example_field = forms.CharField(max_length=100, help_text="Enter some text safely.")

class BookForm(forms.ModelForm):
    """
    A ModelForm specifically for the Book Model.
    It automatically matches the fields in your Book model
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']