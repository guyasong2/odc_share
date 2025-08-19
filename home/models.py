from django.db import models
from django.contrib.auth.models import User
import uuid

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
