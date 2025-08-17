from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("create/", views.dashboard, name="create_room"), 
    path("join/", views.dashboard, name="join_room"),  
    path("room/<str:code>/", views.room_detail, name="room_detail"),
]
