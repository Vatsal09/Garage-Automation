#!/usr/bin/python
# -*- coding: utf-8 -*-
# A view function, or view for short, is simply a Python function that takes a Web request and returns a Web response
# The two essential Django packages to utilize HTTP requests and to render Django's dynamic HTML tempaltes, HttpResponse and render

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Package to custom build a functioning authentication system
from django.contrib.auth import authenticate, login, logout
# Package to create complex lookup queries.
from django.db.models import Q
# Import local models and forms from parking directory.
from .forms import ParkingLotForm, SpotForm, UserForm, SessionForm, ActiveSessionForm, GuestSessionForm, ImageUploadForm
from .models import Parking_Lot, Spot, Session, ActiveSession
# Import garageAutomation models.
from garageAutomation.models import Account, Vehicle, ParkingSession, PaymentMethod
from django.core.urlresolvers import reverse

# Import python packages for logical functions.
import time
import random
import datetime
import openalpr_api
import os

# Create your views here.

# The view that gets called for the HTTP request of url /parking/
def index(request):
    # Check if user that generated the HTTP request is authenticated.
    if not request.user.is_authenticated():
        # If not, render the index.html template.
        # Specifically, call the render helper function that returns an HttpResponse object of the given template.
        return render(request, 'parking/index.html')
    # Filter the list of Parking_Lot objects with a user field associated with the authenticated user.
    parkingLots = Parking_Lot.objects.filter(user=request.user)
    # query contains the GET request
    query = request.GET.get('q')
    # The get request will display the sole Parking_Lot that belongs to the authenticated user with the correct address associated with that Parking_Lot.
    if query:
        parkingLots = parkingLots.filter(Q(address__icontains=query)).distinct()

        # spot_results = spot_results.filter(
        # ....Q(spot_number__icontains=query) |
        # ....Q(sensor_id__icontains=query)
        # ).distinct()

        return render(request, 'parking/main.html',
                      {'parkingLots': parkingLots})
    else:
    # If there is no GET request, then render all the available Parking_Lots associated with the user.
        return render(request, 'parking/main.html',
                      {'parkingLots': parkingLots})
    return render(request, 'parking/main.html')


# The view that gets called for the HTTP request of url /parking/add_lot
def add_lot(request):
    # Check if user that generated the HTTP request is authenticated.
    if not request.user.is_authenticated():
        # If not, render the index.html template.
        return render(request, 'parking/login_manager.html')
    else:
        # Initialize the ParkingLotForm with POST data.
        form = ParkingLotForm(request.POST or None)
        # Check if form is valid.
        if form.is_valid():
            # If form is valid, save the values of the form.
            parkingLot = form.save(commit=False)
            # Add the user to the formed save values.
            parkingLot.user = request.user
            # Save the form.
            parkingLot.save()
            # Add the transfer data to the context.
            # Return the HTTP request along with the template and the context.
            return render(request, 'parking/detail.html',{'parkingLot': parkingLot})
            # If form is invalid, return back to add_lot.html.
        context = {'form': form}
    return render(request, 'parking/add_lot.html', context)

# The view that gets called for the HTTP request of url /parking/parkingLot_id/delete_lot
def delete_lot(request, parkingLot_id):
    #Initialize the parkingLot object through a query for the parkingLot id.
    # Check if user that generated the HTTP request is authenticated.
    if not request.user.is_authenticated():
        # If not, render the index.html template.
        return render(request, 'parking/login_manager.html')
    else:
        parkingLot = Parking_Lot.objects.get(pk=parkingLot_id)
        #Delete the object from the database.
        parkingLot.delete()
        #Query the list of Parking_Lot objects associated with the user
        parkingLots = Parking_Lot.objects.filter(user=request.user)
    #Render main html template with the following contexts.
    return render(request, 'parking/main.html',
                  {'parkingLots': parkingLots})

