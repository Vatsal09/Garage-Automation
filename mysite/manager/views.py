# Import python packages for logical functions.
import time
import random
import datetime
import openalpr_api
import os
from django.core.exceptions import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.template import loader
# Package to custom build a functioning authentication system
from django.contrib.auth import authenticate, login, logout
# Package to create complex lookup queries.
from django.db import models
from django.db.models import Q
# Import local models and forms from parking directory.
from parking.forms import ParkingLotForm, SpotForm, UserForm, SessionForm, ActiveSessionForm, GuestSessionForm, ImageUploadForm
from .models import Parking_Lot, Spot, Session, ActiveSession
# Import garageAutomation models.
from garageAutomation.models import Account, Vehicle, ParkingSession, PaymentMethod
from django.core.urlresolvers import reverse

from django import template
from datetime import date, timedelta
register = template.Library()
def index(request):
#	return HttpResponse("This is the manager's page.")
#	a = HttpResponse(".")
#	template = loader.get_template('pageone.html')
#	context={"<p>This is the URL for second page:</p>"}
#	return HttpResponse(template.render(request))
#	return render(request, 'pageone.html')
	return render(request, 'manager/index.html')
# The view that gets called for the HTTP request of url /manager/analytics

#This function displays a graph of # of customers vs. date/time. 
def analytics(request):
	# Check if the user that generates the Http request is authenticated
	if not request.user.is_authenticated():
		 # If not, go back to the login form.
		return render(request, 'manager/index.html')
	else:
		 # If authenticated, go to analytics page.	
  		return render(request,'manager/analytics.html')

#This function displays the most recent 10 transactions and prints it.   		
def history(request):
	if not request.user.is_authenticated():
		 # If not, go back to the login form.
		return render(request, 'manager/index.html')
	else:
		 # If authenticated, go to analytics page.	
  		return render(request,'manager/history.html')	

#This function takes license # and prints the transactions being searched for.
def searchlicense(request):
	if request.method == 'POST':
	 # Initialize the SpotForm with POST data.
#        form = SpotForm(request.POST or None)
        # Initialize Parking_Lot instance with the correct parkingLot_id
#        parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
		search_id= get_object_or_404(Vehicle, v= license_plate) 
		try:
			vehicle = Vehicle.objects.get(license_plate = search_id)
			# Interact with the user
			html = ("<H1>%s</H1>",vehicle)
			return HttpResponse(html)
		except Vehicle.DoesNotExist:
			return HttpResponse("No such customer found!")
	else:
		return render(request, 'manager/history.html')













'''		pm = PaymentMethod
		vehicle = Vehicle
		parkingsession = ParkingSession
#		
		spot = Spot
		
		seession = Session
        # Check if form is valid.
        if form.is_valid():
            #Initialize list of all the spots in the lot.
            parkingLots_spots = parkingLot.spot_set.all()
            #Check to see if the spot getting added is already a spot in the parking_lot.
            if parkingLot.spot_set.filter(level = form.cleaned_data.get('level')).filter(spot_number = form.cleaned_data.get('spot_number')):
                context = {'parkingLot': parkingLot,'form': form,'error_message': 'You already added that spot'}
                return render(request, 'parking/add_spot.html',context)
            #Otherwise add the spot to the lot and save the form.
            spot = form.save(commit=False)
            spot.parkingLot = parkingLot
            spot.save()
            return render(request, 'parking/detail.html',{'parkingLot': parkingLot})
        #If form is invalid then render add_spot again.
        context = {'parkingLot': parkingLot, 'form': form}
    return render(request, 'parking/add_spot.html', context) '''

