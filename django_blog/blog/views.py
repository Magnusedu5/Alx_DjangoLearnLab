
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all().order_by("-created_at")  # all comments for this post
        context["form"] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        """Handle new comment submission"""
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect("post-detail", pk=self.object.pk)
        return self.get(request, *args, **kwargs)

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






from django.urls import reverse_lazy
from .models import Comment

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Comment
    fields = ["content"]
    template_name = "blog/comment_form.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only author can edit

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only author can delete

    def get_success_url(self):
        return reverse_lazy("post-detail", kwargs={"pk": self.object.post.pk})
