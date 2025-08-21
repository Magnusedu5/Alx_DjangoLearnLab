
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

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
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile has been updated ✔️")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, "/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/profile.html", context)


from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .forms import PostForm, CommentForm

class BlogListView(generic.ListView):
    model = Post
    fields = ["title", "content", "publication_date", "author"]
    template_name = "/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/post_list.html"
    permission_required = "blog.view_post"


class BlogDetailView(generic.DetailView):
    model = Post
    fields = ["title", "content", "publication_date", "author"]
    template_name = "/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/post_detail.html"

    
class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "content", "publication_date", "author"]
    template_name = "/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/post_form.html"
    permission_required = "blog.add_post"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user # set author automatically
        return super().form_valid(form)

class BlogUpdateView(UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Post
    fields = ["title", "content", "publication_date", "author"]
    template_name = "/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/post_form.html"
    permission_required = "blog.change_post"

class BlogDeleteView(UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Post
    fields = ["title", "content", "publication_date", "author"]
    template_name = "/home/magnus/Alx_DjangoLearnLab/django_blog/blog/templates/blog/post_confirm_delete.html"
    permission_required = "blog.delete_post"




from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Comment, Post
from .forms import CommentForm


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "comment_form.html"

    def form_valid(self, form):
        # attach logged-in user
        form.instance.author = self.request.user
        # get the related post
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.kwargs['pk']})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "comment_form.html"

    def get_queryset(self):
        # only allow author to edit their own comments
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "comment_confirm_delete.html"

    def get_queryset(self):
        # only allow author to delete their own comments
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.object.post.pk})
