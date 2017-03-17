from django import forms
from django.contrib.auth.models import User

from .models import Parking_Lot, Spot


class ParkingLotForm(forms.ModelForm):

    class Meta:
        model = Parking_Lot
        fields = ['address', 'max_levels', 'max_spots']


class SpotForm(forms.ModelForm):

    class Meta:
        model = Spot
        fields = ['spot_number', 'sensor_id', 'level']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']