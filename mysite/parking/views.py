from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import ParkingLotForm, SpotForm, UserForm
from .models import Parking_Lot, Spot

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
        spot.lot = parkingLot
        
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