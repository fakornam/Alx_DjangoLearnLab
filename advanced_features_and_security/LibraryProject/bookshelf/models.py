from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager, UserManager
from LibraryProject import settings
from django.contrib.auth.admin import UserAdmin  # ✅ Correct
from .models import CustomUser
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions =[
            ("can_edit_news", "can edit news"),
            ("can_create_news", "can create news"),
            ("can_delete_news", "can delete news"),
            ("can_view_news", "can view news"),
        ]

    def __str__(self) -> str:
        return self.title


# Implement custom user manager by creating user model and superuser
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
    
        user = self.model(
            email = self.normalize_email(email),
            date_of_birth = date_of_birth,
            profile_photo = profile_photo,
        )

        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
# Implement superuser
    def create_superuser(self, email, date_of_birth, password=None, profile_photo=None ):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Create user model
# Extended AbstractUser class
class CustomUser(AbstractUser):
    class Meta:
        db_table = "auth_user"
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", date_of_birth, profile_photo]

    def __str__(self):
        return self.username

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="books")
    publication_year = models.IntegerField(default=2000)

    def __str__(self) -> str:
        return self.title
    