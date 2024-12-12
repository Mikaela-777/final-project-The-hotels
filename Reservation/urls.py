from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
    path('list', views.reservation_list_hotel, name='reservation_list_hotel'),

]
