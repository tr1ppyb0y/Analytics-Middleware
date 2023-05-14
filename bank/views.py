from django.shortcuts import render
from .forms import Payment
from .models import Customer
from django.db import transaction
from django.db.models import F
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
# Create your views here.


def process_payment(request):
    if request.method == 'POST':
        form = Payment(request.POST)
        if form.is_valid():
            payor = form.cleaned_data['payor']
            payee = form.cleaned_data['payee']
            amount = form.cleaned_data['amount']

        with transaction.atomic():
            Customer.objects.filter(name=payor).update(balance=F('balance') - amount)
            Customer.objects.filter(name=payee).update(balance=F('balance') + amount)
        
        return HttpResponseRedirect('/')
    else:
        form = Payment()
    
    return TemplateResponse(request, 'index.html', {'form': form})