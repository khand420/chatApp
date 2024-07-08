from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/<str:group_name>/', views.group_index),
]