
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect("profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/profile.html")