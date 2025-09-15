from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView



class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only the author of a post/comment can edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS → allow for anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise → only allow if the logged-in user is the author
        return obj.author == request.user
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


    # Add filtering & search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["title", "content"]   # exact match filtering
    search_fields = ["title", "content"]      # partial match search

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # ✅ auto-assign logged-in user


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set the logged-in user as the author
        serializer.save(author=self.request.user)

class FeedView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")
