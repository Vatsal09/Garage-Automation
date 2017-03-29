from django.contrib import admin
from .models import Parking_Lot, Spot, Session
from garageAutomation.models import Account, Vehicle

# Register your models here.
admin.site.register(Parking_Lot)
admin.site.register(Spot)
admin.site.register(Session)
admin.site.register(Account)
admin.site.register(Vehicle)
