
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("tags/<slug:tag_slug>/", views.PostByTagListView.as_view(), name="post_by_tag"),
    path("search/", views.search_posts, name="search_posts"),
    path("tags/<str:tag_name>/", views.view_tagged_posts, name="tagged_posts"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("post/<int:pk>/comments/new/", views.CommentCreateView.as_view(), name="comment_create"),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment_edit"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment_delete"),
    path("", PostListView.as_view(), name= "post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name= "post_detail"),
    path("post/new/", PostCreateView.as_view(), name= "post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name= "post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name= "post_delete"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
]
