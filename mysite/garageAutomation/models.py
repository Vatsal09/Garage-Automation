from django.db import models
# from django_enumfield import enum

# pip install --pre django-enumfield==1.3b2  <-- Does not work, neither does stable
# class Country(enum.Enum):
#     USA = 0
#     UK = 1
#     CANADA = 2
    
#     labels = {
#         USA: 'United States',
#         UK: 'United Kingdom',
#         CANADA: 'Canada',
#     }

# class VehicleMake(enum.Enum):
#     UNKOWN = 0
#     HONDA = 1
#     TOYOTA = 2
#     JEEP = 3
#     NISSAN = 4
#     FERARRI = 5

# class Color(enum.Enum):
#     BLACK = 0
#     RED = 1
#     WHITE = 2
#     SILVER = 3

# class PaymentMethodType(enum.Enum):
#     CREDIT = 0
#     DEBIT = 1

# class ParkingLotName(enum.Enum):
#     NBPL = 0

#     labels = {
#         NBPL: "New Brunswick Parking Lot",
#     }

class Account(models.Model):
    account_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.account_id) + ": " + self.first_name

    def haveCard(self,card_number):
        cards = PaymentMethod.objects.filter(account=self.account_id)
        for card in cards:
            if card.card_number == card_number:
                return True
        return False

    def addCard(self, type, card_number, exp, cvv, country, zip):
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
    
    #foreign key for:
        #payment methods
        #vehicles
        #parking sessions
    
    #TODO:
        # username
        # password
        #def verifyPassword
        #def remove
        #remove vehicle
        #remove paymentMethod

class PaymentMethod(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    # type = enum.EnumField(PaymentMethodType, default=PaymentMethodType.CREDIT)
    type = models.CharField(max_length=6)
    card_number = models.CharField(max_length=16)
    exp = models.CharField(max_length=5) # --/--
    cvv = models.CharField(max_length=3)
    country = models.CharField(max_length=30)
    # country = enum.EnumField(Country,default=Country.USA)
    zip = models.CharField(max_length=5)

    def getLastFour(self):
        return self.card_number[-4:]

    def __str__(self):
        return str(self.account.account_id) + ": " + self.getLastFour()
    
    #TODO: 
        #def remove
        #def charge

class Vehicle(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    license_plate = models.CharField(max_length=10)
    make = models.CharField(max_length = 10)
    color = models.CharField(max_length=10)
    # make = enum.EnumField(VehicleMake, default=VehicleMake.UNKOWN)
    # color = enum.EnumField(Color, default=Color.BLACK)

class ParkingSession(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    paymentMethod = models.ForeignKey(PaymentMethod, on_delete=None)
    vehicle = models.ForeignKey(Vehicle, on_delete=None)

    cost = models.PositiveIntegerField()
    
    #TODO: figure out default values
    # enter_time = models.DateTimeField('enter time') 
    # exit_time = models.DateTimeField('exit time')
    
    # location = enum.EnumField(ParkingLotName, default=ParkingLotName.NBPL)
    location = models.CharField(max_length=30)
