from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from .models import Account, PaymentMethod, Vehicle

def index(request):
    account_list = Account.objects.order_by('account_id')
    context = {'account_list': account_list}
    return render(request, 'garageAutomation/index.html', context)

def home(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST.get('account_id'))
        print("*"*50)
        
        try:
            context = {
                'account' : Account.objects.get(pk=request.POST.get('account_id')),
                'payment_methods' : PaymentMethod.objects.filter(account = 1),
                # 'vehicles' : Vehicle.objects.get(account = 1),
            }
        except Account.DoesNotExist:
            raise Http404("Account does not exist")
        return render(request, 'garageAutomation/home.html', context)
    else:
        return redirect('/')