# The view that gets called for the HTTP request of url /parking/parkingLot_id/add_spot
def add_spot(request, parkingLot_id):
    # Check if user that generated the HTTP request is authenticated.
    if not request.user.is_authenticated():
        # If not, render the index.html template.
        return render(request, 'parking/login_manager.html')
    else:
        # Initialize the SpotForm with POST data.
        form = SpotForm(request.POST or None)
        # Initialize Parking_Lot instance with the correct parkingLot_id
        parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
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
    return render(request, 'parking/add_spot.html', context)

# The view that gets called for the HTTP request of url /parking/parkingLot_id/delete_spot
def delete_spot(request, parkingLot_id, spot_id):
    # Check if user that generated the HTTP request is authenticated.
    if not request.user.is_authenticated():
        # If not, render the index.html template.
        return render(request, 'parking/login_manager.html')
    else:
        # Initialize the parkingLot object with parkingLot id
        parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
        # Initialize spot with spot id
        spot = Spot.objects.get(pk=spot_id)
        # Delete that spot from the database
        spot.delete()
    return render(request, 'parking/detail.html',
                  {'parkingLot': parkingLot})


#The view to display the details of the parking lot.
def detail(request, parkingLot_id):
    # Check if user that generated the HTTP request is authenticated.
    if not request.user.is_authenticated():
        # If not, render the index.html template.
        return render(request, 'parking/login_manager.html')
    else:
        #Initialize user as user of HTTP request.
        user = request.user
        #Initialize parkingLot instance with parkingLot id.
        parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
        #Return HTTP request for detail html template with the following context.
        return render(request, 'parking/detail.html',
                      {'parkingLot': parkingLot, 'user': user})

#View to register a new user.
def register_manager(request):
    # Initialize the SpotForm with POST data.
    form = UserForm(request.POST or None)
    # Check if form is valid.
    if form.is_valid():
        #If so create a new user
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        #Try to authenticate the new user with the username and password. authenticate(...) returns a user or none.
        user = authenticate(username=username, password=password)
        #Check if user was returned.
        if user is not None:
            #Check if user is activated.
            if user.is_active:
                #Login the user.
                login(request, user)
                #Retrieve all lots associated with user.
                parkingLots = Parking_Lot.objects.filter(user=request.user)
                #Render main html template.
                return render(request, 'parking/main.html',
                              {'parkingLots': parkingLots})
    context = {'form': form}
    return render(request, 'parking/register_manager.html', context)

#View for login manager/screen
def login_manager(request):
    #Check if request is POST request
    if request.method == 'POST':
        #Authenticate user with POST request fields.
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        #Check if user exists
        if user is not None:
            #Check if user is activated.
            if user.is_active:
                #Retrieve all lots associated with your account
                login(request, user)
                parkingLots = Parking_Lot.objects.filter(user=request.user)

                # Infinite loop for sensor checker activate
                # render(request, 'parking/update_occupancy')

                return render(request, 'parking/main.html',
                              {'parkingLots': parkingLots})
            else:
                #Render login manager with an error displaying account being disabled.
                return render(request, 'parking/login_manager.html',
                              {'error_message': 'Your account has been disabled'
                              })
        else:
            #Render login manager with an error displaying invalid login.
            return render(request, 'parking/login_manager.html',
                          {'error_message': 'Invalid login'})
    return render(request, 'parking/login_manager.html')

#View for logout.
def logout_manager(request):
    #Logout.
    logout(request)
    form = UserForm(request.POST or None)
    context = {'form': form}
    return render(request, 'parking/index.html', context)

#View for main parking lot page.
def main(request):
    # Check if user that generated the HTTP request is authenticated.
    if not request.user.is_authenticated():
        # If not, render the index.html template.
        return render(request, 'parking/login_manager.html')
    else:
        #Retrieve all lots associated with user.
        parkingLots = Parking_Lot.objects.filter(user=request.user)
        #Retrieve all spots.
        spot_results = Spot.objects.all()
        #Check if URL held GET request.
        query = request.GET.get('q')
        if query:
            #Display sole lot with address contained in GET request.
            parkingLots = parkingLots.filter(Q(address__icontains=query)).distinct()
            spot_results =  spot_results.filter(Q(spot_number__icontains=query)| Q(sensor_id__icontains=query)).distinct()
            return render(request, 'parking/main.html',
                          {'parkingLots': parkingLots,
                          'spots': spot_results})
        else:
            return render(request, 'parking/main.html',
                          {'parkingLots': parkingLots})

