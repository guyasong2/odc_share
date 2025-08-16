from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from home.models import Room, RoomParticipant
from home.forms import RoomForm, JoinRoomForm
from django.contrib.auth.decorators import login_required

@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            if not room.is_private:
                room.password = ''
            room.save()
            # Add host as participant automatically
            RoomParticipant.objects.create(room=room, user=request.user, is_admin=True)
            messages.success(request, f"Room '{room.name}' created successfully!")
            return redirect('room_detail', room_id=room.id)
    else:
        form = RoomForm()
    return render(request, 'dashboard.html', {'form': form})

@login_required
def join_room(request, room_id):
    room = get_object_or_404(Room, id=room_id, is_active=True)
    if request.method == 'POST':
        form = JoinRoomForm(request.POST)
        if form.is_valid():
            password = request.POST.get('password')
            if room.is_private and room.password != password:
                messages.error(request, "Incorrect password!")
            else:
                # Add participant if not already joined
                participant, created = RoomParticipant.objects.get_or_create(
                    room=room,
                    user=request.user
                )
                if created:
                    messages.success(request, f"You joined '{room.name}'!")
                else:
                    messages.info(request, f"You are already in '{room.name}'!")
                return redirect('room_detail', room_id=room.id)
    else:
        form = JoinRoomForm()
    return render(request, 'dashboard.html', {'form': form, 'room': room})

@login_required
def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id, is_active=True)
    participants = room.participants.all()
    return render(request, 'room_detail.html', {'room': room, 'participants': participants})

def home(request):
    rooms = [{"name": "Orange digital center"}] * 8
    return render(request, "home.html", {"rooms": rooms})

@login_required
def dashboard(request):
    return render(request, "dashboard.html")




