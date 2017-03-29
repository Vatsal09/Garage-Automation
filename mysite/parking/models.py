#Models is the single, definitive source of data about the apps data. It contains the essential fields and behaviors of the data. Generally, each model maps to a single database table.
#Each model is a subclass of models.Model
#Each attribute of the model maps to a database column with each field being an instance of the appropriate Field class.
#Django provides database-access queries in a well documented API

# The following is used for manager. Will wait till manager is done
from __future__ import unicode_literals
#Import required Django packages
from django.contrib.auth.models import Permission, User
from django.core.validators import RegexValidator
from django.db import models
#Import models from garageAutomation to establish a relationship.
from garageAutomation.models import Account, Vehicle

#Import packages to help with logical functions
import random
import datetime

#Parking_Lot model.
class Parking_Lot(models.Model):
	#Initialize after manager has been created
	#Initialize a user field with a one-to-many relationship to the User model with a default value of 1.
	user = models.ForeignKey(User, default=1)
	#Initialize an address field with a char data type of max_length of 150.
	address = models.CharField(max_length= 150)
	#Initialize a max_levels field with a char data type of max_length of 3.
	max_levels = models.CharField(max_length = 3, validators=[RegexValidator(r'^[1-9]\d{0,2}$')])
	#Initialize a max_spots field with a char data type of max_length of 5.
	max_spots = models.CharField(max_length = 5, validators=[RegexValidator(r'^[1-9]\d{0,4}$')])

	#A python method that returns a unicode representation of the model. This is what is displayed when the model is called as a string.
	def __str__(self):
		#Return the id of the Parking_Lot as a string.	
		return str(self.id)

	# Function to check number of spots open
	def num_spots_open(self): #This needs to be checked
		open_spots = Spot.objects.filter(is_occupied == False).count() #This needs to be checked
		return open_spots
#Spot model
class Spot(models.Model):
	#Initialize a parkingLot field with a many-to-one relationship to the Parking_Lot model.
	#If the parkingLot gets deleted then all the spots in the relationship gets deleted.
	parkingLot = models.ForeignKey(Parking_Lot, on_delete=models.CASCADE)
	#Initialize a spot_number field with the number of the parking spots with an int data type.
	spot_number = models.IntegerField(validators= [RegexValidator(r'^[1-9]{0,10}$')])
	#Initialize a sensor_id field associated with the spot with char data type with a max_length of 10.
	sensor_id = models.CharField(max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')])
	#Initialize a level field associated with the level of the spot
	level = models.CharField(max_length = 3, validators=[RegexValidator(r'^[1-9]{1,3}$')])
	#Initialize a is_occupied boolean field to determine if the Spot is occupied, defaulting to false.
	is_occupied = models.BooleanField(default= False)
	#Initialize a is_disabled boolean field to determine if the Spot is disabled, defaulting to false.
	is_disabled = models.BooleanField(default= False)

	#A python method that returns a unicode representation of the model. This is what is displayed when the model is called as a string.
	def __str__(self):
		result = "Not Sure if Occupied"
		if(self.is_occupied):
			result = "Occupied"
		else:
			result = "Not Occupied"

		return self.spot_number + ' - ' + self.sensor_id + ' - ' + result

	#Function to check if spot is open
	def is_open(self):
		if(self.is_occupied):
			return "Yes"
		return "No"
	#Function to check if spot is disabled
	def sensor_disable_status(self):
		if(self.is_disabled):
			return "Yes"
		return "No"
	#Function to update sensor status
	def update_sensor_status(self):
		self.is_occupied = bool(random.getrandbits(1))
		self.save()
		return "Sensor status for " + self.spot_number + " updated"

# class Sensor(models.Model):
# 	spot = models.OneToOneField(Spot, on_delete=models.CASCADE, primary_key=True)
# 	sensor_id = models.CharField(max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')])
# 	sensor_status = models.BooleanField(default= True)
# 	# Function to check if spot is open
# 	def check_status(self):
# 		if(self.is_occupied):
# 			return True
# 		return False
#Session model
class Session(models.Model):
    #Initialize a parkingLot field to create a many-to-one relationship to the Parking_Lot model.
    #If the parkingLot gets deleted then all the sessions in the relationship gets deleted.
    parkingLot = models.ForeignKey(Parking_Lot, on_delete=models.CASCADE, blank = True)
    # vehicle = models.OneToOneField(Vehicle)
    
    #Initialize a Credit_Card field associated with the session with char data type with a max_length of 16.
    Credit_Card = models.CharField(max_length = 16, blank = True)

    #Initialize a license_plate_number field associated with the session with char data type with a max_length of 7.
    license_plate_number = models.CharField(max_length = 7, validators=[RegexValidator(r'^[A-Z0-9]{6,7}$')], blank = True)
    #Initialize a time_arrived field associated with the session with char data type with a max_length of 10.
    time_arrived = models.CharField(max_length = 10, blank = True)
    #Initialize a time_exited field associated with the session with char data type with a max_length of 10.
    time_exited = models.CharField(max_length = 10, blank = True)
    #Initialize a stay_length field associated with the session with char data type with a max_length of 2.
    stay_length = models.CharField(max_length = 2, blank = True)
    #Initialize a amount_charged field associated with the session with char data type with a max_length of 5.
    amount_charged = models.CharField(max_length = 5, blank = True)
    #account = models.ForeignKey(Account, on_delete=models.CASCADE)

    #time_arrived = models.DateTimeField(auto_now=True)
    #date_arrived = models.DateField(_("Date"), default=datetime.date.today)
    #Initialize a user_type field associated with the session with char data type with a max_length of 1.
    user_type = models.CharField(max_length = 1)

    def __str__(self):
        return str(self.id)

# class RegisteredUser(models.Model):
#     reg_user = 	models.OneToOneField(Session)
#     #account = models.OneToOneField(Account)
#     #vehicle = models.OneToOneField(Vehicle)
#     user_type = models.CharField(max_length = 1, default=1)
#
# class GuestUser(models.Model):
#     guest_user = models.OneToOneField(Session)
#     #CC = models.CharField(max_length = 16)
#     user_type = models.CharField(max_length = 1, default=2)
#
# class CashUser(models.Model):
#     cash_user = models.OneToOneField(Session)
#     hasPaid = models.BooleanField(default = False)
#     user_type = models.CharField(max_length = 1, default=3)
