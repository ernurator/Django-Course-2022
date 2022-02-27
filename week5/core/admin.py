from django.contrib import admin
from .models import Author, Book, Publisher

# admin.site.register(Author)


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


@admin.register(Publisher)
class PublisherModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'city', 'country')


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'author', 'publisher')
    search_fields = ('title', 'author__first_name', 'author__last_name')
    ordering = ('id',)
