from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    model = Book
    prepopulated_fields = {'slug': ('title',)}

class BookCategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Book, BookAdmin)
admin.site.register(Category, BookCategoryAdmin)
admin.site.register(Comment)