#View control for /parking/update_occupancy
def update_occupancy(request, parkingLot_id):
    # Check if user that generated the HTTP request is authenticated.
    if not request.user.is_authenticated():
        # If not, render the index.html template.
        return render(request, 'parking/login_manager.html')
    else:
        #Initialize parking_Lot object with id.
        parkingLot = Parking_Lot.objects.get(pk=parkingLot_id)
        #Initialize list of all spots in that parking_lot
        parkingLots_spots = parkingLot.spot_set.all()
        #For now give each spot in that lot a random occupancy.
        for s in parkingLots_spots:
            s.is_occupied = bool(random.getrandbits(1))
            s.save()
        return render(request, 'parking/detail.html',
                      {'parkingLot': parkingLot})


        # return render(request, 'parking/update_occupancy.html')
    # If the inifinite loop is to be activated for checker, uncomment below and uncomment the render request in login_manager(request) view
    # else:
    # .... while True:
    # ........ for s in Spot.objects.all():
    # ............ s.is_occupied = bool(random.getrandbits(1))
    # ............ s.save()
    # ........ time.sleep(10)

def disable_spot(request, parkingLot_id, spot_id):
    # Check if user that generated the HTTP request is authenticated.
    if not request.user.is_authenticated():
        # If not, render the index.html template.
        return render(request, 'parking/login_manager.html')
    else:
        #Initialize parkingLot object acquired by parkingLot_id
        parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
        #Inialize Spot object acquired by spot_id
        spot = Spot.objects.get(pk=spot_id)
        #Set is_disabled to be true to disable the spot.
        spot.is_disabled = True
        #Set is_occupied to be false.
        spot.is_occupied = False
        spot.save()
    #Render the detail template.
    return render(request, 'parking/detail.html',
                  {'parkingLot': parkingLot})


def enable_spot(request, parkingLot_id, spot_id):
    # Check if user that generated the HTTP request is authenticated.
    if not request.user.is_authenticated():
        # If not, render the index.html template.
        return render(request, 'parking/login_manager.html')
    else:
        #Initialize parkingLot object acquired by parkingLot_id
        parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
        #Inialize Spot object acquired by spot_id
        spot = Spot.objects.get(pk=spot_id)
        #Set is_disabled to be false to activate the spot.
        spot.is_disabled = False
        #Set is_occupied to be true.
        spot.is_occupied = True
        spot.save()
    #Render the detail template.
    return render(request, 'parking/detail.html',
                  {'parkingLot': parkingLot})

