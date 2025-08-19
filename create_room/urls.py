from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_rooms, name='list_rooms'),
    path('join-room/<int:room_id>/', views.join, name='join_room'),
]
