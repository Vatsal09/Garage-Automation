from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import ParkingLotForm, SpotForm, UserForm
from .models import Parking_Lot, Spot
import time
import random
from django.core import serializers
import json

# Create your views here.

def index(request):
	return render(request, 'parking/index.html')
def add_lot(request):
    if not request.user.is_authenticated():
        return render(request, 'parking/login_manager.html')
    
    else:
        form = ParkingLotForm(request.POST or None)
        if form.is_valid():
            parkingLot = form.save(commit=False)
            parkingLot.user = request.user
              
            parkingLot.save()
            return render(request, 'parking/detail.html', {'parkingLot': parkingLot})
        context = {
            "form": form,
        }
        return render(request, 'parking/add_lot.html', context) 

def add_spot(request, parkingLot_id):
    form = SpotForm(request.POST or None)
    parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
    if form.is_valid():
        parkingLots_spots = parkingLot.spot_set.all()
        for s in parkingLots_spots:
            if s.spot_number == form.cleaned_data.get("spot_number"):
                context = {
                    'parkingLot': parkingLot,
                    'form': form,
                    'error_message': 'You already added that spot',
                }
                return render(request, 'parking/add_spot.html', context)
        spot = form.save(commit=False)
        spot.parkingLot = parkingLot
        spot.save()
        return render(request, 'parking/detail.html', {'parkingLot': parkingLot})
    context = {
        'parkingLot': parkingLot,
        'form': form,
    }
    return render(request, 'parking/add_spot.html', context)

def delete_lot(request, parkingLot_id):
    parkingLot = Parking_Lot.objects.get(pk=parkingLot_id)
    parkingLot.delete()
    parkingLots = Parking_Lot.objects.filter(user=request.user)
    return render(request, 'parking/main.html', {'parkingLots': parkingLots})
	 

def detail(request, parkingLot_id):
    if not request.user.is_authenticated():
        return render(request, 'parking/login_manager.html')
    else:
        user = request.user
        parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
        return render(request, 'parking/detail.html', {'parkingLot': parkingLot, 'user': user}) 

 

def delete_spot(request, parkingLot_id, spot_id):
    parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
    spot = Spot.objects.get(pk=spot_id)
    spot.delete()
    return render(request, 'parking/detail.html', {'parkingLot': parkingLot})

def register_manager(request):

    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                parkingLots = Parking_Lot.objects.filter(user=request.user)
                return render(request, 'parking/main.html', {'parkingLots': parkingLots})
    context = {
        "form": form,
    }
    return render(request, 'parking/register_manager.html', context)

