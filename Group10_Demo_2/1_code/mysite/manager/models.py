# -*- coding: utf-8 -*-
#Models is the single, definitive source of data about the apps data. It contains the essential fields and behaviors of the data. Generally, each model maps to a single database table.
#Each model is a subclass of models.Model
#Each attribute of the model maps to a database column with each field being an instance of the appropriate Field class.
#Django provides database-access queries in a well documented API

# The following imports models from the parking system parking/models.py.
from __future__ import unicode_literals
#Import required Django packages.
from django.contrib.auth.models import Permission, User
from django.core.validators import RegexValidator
from django.db import models
#Import models from garageAutomation ------------------------
from garageAutomation.models import Account, Vehicle, PaymentMethod, ParkingSession
#Import models from parking to establish a relationship.
from parking.models import Parking_Lot, Spot, Session, ActiveSession, Image
#Import packages to help with logical functions.
import datetime, random
from django.utils import timezone 

# Create your models here.

#class displayTrans():

#class verify():

class Price(models.Model):
	"""Initialize a standalone price field"""
	#Initialize a value field with a positive integer type of default value of the price,$10/hr.
	value = models.PositiveIntegerField(default=10)
	#Print the current price.
	def __str__(self):
		return self.value
	def print_value(self): 
		return self.value	
	#Change the current price into new_value.
	def change(self, new_value):
		if new_value > 0:
			value = new_value
		else:
			return "Invalid price!"

class Revenue(models.Model):
	#Initialize a amount field with a positive integer type
	amount = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.amount
class TransHis(models.Model):
	"""Transaction History"""
	account= Account
	pm = PaymentMethod
	vehicle = Vehicle
	parkingsession = ParkingSession
#	parking_lot = Parking_Lot
	spot = Spot
	#Fetch the session info.
	session = Session

		

'''
class CheckAcct(object):
	"""docstring for CheckAcct"""
	def __init__(self, arg):
		super(CheckAcct, self).__init__()
		self.arg = arg
		

class Plot(models.Models):
 	"""Takes data from the database and plot """
 	def __init__(self, arg):
 		super(ClassName, self).__init__()
 		self.arg = arg
 		
class History(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

class SearchHistory(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
		'''
