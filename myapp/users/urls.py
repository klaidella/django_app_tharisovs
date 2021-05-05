from django.urls import path
from django.contrib import admin

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_user', views.AddUserFormView.as_view(), name='add_user'),
    path('get_user/<pk>/', views.GetUserView.as_view(), name='get_user'),
    path('edit_user/<pk>/', views.UserUpdateView.as_view(), name='edit_user'),
    path('delete_user/<pk>/', views.UserDeleteView.as_view(), name='delete_user'),
]

