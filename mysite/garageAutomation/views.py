from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404

from .models import Account, PaymentMethod, Vehicle, ParkingSession
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    account_list = Account.objects.order_by('pk')
    context = {'account_list': account_list}
    return render(request, 'garageAutomation/index.html', context)

@login_required
def home(request):
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
        return render(request, 'garageAutomation/home.html', context) #context is what gets passed to the rendered HTML page
    else:
        account = Account.objects.get(user = request.user)
        context = {
            'account' : account,
            'payment_methods' : PaymentMethod.objects.filter(account=account.account_id),
            'vehicles' : Vehicle.objects.filter(account=account.account_id),
            'parking_sessions' : ParkingSession.objects.filter(account = account)
        } 
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










