from django.db import models
from django.urls import reverse
from Users.models import User

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100,allow_unicode=True)

    def __str__(self):
        return self.name
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_author', null=True, blank=True)
    # for deploying must delete null and blank on user field
    category = models.ManyToManyField(Category,null=True,blank=True)
    title = models.CharField(max_length=100)
    short_description = models.TextField(null=True, blank=True)
    book_cover = models.ImageField(upload_to='media/books/book_cover', blank=True, null=True)
    book_file = models.FileField(upload_to='media/books/book_file', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorites = models.BooleanField(default=0,null=True,blank=True)
    slug = models.SlugField(allow_unicode=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:book_detail', args={'slug': self.slug})


class Comment(models.Model):
    STATUS_CHOICES = (
        ('1', 'waiting'),
        ('2', 'rejected'),
        ('3', 'confirmed'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.title
