# Import the include and path functions from django.urls
from django.urls import include, path

# Import the admin module from blog_app (this is a bit unusual as admin is typically imported from django.contrib)
from blog_app import admin

# Import the views module from the current directory
from . import views

# Define the URL patterns for the application
urlpatterns = [
    # Root URL (e.g., http://127.0.0.1:8000/), mapped to the blog_list view
    path('', views.blog_list, name='blog_list'),

    # URL pattern for viewing a specific blog post by primary key (e.g., http://127.0.0.1:8000/1/)
    path('<int:pk>/', views.blog_detail, name='blog_detail'),

    # URL pattern for creating a new blog post (e.g., http://127.0.0.1:8000/new/)
    path('new/', views.blog_create, name='blog_create'),

    # URL pattern for editing a specific blog post by primary key (e.g., http://127.0.0.1:8000/1/edit/)
    path('<int:pk>/edit/', views.blog_update, name='blog_update'),

    # URL pattern for deleting a specific blog post by primary key (e.g., http://127.0.0.1:8000/1/delete/)
    path('<int:pk>/delete/', views.blog_delete, name='blog_delete'),
]
