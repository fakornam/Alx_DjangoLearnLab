from django.contrib import admin
from .models import Author, Book
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, UserAdmin
from .import admin_site, CustomUserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display =["username", "email", "date_of_birth", "profile_photo", "is_admin"]

    admin_site.register(CustomUser, CustomUserAdmin)


"admin.site.register(CustomUser, CustomUserAdmin)"


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title","publication_year","author"]
    search_fields = ["title"]
    list_filter = ["publication_year"]