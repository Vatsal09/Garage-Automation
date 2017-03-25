# The following is used for manager. Will wait till manager is done
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.validators import RegexValidator
from django.db import models
from garageAutomation.models import Account, Vehicle
import random
import datetime
# Create your models here.

# class Session(models.Model):
#     current_date = models.DateField(_("Date"), default=datetime.date.today)
#
#     def __str__(self):
#         return str(self.id)

class Parking_Lot(models.Model):
	# Initialize after manager has been created
	user = models.ForeignKey(User, default=1)
	address = models.CharField(max_length= 150)
	max_levels = models.CharField(max_length = 3, validators=[RegexValidator(r'^\d{1,3}$')])
	max_spots = models.CharField(max_length = 5, validators=[RegexValidator(r'^\d{1,5}$')])

	def __str__(self):
		return str(self.id)

	# Function to check number of spots open
	def num_spots_open(self): #This needs to be checked
		open_spots = Spot.objects.filter(is_occupied = False).count() #This needs to be checked
		return open_spots

class Spot(models.Model):
	# 1 -M relationship between Parking_Lot and Spot
	parkingLot = models.ForeignKey(Parking_Lot, on_delete=models.CASCADE)
	# Physical number of the parking spot
	spot_number = models.CharField(max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')])
	# Sensor id number associated witht he spot_number
	sensor_id = models.CharField(max_length = 10, validators=[RegexValidator(r'^\d{1,10}$')])
	# Level of the spot
	level = models.CharField(max_length = 3, validators=[RegexValidator(r'^\d{1,3}$')])
	# Is the space occupied or not
	is_occupied = models.BooleanField(default= False)
	# Disabled by manager
	is_disabled = models.BooleanField(default= False)

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
			return "Yes"
		return "No"
	# Function to check if spot is disabled
	def sensor_disable_status(self):
		if(self.is_disabled):
			return "Yes"
		return "No"
	# Updates sensor status
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

class Session(models.Model):
    parkingLot = models.ForeignKey(Parking_Lot, on_delete=models.CASCADE, blank = True)
    #vehicle = models.OneToOneField(Vehicle)
    CreditCard = models.CharField(max_length = 16, blank = True)

    license_plate_number = models.CharField(max_length = 7, validators=[RegexValidator(r'^[A-Z0-9]{6,7}$')], blank = True)
    time_arrived = models.CharField(max_length = 10, blank = True)
    time_exited = models.CharField(max_length = 10, blank = True)
    stay_length = models.CharField(max_length = 2, blank = True)
    amount_charged = models.CharField(max_length = 5, blank = True)
	#CC = models.CharField(max_length = 16, blank = True)

    #account = models.ForeignKey(Account, on_delete=models.CASCADE)

    #time_arrived = models.DateTimeField(auto_now=True)
    #date_arrived = models.DateField(_("Date"), default=datetime.date.today)
    user_type = models.CharField(max_length = 1)

    def __str__(self):
        return str(self.id)

class RegisteredUser(models.Model):
    reg_user = 	models.OneToOneField(Session)
    #account = models.OneToOneField(Account)
    #vehicle = models.OneToOneField(Vehicle)
    user_type = models.CharField(max_length = 1, default=1)

class GuestUser(models.Model):
    guest_user = models.OneToOneField(Session)
    #CC = models.CharField(max_length = 16)
    user_type = models.CharField(max_length = 1, default=2)

class CashUser(models.Model):
    cash_user = models.OneToOneField(Session)
    hasPaid = models.BooleanField(default = False)
    user_type = models.CharField(max_length = 1, default=3)
