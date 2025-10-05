# This is for the forms file for the user
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from django import forms
from .models import Post, Tag
from .models import BlogPost  
from taggit.forms import TagWidget 
from django.forms import widgets


class BlogPostForm(forms.ModelForm):
    tags = forms.CharField(
        widget=TagWidget(),  # Use TagWidget for tags
        required=False,      # Optional, you can make it required based on your need
    )
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'tags']  # Ensure 'tags' is included in fields

    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Add tags separated by commas'})
    )
    
    def clean_tags(self):
        tags_input = self.cleaned_data.get('tags')
        tags_list = [tag.strip() for tag in tags_input.split(',')] if tags_input else []
        return tags_list


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update({'placeholder': "Write your comment here..."})

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget_attrs.update({"class": "form-control"})
        self.fields["content"].widget_attrs.update({"class": "form-control"})
        


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