#Map view to render map.
def map(request, parkingLot_id, level):

    parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
    parkingLots_spots = parkingLot.spot_set.all()
    num_levels = parkingLot.max_levels
    num_levels = int(num_levels)
    level_1 = int(level)
    prev_level = int(level) - 1
    next_level = int(level) + 1
    last_spot_per_level = []
    last_spot_per_level.append(0)
    temp_num = 0
    for i in range(1, num_levels + 1):
        for s in parkingLots_spots:
            if int(s.level) == i and int(s.spot_number) > temp_num:
                temp_num = int(s.spot_number)
        last_spot_per_level.append(temp_num)

    # [0/1 100 113 455]

    data_max = last_spot_per_level[level_1]
    data_min = last_spot_per_level[level_1 - 1] + 1
    data_set = []

    # For even

    if data_max % 2 == 0:
        bottom_left = data_min
        top_left = round(float(data_max + data_min) / float(2) - 0.5)
        top_left = int(top_left)
        bottom_right = top_left + 1
        top_right = data_max
        data_set = [bottom_left, top_left, bottom_right, top_right]
    else:




        bottom_left = data_min
        top_left = (data_max + data_min) / 2 - 1
        bottom_right = top_left + 1
        top_right = data_max
        data_set = [bottom_left, top_left, bottom_right, top_right]

    # spots_left = []
    # spots_right = []
    # for x in parkingLots_spots :
    # .... if x.spot_number >= data_set[0] and x.spot_number <= data_set[1]:
    # ........ spots_left.append(x)
    # .... if x.spot_number >= data_set[2] and x.spot_number <= data_set[3]:
    # ........ spots_right.append(x)

    spots_left = Spot.objects.filter(parkingLot=parkingLot_id).filter(spot_number__gte=data_set[0]).filter(spot_number__lte=data_set[1])
    spots_right = Spot.objects.filter(parkingLot=parkingLot_id).filter(spot_number__gte=data_set[2]).filter(spot_number__lte=data_set[3])
    spots = zip(spots_left, spots_right)

    # left= Parking_Lot.objects.filter(pk=parkingLot_id).filter(spot.all().filter(spot_number__lte = data_set[0]).filter(spot_number__lte = data_set[1])
    # right = parkingLots_spots.objects.all().filter(int(spot_number)>= data_set[2]).filter(int(spot_number)<= data_set[3])

    # json_data_set = json.dumps(data_set)
    # json_level = json.dumps(level_1)
    # json_serializer = serializers.get_serializer("json")()
    # json_spots = json_serializer.serialize(parkingLot.spot_set.all())

    return render(request, 'parking/map.html', {
        'data_set': data_set,
        'level': int(level),
        'prev_level': int(prev_level),
        'next_level': int(next_level),
        'num_levels': num_levels,
        'parkingLot': parkingLot,
        'spots': spots,
        })


        # 'spots1': json_spots,
        # 'level': json_level,
        # 'data_set': json_data_set,

#View for system that coressponds to each parking lot.
def system(request, parkingLot_id):
    # Check if user that generated the HTTP request is authenticated.
    if not request.user.is_authenticated():
        # If not, render the index.html template.
        return render(request, 'parking/login_manager.html')
    else:
        user = request.user
        parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
        return render(request, 'parking/system.html',
                      {'parkingLot': parkingLot, 'user': user})


#View for enter_session,
def enter_session(request, parkingLot_id):
    #Receive form with post data.
    form = ImageUploadForm(request.POST, request.FILES)
    #Initialize parkingLot instance with parkingLot_id
    parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
    #Check if form is valid
    if form.is_valid():
        apiclient = openalpr_api.DefaultApi()
        key = os.environ.get('OPENALPR_SECRET_KEY', "sk_DEMODEMODEMODEMODEMODEMO")
        response = apiclient.recognize_post(key, "plate,color,make,makemodel", image='MEDIA_ROOT/pics/{}'.format(request.FILES['image'].name), country="us")

        plate_obj = response.plate.results[0]
        license_plate_number = plate_obj.plate
        #Try to acquire Vehicle object with license_plate_number
        try:
            v = Vehicle.objects.get(license_plate=license_plate_number)
        except Vehicle.DoesNotExist:
            v = None
        #Check if the license_plate is in a current session.
        try:
            check_session = ActiveSession.objects.get(license_plate_number=license_plate_number)
        except ActiveSession.DoesNotExist:
            check_session = None
        #Go through this logic if the license_plate does not have a current session.
        if check_session == None:
            if v != None:
                #Create a session
                session = form.save(commit=False)
                session.license_plate_number = license_plate_number
                #Give the session a user_type of 1
                session.user_type = 1
                #Set the session to have a time_arrived of the current time
                session.time_arrived = datetime.datetime.now().strftime('%H:%M:%S')
                #Set the parkingLot to the session
                session.parkingLot = parkingLot
                #Save the session.
                session.save()
                return render(request, 'parking/system.html',
                              {'parkingLot': parkingLot})
            #If vehicle does not exist then the vehicle does not belong to a current user.
            else:
                context = {'parkingLot': parkingLot,
                           'license_plate_number': license_plate_number}
                #Redirect to enter_guest view.
                return redirect('/{}/system/enter_guest/{}'.format(parkingLot_id,
                                license_plate_number),
                                parkingLot_id=parkingLot_id,
                                license_plate=license_plate_number)
        #If the license_plate already has a session then return an error message.
        else:
            context = {
                'parkingLot': parkingLot,
                'license_plate_number': license_plate_number,
                'form': form,
                'error_message': 'This vehicle is in another session.',
                }
            return render(request, 'parking/enter_session.html',
                          context)
    context = {'parkingLot': parkingLot, 'form': form}
    return render(request, 'parking/enter_session.html', context)

