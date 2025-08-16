from django.shortcuts import render

def list_rooms(request):
    rooms = [{"name": "Orange digital center"}] * 8
    return render(request, "list_room.html", {"rooms": rooms})