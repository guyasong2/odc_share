from django.shortcuts import render, redirect, get_object_or_404
from home.models import Room
from home.forms import RoomForm, JoinRoomForm
from django.contrib.auth.decorators import login_required


def home(request):
    rooms = Room.objects.all()
    return render(request, "home.html", {"rooms":rooms})

@login_required
def dashboard(request):
    create_form = RoomForm()
    join_form = JoinRoomForm()

    if request.method == "POST":
        if "create_room" in request.POST:
            create_form = RoomForm(request.POST)
            if create_form.is_valid():
                room = create_form.save(commit=False)
                room.created_by = request.user
                room.save()
                return redirect("room_detail", code=room.code)

        elif "join_room" in request.POST:
            join_form = JoinRoomForm(request.POST)
            if join_form.is_valid():
                code = join_form.cleaned_data["code"]
                try:
                    room = Room.objects.get(code=code)
                    room.members.add(request.user)
                except Room.DoesNotExist:
                    join_form.add_error("code", "Room not found")
                return redirect("room_detail", code=room.code)

    return render(request, "dashboard.html", {
        "create_form": create_form,
        "join_form": join_form,
    })

@login_required
def room_detail(request, code):
    rooms = get_object_or_404(Room, code=code)
    return render(request, "room_detail.html", {"rooms": rooms})
