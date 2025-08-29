from django.shortcuts import render, redirect, get_object_or_404
from home.models import Room
from home.forms import RoomForm, JoinRoomForm, SharedFileForm
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
                return redirect('room_detail_by_code', code=room.code)

        elif "join_room" in request.POST:
            join_form = JoinRoomForm(request.POST)
            if join_form.is_valid():
                code = join_form.cleaned_data["code"]
                try:
                    room = Room.objects.get(code=code)
                    room.members.add(request.user)
                except Room.DoesNotExist:
                    join_form.add_error("code", "Room not found")
                return redirect('room_detail_by_code', code=room.code)

    return render(request, "dashboard.html", {
        "create_form": create_form,
        "join_form": join_form,
    })

@login_required
def room_details(request, room_id):  # must accept room_id
    room = get_object_or_404(Room, id=room_id)
    files = room.files.all()

    # Only admin can upload
    if request.user == room.created_by:
        if request.method == "POST":
            form = SharedFileForm(request.POST, request.FILES)
            if form.is_valid():
                shared_file = form.save(commit=False)
                shared_file.room = room
                shared_file.uploaded_by = request.user
                shared_file.save()
                return redirect("room_detail_by_id", room_id=room.id)
        else:
            form = SharedFileForm()
    else:
        form = None

    return render(request, "room_detail.html", {
        "room": room,
        "files": files,
        "form": form
    })

def room_detail(request, code): 
    room = get_object_or_404(Room, code=code)
    files = room.files.all()

    # Only admin can upload
    if request.user == room.created_by:
        if request.method == "POST":
            form = SharedFileForm(request.POST, request.FILES)
            if form.is_valid():
                shared_file = form.save(commit=False)
                shared_file.room = room
                shared_file.uploaded_by = request.user
                shared_file.save()
                return redirect("room_detail_by_code", code=room.code)
        else:
            form = SharedFileForm()
    else:
        form = None

    return render(request, "room_detail.html", {
        "room": room,
        "files": files,
        "form": form
    })


def about(request):
    return render(request, "about.html")