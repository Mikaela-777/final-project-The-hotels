from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_room, name='create_room'),
    path('edit/<int:pk>/', views.edit_room, name='edit_room'),
    path('delete/<int:pk>/', views.delete_room, name='delete_room'),
    path('', views.room_list, name='room_list'),
    path('pesan/<str:room_type>/', views.pesan_kamar, name='pesan_kamar'),
    path('room_setting/', views.room_setting, name='setting_room')
]
