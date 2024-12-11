from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_reservation, name='create_reservation'),
    path('delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
    path('', views.reservation_list, name='reservation_list'),  # Halaman daftar reservasi
]
