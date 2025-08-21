from django.urls import path
from blog import views as for_views
from django.contrib.auth import views

urlpatterns = [
    path("register/", for_views.register, name="/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/register.html"),
    path("profile/", for_views.profile, name="/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/profile.html"),
    path("login/", views.LoginView.as_view(template_name="/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/registration/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),


]