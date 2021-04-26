from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_user', views.add_user, name='add_user'),
    path('get_user/<int:user_id>', views.get_user, name='get_user'),
    path('edit_user/<int:user_id>', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>', views.delete_user, name='delete_user'),
]

