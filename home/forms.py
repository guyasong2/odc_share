from django import forms
from .models import Room, RoomParticipant

class RoomForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Optional password for private rooms'})
    )

    class Meta:
        model = Room
        fields = ['name', 'description', 'max_participants', 'is_private', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Room name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe your room', 'rows': 3}),
            'max_participants': forms.NumberInput(attrs={'min': 2}),
            'is_private': forms.CheckboxInput(),
        }

class JoinRoomForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter room password if required'})
    )

    class Meta:
        model = RoomParticipant
        fields = ['user']  # room will be selected in the view
