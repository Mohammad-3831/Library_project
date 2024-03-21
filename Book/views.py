from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class BookListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        book = Book.objects.all()
        data = BookSerializer(book, many=True).data
        return Response(data)


class AddBookView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response({'message': 'Book Added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, slug=kwargs['slug'])
        data = BookSerializer(book).data
        return Response(data)


class CategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        data = CategorySerializer(category, many=True).data
        return Response(data)

class CategoryDetailView(APIView):
    def get(self, request, *args, **kwargs):
        category = Category.objects.filter(slug=kwargs['slug'])
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteCategoryView(APIView):
    def delete(self, request, *args, **kwargs):
        category = get_object_or_404(Category, slug=kwargs['slug'])
        category.delete()
        return Response({"result": "category deleted successfully!"}, status=status.HTTP_200_OK)

class AddCategoryView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Category Added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCategoryView(APIView):
    def put(self, request, *args, **kwargs):
        category = get_object_or_404(Category, slug=kwargs['slug'])
        serializer = CategorySerializer(category, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddCommentView(APIView):

    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response({'message': 'Comment Added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateBookView(APIView):

    def put(self, request, *args, **kwargs):
        book = get_object_or_404(Book, slug=kwargs['slug'])
        serializer = BookSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        book = get_object_or_404(Book, slug=kwargs['slug'])
        book.delete()
        return Response({"result": "book deleted successfully!"}, status=status.HTTP_200_OK)

class SearchBookView(APIView):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        book = Book.objects.filter(title__icontains=q)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetBookWithCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        category = request.GET.get('category')
        book = Book.objects.filter(category=category)
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)