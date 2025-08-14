from django.shortcuts import render

def home(request):
    rooms = [{"name": "Orange digital center"}] * 8
    return render(request, "home.html", {"rooms": rooms})

