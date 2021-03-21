from django.urls import path
from .views import main_page_view, search_result, book_page_view, book_page_update

urlpatterns = [
    path("", main_page_view, name='main_page_view'),
    path("search_result/", search_result, name='search_result'),
    path("book_page/<int:pk>", book_page_view, name='book_page_view'),
    path("book_page_update/<int:pk>", book_page_update, name='book_page_update')
]
