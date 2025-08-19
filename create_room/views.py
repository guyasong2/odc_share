from django.shortcuts import render,redirect, get_object_or_404
from home.models import Room

def list_rooms(request):
    rooms = Room.objects.all()
    return render(request, "list_room.html", {"rooms": rooms})

def join(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        code_entered = request.POST.get('room_code')
        if code_entered == room.code: 
            return redirect('room_detail_by_id', room_id=room.id)
        else:
            error = "Incorrect room code"
            return render(request, 'join.html', {'room': room, 'error': error})

    return render(request, 'join.html', {'room': room})