from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookmark_list, name='bookmark_list'),
    path('add/', views.add_bookmark, name='add_bookmark'),
    path('edit/<int:pk>/', views.edit_bookmark, name='edit_bookmark'),
    path('delete/<int:pk>/', views.delete_bookmark, name='delete_bookmark'),  # Define the URL pattern for deleting
    # Add other URL patterns as needed
]
