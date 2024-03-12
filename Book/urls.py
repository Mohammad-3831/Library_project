from django.urls import path
from .views import *

app_name = 'book'

urlpatterns = [
    path('list',BookListView.as_view(),name='list'),
    path('add',AddBookView.as_view(),name='add'),
    path('add_comment',AddCommentView.as_view(),name='add_comment'),
    path('category',CategoryListView.as_view(),name='category'),
    path('detail/<str:slug>',BookDetailView.as_view(),name='detail'),
]