from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Parking_Lot, Spot

# Create your views here.

def index(request):
	return render(request, 'parking/index.html')

def add_lot(request):
	return HttpResponse("<h1> add_lot </h1>") 

def delete_lot(request):
	return HttpResponse("<h1> delete_lot </h1>") 

def detail(request):
	return HttpResponse("<h1> detail </h1>") 

def add_spot(request):
	return HttpResponse("<h1> add_spot </h1>") 

def delete_spot(request):
	return HttpResponse("<h1> delete_spot </h1>") 

def register_manager(request):
	return HttpResponse("<h1> register manager </h1>")

def login_manager(request):
	return HttpResponse("<h1> login manager </h1>")

def logout_manager(request):
	return HttpResponse("<h1> logout manager </h1>")