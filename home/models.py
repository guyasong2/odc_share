from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    # Basic room info
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Who created the room
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_rooms')

    # Room settings
    max_participants = models.PositiveIntegerField(default=10)
    is_private = models.BooleanField(default=False)
    password = models.CharField(max_length=50, blank=True, null=True)  # Optional password for private rooms

    # Status
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class RoomParticipant(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='joined_rooms')
    joined_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)  # To allow the host or selected participants to manage the room

    class Meta:
        unique_together = ('room', 'user')  # Prevent a user from joining the same room twice

    def __str__(self):
        return f"{self.user.username} in {self.room.name}"