from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404

from .models import Account, PaymentMethod, Vehicle

def index(request):
    account_list = Account.objects.order_by('account_id')
    context = {'account_list': account_list}
    return render(request, 'garageAutomation/index.html', context)

def home(request):
    if request.method == "POST":     
        try:
            recievedAccount = Account.objects.get(pk=request.POST.get('account_id'))
            
            # add card
            if request.POST.get('addCard'):
                recievedAccount.addCard(request.POST.get('type'), request.POST.get('card_number'), request.POST.get('exp'), request.POST.get('cvv'), request.POST.get('country'), request.POST.get('zip'))

            # delete card
            if request.POST.get('removeCard'):     
                recievedAccount.removeCard(request.POST.get('card_number'), request.POST.get('exp'))
            
            #remove Vehicle
            if request.POST.get('removeVehicle'):     
                recievedAccount.removeVehicle(request.POST.get('vehicle_pk'),request.POST.get('license_plate'))

            # render home
            context = {
                'account' : recievedAccount,
                'payment_methods' : PaymentMethod.objects.filter(account=recievedAccount.account_id),
                'vehicles' : Vehicle.objects.filter(account=recievedAccount.account_id),
            }
        except Account.DoesNotExist:
            raise Http404("Account does not exist")
        return render(request, 'garageAutomation/home.html', context)
    else:
        return redirect('garageAutomation/')