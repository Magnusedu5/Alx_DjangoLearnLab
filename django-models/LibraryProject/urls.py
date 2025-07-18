from django.contrib import admin
from django.urls import path, include
from .views import list_books, bookviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('relationship/', include('relationship_app.urls')),  # 👈 link to app URLs
]