from django.db import transaction
from django.db.models import F
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from .forms import Payment
from .models import Customer


class ProcessPayment(FormView):
    model = Customer
    template_name = 'index.html'
    form_class = Payment

    def form_valid(self, form):
        payor = form.cleaned_data['payor']
        payee = form.cleaned_data['payee']
        amount = form.cleaned_data['amount']

        with transaction.atomic():
            Customer.objects.filter(name=payor).update(balance=F('balance') - amount)
            Customer.objects.filter(name=payee).update(balance=F('balance') + amount)
        
        return HttpResponseRedirect('/')
