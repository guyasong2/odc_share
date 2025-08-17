from django.shortcuts import render
from home.models import Room

def list_rooms(request):
    rooms = Room.objects.all()
    return render(request, "list_room.html", {"rooms": rooms})