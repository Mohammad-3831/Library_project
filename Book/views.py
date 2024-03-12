from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin

# def setup(self, request, *args, **kwargs):
#     super().setup(request, *args, **kwargs)
#     self.book = get_object_or_404(Book, slug=kwargs['slug'])
#     self.comments = Comment.objects.filter(status=3,book=self.book)
#     self.category = Category.objects.all()

class BookListView(APIView):

    def get(self,request,*args,**kwargs):
        book = Book.objects.all()
        data = BookSerializer(book,many=True).data
        return Response(data)

class AddBookView(APIView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('book:list')
        return super().dispatch(request, *args, **kwargs)
    def post(self,request,*args,**kwargs):
        serializer = BookSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response({'message':'Book Added'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    def get(self,request,*args,**kwargs):
        book = get_object_or_404(Book, slug=kwargs['slug'])
        data = BookSerializer(book).data
        return Response(data)



class CategoryListView(APIView):
    def get(self,request,*args,**kwargs):
        category = Category.objects.all()
        data = CategorySerializer(category,many=True).data
        return Response(data)

class AddCommentView(APIView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('book:category')
        return super().dispatch(request, *args, **kwargs)
    def post(self,request,*args,**kwargs):
        serializer = CommentSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response({'message':'Comment Added'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)