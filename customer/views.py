from django.shortcuts import render
from .models import Customer
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import CreateCustomerForm, UpdateCustomerForm




class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/allcustomers.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context
    
    


class CustomerCreate(CreateView):
    model = Customer
    form_class = CreateCustomerForm
    template_name = 'customers/create_customer.html'
    success_url = reverse_lazy('customer-list')
       
    
    
    
class CustomerDetailView(DetailView):
    model = Customer
    pk_url_kwarg = 'id'
    template_name = 'customers/customer_detail.html'

    
    
    
class CustomerUpdate(UpdateView):
    model = Customer
    template_name = 'customers/edit_customer.html'
    pk_url_kwarg = 'id'
    form_class = UpdateCustomerForm
    success_url = reverse_lazy('customer-list')