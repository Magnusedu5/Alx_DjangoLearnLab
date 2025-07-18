from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('view_books/<int:pk>/', views.LibraryDetailView.as_view(), name='view_books')
]

#user login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView
   

urlpatterns = [
    path('logout/', 
         LogoutView.as_view(template_name='relationship_app/logout.html'), 
         name='logout'
         ),

    path('register/', 
         RegisterView.as_view(), 
         name='register'
         ),

     path('login/', 
         LoginView.as_view(template_name='relationship_app/login.html'), 
         name='login'
         ),

]