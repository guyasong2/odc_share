from django.contrib import admin
from home.models import Room

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ["room_name", "created_by", "created_at", "code"]

admin.site.register(Room, RoomAdmin)