#View for exit_session.
def exit_session(request, parkingLot_id):
    #Receive form with post data.
    form = SessionForm(request.POST or None)
    #Initialize parkingLot instance with parkingLot_id
    parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
    #Check if form is valid.
    if form.is_valid():
        #Initialize license_plate_number with form data.
        license_plate_number = form.cleaned_data['license_plate_number']
        #Check if session exists
        try:
            check_session = ActiveSession.objects.get(license_plate_number=license_plate_number)
        except ActiveSession.DoesNotExist:
            check_session = None
        if check_session != None:
            store_session = form.save(commit=False)
            store_session.user_type = check_session.user_type
            #Set the session to have a time_arrived of the current time
            store_session.time_arrived = check_session.time_arrived
            #Set the parkingLot to the session
            store_session.parkingLot = check_session.parkingLot
            #Initialize values of the session
            #Give time_exited current time
            store_session.time_exited = datetime.datetime.now().strftime('%H:%M:%S')
            #Calculated stay_length base on time_exited and time_arrived.
            store_session.stay_length = int(store_session.time_exited[:2]) - int(check_session.time_arrived[:2])
            store_session.amount_charged = str(int(store_session.stay_length) * 5)
            store_session.save()
            check_session.delete()

            #Save parking session for user History
            session = ParkingSession()
            vehicle = Vehicle.objects.get(license_plate=license_plate_number)
            session.account = vehicle.account
            session.vehicle = vehicle
            #Uses the first available payment method
            session.paymentMethod = PaymentMethod.objects.filter(account=vehicle.account)[0]
            session.cost = store_session.amount_charged
            session.enter_time = datetime.datetime.now()
            session.duration = store_session.stay_length
            session.location = parkingLot_id
            session.save()

            return render(request, 'parking/system.html',
                          {'parkingLot': parkingLot})
        else:
            context = {'parkingLot': parkingLot,'error_message': 'This vehicle is not in a current session.','license_plate_number': license_plate_number}
            return render(request, 'parking/exit_session.html', context)

    context = {'parkingLot': parkingLot, 'form': form}
    return render(request, 'parking/exit_session.html', context)

#View if vehicle is not registered to a user.
def enter_guest(request, parkingLot_id, license_plate):
    #Initialize form with POST request data.
    form = GuestSessionForm(request.POST or None)
    #Initialize parkingLot
    parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
    #Check if form is valid
    if form.is_valid():
        #If valid initialize Session variables similar to enter_session()
        session = form.save(commit=False)
        session.license_plate_number = license_plate
        #Set user_type to 2 to correspond with a guest user.
        session.user_type = 2
        session.time_arrived = datetime.datetime.now().strftime('%H:%M:%S')
        session.parkingLot = parkingLot
        session.save()
        return render(request, 'parking/system.html',
                      {'parkingLot': parkingLot})
    context = {'parkingLot': parkingLot,
               'license_plate': license_plate, 'form': form}
    return render(request, 'parking/enter_guest.html', context)


def enter_cash_guest(request, parkingLot_id, license_plate):
    parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
    #Set the user_type to cash user
    session = Session(license_plate_number=license_plate, user_type='3'
                      ,
                      time_arrived=datetime.datetime.now().strftime('%H:%M:%S'
                      ), parkingLot=parkingLot)
    session.save()
    return render(request, 'parking/system.html',
                  {'parkingLot': parkingLot})