def login_manager(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                parkingLots = Parking_Lot.objects.filter(user=request.user)
                # Infinite loop for sensor checker activate
                #render(request, 'parking/update_occupancy')
                return render(request, 'parking/main.html', {'parkingLots': parkingLots})
            else:
                return render(request, 'parking/login_manager.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'parking/login_manager.html', {'error_message': 'Invalid login'})
    return render(request, 'parking/login_manager.html')
	


def logout_manager(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'parking/index.html', context)

def main(request):
    if not request.user.is_authenticated():
        return render(request, 'parking/login_manager.html')
    else:
        parkingLots = Parking_Lot.objects.filter(user=request.user)
        spot_results = Spot.objects.all()
        query = request.GET.get("q")
        if query:
            parkingLots = parkingLots.filter(
                Q(address__icontains=query)                
            ).distinct()
            spot_results = spot_results.filter(
                Q(spot_number__icontains=query) |
                Q(sensor_id__icontains=query)
            ).distinct()
            return render(request, 'parking/main.html', {
                'parkingLots': parkingLots,
                'spots': spot_results,
            })
        else:
            return render(request, 'parking/main.html', {'parkingLots': parkingLots})

def update_occupancy(request, parkingLot_id):
    if not request.user.is_authenticated():
        return render(request, 'parking/login_manager.html')
    else:
        parkingLot = Parking_Lot.objects.get(pk=parkingLot_id)
        parkingLots_spots = parkingLot.spot_set.all()
        for s in parkingLots_spots:
                s.is_occupied = bool(random.getrandbits(1))
                s.save()
        return render(request, 'parking/detail.html', {'parkingLot': parkingLot})
        #return render(request, 'parking/update_occupancy.html')
    # If the inifinite loop is to be activated for checker, uncomment below and uncomment the render request in login_manager(request) view
    # else:
    #     while True:
    #         for s in Spot.objects.all():
    #             s.is_occupied = bool(random.getrandbits(1))
    #             s.save()
    #         time.sleep(10)
    
def disable_spot(request, parkingLot_id, spot_id):
    parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
    spot = Spot.objects.get(pk=spot_id)
    spot.is_disabled = True
    spot.is_occupied = False
    spot.save()
    return render(request, 'parking/detail.html', {'parkingLot': parkingLot})

def enable_spot(request, parkingLot_id, spot_id):
    parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
    spot = Spot.objects.get(pk=spot_id)
    spot.is_disabled = False
    spot.is_occupied = True
    spot.save()
    return render(request, 'parking/detail.html', {'parkingLot': parkingLot})

def map(request, parkingLot_id, level):
    parkingLot = get_object_or_404(Parking_Lot, pk=parkingLot_id)
    parkingLots_spots = parkingLot.spot_set.all()
    num_levels = parkingLot.max_levels
    num_levels = int(num_levels)
    level_1 = int(level)
    last_spot_per_level = []
    last_spot_per_level.append(0)
    temp_num = 0
    for i in range(1, (num_levels+1)):
        for s in parkingLots_spots:
            if int(s.level) == i and int(s.spot_number) > temp_num:
               temp_num = int(s.spot_number)
        last_spot_per_level.append(temp_num)
    # [0/1 100 113 455]
    data_max = last_spot_per_level[level_1]
    data_min = last_spot_per_level[level_1-1]+1
    data_set = []
    # For even
    if data_max%2==0:
        bottom_left = data_min
        top_left = round((float(data_max+data_min)/float(2))-0.5)
        top_left = int(top_left)
        bottom_right = top_left+1
        top_right = data_max
        data_set = [bottom_left, top_left, bottom_right, top_right]

    else:
        bottom_left = data_min
        top_left = ((data_max+data_min)/2)-1
        bottom_right = top_left+1
        top_right = data_max
        data_set = [bottom_left, top_left, bottom_right, top_right]
    # spots_left = []
    # spots_right = []
    # for x in parkingLots_spots :
    #     if x.spot_number >= data_set[0] and x.spot_number <= data_set[1]:
    #         spots_left.append(x)
    #     if x.spot_number >= data_set[2] and x.spot_number <= data_set[3]:
    #         spots_right.append(x) 
    spots_left = Spot.objects.filter(parkingLot = parkingLot_id).filter(spot_number__gte = data_set[0]).filter(spot_number__lte = data_set[1])
    spots_right = Spot.objects.filter(parkingLot = parkingLot_id).filter(spot_number__gte = data_set[2]).filter(spot_number__lte = data_set[3])
    spots = zip(spots_left, spots_right)

    # left= Parking_Lot.objects.filter(pk=parkingLot_id).filter(spot.all().filter(spot_number__lte = data_set[0]).filter(spot_number__lte = data_set[1])
    # right = parkingLots_spots.objects.all().filter(int(spot_number)>= data_set[2]).filter(int(spot_number)<= data_set[3])

    
    # json_data_set = json.dumps(data_set)
    # json_level = json.dumps(level_1)
    # json_serializer = serializers.get_serializer("json")()
    # json_spots = json_serializer.serialize(parkingLot.spot_set.all())
    return render(request, 'parking/map.html', {
        'data_set' : data_set,
        'level' : level,
        'parkingLot': parkingLot,
        'spots' : spots,
        # 'spots1': json_spots, 
        # 'level': json_level,
        # 'data_set': json_data_set,
    })










