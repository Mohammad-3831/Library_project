from django.urls import path
from .views import *

app_name = 'book'

urlpatterns = [
    path('list',BookListView.as_view(),name='list'),
    path('add',AddBookView.as_view(),name='add'),
    path('add_comment',AddCommentView.as_view(),name='add_comment'),
    path('category',CategoryListView.as_view(),name='category'),
    path('category/add',AddCategoryView.as_view(),name='add_category'),
    path('category/update/<str:slug>',UpdateCategoryView.as_view(),name='update_category'),
    path('category/<str:slug>',CategoryDetailView.as_view(),name='category_detail'),
    path('category/delete/<str:slug>',DeleteCategoryView.as_view(),name='delete_category'),
    path('detail/<str:slug>',BookDetailView.as_view(),name='detail'),
    path('update/<str:slug>',UpdateBookView.as_view(),name='update_book'),
    path('delete/<str:slug>',DeleteBookView.as_view(),name='delete_book'),
    path('search/',SearchBookView.as_view(),name='search_book'),
    path('category_book/',GetBookWithCategoryView.as_view(),name='get_book_with_category'),
]