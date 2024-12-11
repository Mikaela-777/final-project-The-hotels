from django.urls import path
from . import views

urlpatterns = [
    path('/create/', views.create_room, name='create_room'),
    path('/edit/<int:pk>/', views.edit_room, name='edit_room'),
    path('/delete/<int:pk>/', views.delete_room, name='delete_room'),
    path('', views.room_list, name='room_list'),  # Tambahkan list untuk daftar Room
]
