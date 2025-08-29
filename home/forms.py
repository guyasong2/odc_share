from django import forms
from .models import Room, SharedFile


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["room_name", "description"]
        widgets = {
            "room_name": forms.TextInput(attrs={
                "class": "w-full border border-gray-300 rounded-lg p-2",
                "placeholder": "Enter room name..."
            }),
            "description": forms.TextInput(attrs={
                "class": "w-full border border-gray-300 rounded-lg p-2",
                "placeholder": "Enter description"
            })
        }


class JoinRoomForm(forms.Form):
    code = forms.CharField(
        max_length=8,
        widget=forms.TextInput(attrs={"class": "w-full border border-gray-300 rounded-lg p-2",
            "placeholder": "Enter room code..."})
    )


class SharedFileForm(forms.ModelForm):
    class Meta:
        model = SharedFile
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'border rounded-lg p-2 w-full mb-3 sm:mb-3 md:mb-3 '})
        }