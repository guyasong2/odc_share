from django.db import models
from django.contrib.auth.models import User
import uuid

# Function to separate location of files uploaded per room created
def upload_to_room(instance, filename):
    return f"room_files/{instance.room.code}/{filename}"

class Room(models.Model):
    room_name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=200, null=True)
    code = models.CharField(max_length=6, unique=True, editable=False, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rooms", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name="joined_rooms", blank=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(uuid.uuid4())[:6].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.room_name}"


class RoomFile(models.Model): # The model for files of a room
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="files")
    uploader = models.ForeignKey(User, models.CASCADE, related_name="uploaded_files", null=True)
    file = models.FileField(upload_to=upload_to_room)
    original_filename = models.TextField(max_length=255, null=True, editable=False, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    

class RoomMembership(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="memberships")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="room_memberships")
    joined_at = models.DateTimeField(auto_now_add=True)
    is_moderator = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('room', 'user')