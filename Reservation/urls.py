from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('list', views.reservation_list_hotel, name='reservation_list_hotel'),
    path('<int:pk>/cancel/', views.cancel_reservation, name='cancel_reservation'),
]
