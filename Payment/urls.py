from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('create/<int:reservation_id>/', views.create_payment, name='create_payment'),
    path('alllist', views.payment_list_all, name='payment_list_all'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)