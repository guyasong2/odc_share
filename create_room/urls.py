from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_rooms, name='list_rooms'),
    path('create_room/', views.create_room, name='create_room'),
    path('join_room/', views.join_room, name='join_room'),
]
