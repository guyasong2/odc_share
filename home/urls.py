from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_room, name='create_room'),
    path('join/<int:room_id>/', views.join_room, name='join_room'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
]
