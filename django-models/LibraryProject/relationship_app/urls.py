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
from . import views
   

urlpatterns = [
    path('logout/', 
         LogoutView.as_view(template_name='relationship_app/logout.html'), 
         name='logout'
         ),

    path('register/', 
         views.register,
         name='register'
         ),

     path('login/', 
         LoginView.as_view(template_name='relationship_app/login.html'), 
         name='login'
         ),

]


from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

