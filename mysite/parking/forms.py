#Import forms, which is a set of data.
from django import forms
from django.contrib.auth.models import User
from .models import Parking_Lot, Spot, Session, ActiveSession, Image

#Creating a form from the Parking_Lot model.
class ParkingLotForm(forms.ModelForm):

    class Meta:
        model = Parking_Lot
	#Creating a form field for each model field.
        fields = ['address', 'max_levels', 'max_spots']


#Creating a form from the Spot model.
class SpotForm(forms.ModelForm):

    class Meta:
        model = Spot
	#Creating a form field for each model field.
        fields = ['spot_number', 'sensor_id', 'level']


#Creating a form from the User model.
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
	#Creating a form field for each model field.
        fields = ['username', 'email', 'password']


#Creating a form from the Session model.
class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
	#Creating a form field for each model field.
        fields = ['license_plate_number']
#Creating a form from the Session model.
class ActiveSessionForm(forms.ModelForm):

    class Meta:
        model = ActiveSession
    #Creating a form field for each model field.
        fields = ['license_plate_number']


#Creating a guest form from the Session model.
class GuestSessionForm(forms.ModelForm):

    class Meta:
        model = Session
	#Creating a form field for each model field.
        fields = ['Credit_Card']

#Creating a upload image form
class ImageUploadForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ['image']
