from django.shortcuts import render
from .models import Device
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from customer.models import Customer
from device.forms import CreateDeviceForm
# Create your views here.


# def devices(request):
#     devices = Device.objects.all()
#     context = {
#         'devices': devices
#     }
#     return render(request,"devices/devices.html", context)


class DeviceListView(ListView):
    model = Device
    template_name = 'devices/devices.html'


    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['devices'] = Device.objects.all()
        return context
    
    
    
    

class DeviceCreateView(CreateView):
    model = Device
    form_class = CreateDeviceForm
    template_name = 'devices/add_device.html'
    success_url = reverse_lazy('device-list')
    
    
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context
    
    
    def form_invalid(self, form):
        # Log the errors if necessary, for debugging
        print(form.errors)
        return super().form_invalid(form)