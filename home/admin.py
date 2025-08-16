from django.contrib import admin
from home.models import Room, RoomParticipant

# Register your models here.
class createRoomAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
admin.site.register(Room, createRoomAdmin)

class RoomParticipantAdmin(admin.ModelAdmin):
    list_display = ["room", "user"]
admin.site.register(RoomParticipant, RoomParticipantAdmin)