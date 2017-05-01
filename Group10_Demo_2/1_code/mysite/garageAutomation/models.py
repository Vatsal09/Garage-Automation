from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
# from django_enumfield import enum

class PaymentMethod(models.Model): 
    #account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    type = models.CharField(max_length=6)
    card_number = models.CharField(max_length=16)
    exp = models.CharField(max_length=5) # --/--
    cvv = models.CharField(max_length=3)
    country = models.CharField(max_length=30)
    zip = models.CharField(max_length=5)

    def getLastFour(self): #prints last 4 digits of card number for Payment and Payment Details
        return self.card_number[-4:]
 
    def __str__(self):
        return str(self.getLastFour())
    
    def printType(self): 
        if (self.type == "Debit"):
            return "Debit "
        else: 
            return self.type

    #TODO: 
        #def charge card - will be part of exit user case

class Account(models.Model): #account for each user
    account_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    paymentmethods = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE) 
    def __str__(self):
        return str(self.account_id) + ": " + self.first_name

    def haveCard(self,c_num): #have card in database; a payment method can only exist on one account (it is used to determine which account to add a vehicle to)
        if len(PaymentMethod.objects.filter(card_number=c_num)) > 0 : 
            return True
        else:
            return False

    def addCard(self, type, card_number, exp, cvv, country, zip): #add card to db with account field set to current account
        if self.haveCard(card_number) == False:
            newCard = PaymentMethod()
            newCard.account = self
            newCard.type = type
            newCard.card_number = card_number
            newCard.exp = exp
            newCard.cvv = cvv
            newCard.country = country
            newCard.zip = zip
            newCard.save()
            self.paymentmethod_set.add(newCard)

    def removeCard(self,recieved_card_number,recieved_exp): #remove card from db
        card = PaymentMethod.objects.filter(account=self.account_id, card_number=recieved_card_number, exp=recieved_exp)
        card.delete()

    def printPhoneNumber(self): 
        return "(" + self.phone_number[0:3] + ") " + self.phone_number[3:6] + "-" + self.phone_number[6:]
    
    def removeVehicle(self,recieved_vehicle_pk,recieved_license_plate):
        vehicle = Vehicle.objects.get(account=self.account_id,pk=recieved_vehicle_pk, license_plate=recieved_license_plate)
        vehicle.delete()

class Vehicle(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    license_plate = models.CharField(max_length=10, unique=True) #license_plate can only be registered to one account
    make = models.CharField(max_length = 10)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.license_plate

class ParkingSession(models.Model): 
    account = models.ForeignKey(Account, on_delete=None) #Manager should still have access to all prior sessions, even if account deleted
    paymentMethod = models.ForeignKey(PaymentMethod, on_delete=None)
    vehicle = models.ForeignKey(Vehicle, on_delete=None)

    cost = models.PositiveIntegerField()
    
    enter_time = models.DateTimeField(default = timezone.now) 
    duration = models.PositiveIntegerField(default=0)
    
    location = models.CharField(max_length=30)

    def __str__(self):
        return str(self.account.account_id)
