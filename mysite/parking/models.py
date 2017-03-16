# The following is used for manager. Will wait till manager is done

# from django.contrib.auth.models import Permission, User
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Parking_Lot(models.Model):
	# Initialize after manager has been created 
	# manager = models.ForeignKey(User, default=1)	
	address = models.CharField(max_length= 150)
	max_levels = models.Charfield(max_length = 3, validators=[RegexValidator(r'^\d{1,3}$')])
	max_spots = models.Charfield(max_length = 5, validators=[RegexValidator(r'^\d{1,5}$')])

	def __str__(self):
		return self.id

	# Function to check number of spots open
	def num_spots_open(self): #This needs to be checked
		
		open_spots = Spot.objects.filter(is_occupied = False).count() #This needs to be checked
		return open_spots 




class Spot(models.Model):
	# 1 -M relationship between Parking_Lot and Spot
	lot = models.ForeignKey(Parking_Lot, on_delete=models.CASCADE)
	# Physical number of the parking spot 
	spot_number = models.CharField(max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')])
	# Sensor id number associated witht he spot_number
	sensor_id = models.CharField(max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')])
	# Level of the spot 
	level = models.Charfield(max_length = 3, validators=[RegexValidator(r'^\d{1,3}$')])
	# Is the space occupied or not
	is_occupied = models.BooleanField(default= True)

	def __str__(self):
		result = "Not Sure if Occupied"
		if(self.is_occupied):
			result = "Occupied"
		else:
			result = "Not Occupied"

		return self.spot_number + ' - ' + self.sensor_id + ' - ' + result

	# Function to check if spot is open
	def is_open(self):
		if(self.is_occupied):
			return True
	return False

