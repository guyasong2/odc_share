from django.shortcuts import render

def list_rooms(request):
    return render(request, "list_room.html")

def create_room(request):
    return render(request, "create_room.html")

def join_room(request):
    return render(request, "join_room.html")