from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
        widgets = {
            "tags": TagWidget(),
        }

    def validate_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: make tags more user-friendly
        self.fields["tags"].widget = forms.TextInput(
            attrs={"placeholder": "Add tags separated by commas"}
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def validate_content(self):
        content = self.cleaned_data.get("content")
        if not content or content.strip() == "":
            raise forms.ValidationError("Comment cannot be empty.")
        if len(content) < 3:
            raise forms.ValidationError("Comment must be at least 3 characters long.")
        return content