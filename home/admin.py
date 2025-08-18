from django.contrib import admin
from home.models import Room, RoomFile, RoomMembership

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ["room_name", "created_by", "created_at", "code"]

admin.site.register(Room, RoomAdmin)
admin.site.register(RoomMembership)

@admin.register(RoomFile)
class RoomFileAdmin(admin.ModelAdmin):
    list_display = ('original_filename', 'room', 'uploader', 'uploaded_at')
    list_filter = ('uploaded_at', 'room')
    search_fields = ('original_filename',)