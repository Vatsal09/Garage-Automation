from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    return HttpResponse("<h1><strong> PARKING LOT INDEX PAGE </strong> </h1>")
# Function to check if spot is open 
# Function to check number of spots open