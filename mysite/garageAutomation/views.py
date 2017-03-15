from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404

from .models import Account, PaymentMethod, Vehicle

def index(request):
    account_list = Account.objects.order_by('account_id')
    context = {'account_list': account_list}
    return render(request, 'garageAutomation/index.html', context)

def home(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print("*"*50)       
        try:
            account = Account.objects.get(pk=request.POST.get('account_id'))
            if request.POST.get('addCard'):
                account.addCard(request.POST.get('type'), request.POST.get('card_number'), request.POST.get('exp'), request.POST.get('cvv'), request.POST.get('country'), request.POST.get('zip'))
                       
            context = {
                'account' : account,
                'payment_methods' : PaymentMethod.objects.filter(account = 1),
                # 'vehicles' : Vehicle.objects.get(account = 1),
            }
        except Account.DoesNotExist:
            raise Http404("Account does not exist")
        return render(request, 'garageAutomation/home.html', context)
    else:
        return redirect('/')
