from django.urls import path
from blog import views as as_views
from django.contrib.auth import views

urlpatterns = [
    path("register/", as_views.register, name="register"),
    path("profile/", as_views.profile, name="profile"),
    path("login/", views.LoginView.as_view(template_name="blog/templates/blog/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),


]