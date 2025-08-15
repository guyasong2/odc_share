from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    rooms = [{"name": "Orange digital center"}] * 8
    return render(request, "home.html", {"rooms": rooms})

@login_required
def dashboard(request):
    return render(request, "dashboard.html")




