from django.contrib import admin
from home.models import Room,SharedFile

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ["id","room_name", "created_by", "created_at", "code"]

admin.site.register(Room, RoomAdmin)

class RoomFiles(admin.ModelAdmin):
    list_display = ["room", "file", "uploaded_at"]
admin.site.register(SharedFile, RoomFiles)

