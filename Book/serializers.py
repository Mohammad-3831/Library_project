from rest_framework import serializers
from rest_framework.serializers import *
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'

    def get_comments(self,obj):
        serializer = CommentSerializer(instance=obj.book_comments.all(), many=True)
        return serializer.data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
