from django.urls import path
from .views import submit_feedback
from . import views

urlpatterns = [
    path("", submit_feedback, name="submit_feedback"),
    path("list", views.feedback_list, name="feedback_list"),

]
