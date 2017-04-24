from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404

from .models import Account, PaymentMethod, Vehicle, ParkingSession
from parking.models import Parking_Lot, Spot
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    account_list = Account.objects.order_by('pk')
    context = {'account_list': account_list}
    return render(request, 'garageAutomation/index.html', context)

@login_required
def home(request, parkingLot_id, level):
    if request.method == "POST":     
        try:
            recievedAccount = Account.objects.get(user = request.user)
            
            # add card
            if request.POST.get('addCard'):
                recievedAccount.addCard(request.POST.get('type'), request.POST.get('card_number'), request.POST.get('exp'), request.POST.get('cvv'), request.POST.get('country'), request.POST.get('zip'))

            # delete card
            if request.POST.get('removeCard'):
                if len(PaymentMethod.objects.filter(account = recievedAccount.pk)) > 1:
                    recievedAccount.removeCard(request.POST.get('card_number'), request.POST.get('exp'))
            
            #remove Vehicle
            if request.POST.get('removeVehicle'):     
                recievedAccount.removeVehicle(request.POST.get('vehicle_pk'),request.POST.get('license_plate'))
            
            # delete Account
            if request.POST.get('deleteAccount'):    
                recievedAccount.user.delete()

            # update First Name
            if request.POST.get('updateFirstName'):    
                recievedAccount.first_name = request.POST.get('firstName')

            # update Last Name
            if request.POST.get('updateLastName'):    
                recievedAccount.last_name = request.POST.get('lastName')

            # update Phone Number
            if request.POST.get('updatePhoneNumber'):    
                recievedAccount.phone_number = request.POST.get('phoneNumber')

            # render home
            context = {
                'account' : recievedAccount,
                'payment_methods' : PaymentMethod.objects.filter(account=recievedAccount.account_id),
                'vehicles' : Vehicle.objects.filter(account=recievedAccount.account_id),
                'parking_sessions' : ParkingSession.objects.filter(account = recievedAccount)
            } 
        except Account.DoesNotExist:
            raise Http404("Account does not exist")
    else:
        account = Account.objects.get(user = request.user)
        context = {
            'account' : account,
            'payment_methods' : PaymentMethod.objects.filter(account=account.account_id),
            'vehicles' : Vehicle.objects.filter(account=account.account_id),
            'parking_sessions' : ParkingSession.objects.filter(account = account)
        } 

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

    spots_left = Spot.objects.filter(parkingLot=parkingLot_id).filter(spot_number__gte=data_set[0]).filter(spot_number__lte=data_set[1])
    spots_right = Spot.objects.filter(parkingLot=parkingLot_id).filter(spot_number__gte=data_set[2]).filter(spot_number__lte=data_set[3])
    spots = zip(spots_left, spots_right)

    context['data_set'] = data_set
    context['level'] = int(level)
    context['prev_level'] = int(prev_level)
    context['next_level'] = int(next_level)
    context['num_levels'] = num_levels
    context['parkingLot'] = parkingLot
    context['spots'] = spots

    return render(request, 'garageAutomation/home.html', context) 

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(request.POST)
            form = form.save()
            account = Account()          
            account.user = form 
            account.first_name = str(request.POST.get('first_name'))
            account.last_name = str(request.POST.get('last_name'))
            account.phone_number = str(request.POST.get('phone_number'))
            account.save()
            account = Account.objects.get(user = form)
            account.addCard(request.POST.get('type'), request.POST.get('card_number'), request.POST.get('exp'), request.POST.get('cvv'), request.POST.get('country'), request.POST.get('zip'))
            return redirect('/garageAutomation/login')
    return render(request, 'garageAutomation/register.html', {'form':form})










