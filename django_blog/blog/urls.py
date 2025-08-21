from django.urls import path
from blog import views as for_views
from django.contrib.auth import views
from .views import (
    BlogListView, BlogDetailView, BlogCreateView,
    BlogUpdateView, BlogDeleteView
)
from django.urls import path
from .views import BlogDetailView, CommentUpdateView, CommentDeleteView


    

urlpatterns = [
    path("register/", for_views.register, name="/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/register.html"),
    path("profile/", for_views.profile, name="/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/profile.html"),
    path("login/", views.LoginView.as_view(template_name="/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/registration/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),

    path("post/", BlogListView.as_view(), name="post-list"),
    path("post/new/", BlogCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", BlogUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post-delete"),

    path("post/<int:pk>/", BlogDetailView.as_view(), name="post-detail"),
    path("comment/<int:pk>/edit/", CommentUpdateView.as_view(), name="comment-edit"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),

]
