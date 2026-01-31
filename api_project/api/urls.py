from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book-list')

urlpatterns = [
    # Manual path
    #path('books/', BookList.as_view(), name='book-list'),

    # The router-generated paths for CRUD
    path('', include(router.urls)),
]
