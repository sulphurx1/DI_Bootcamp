from django.shortcuts import render, get_object_or_404, redirect
from .models import Rental, Customer, Vehicle
from django.contrib import messages
from django.urls import reverse_lazy
from .form import CustomerForm, VehicleForm
from itertools import groupby
from operator import attrgetter


# Create your views here.

# /rent/rental/ - show a list of all rentals, unreturned first, then ordered by date ascending (earliest first)
def rental_list_view(request):
    rental_list = Rental.objects.all()
    context = {'rental_list': rental_list}
    return render(request, 'index.html', context)


# /rent/rental/<pk> - show the information about the given rental:
## customer details
## vehicle details
## rental details (“Returned on: <date>” / “Not yet returned”)
def rental_detail(request, pk):
    rental = get_object_or_404(Rental, pk)
    context = {'rental': rental}
    return render(request, 'index.html', context)

# /rent/rental/add – provide a form to enter a customer ID and a vehicle ID to create a rental.
## If the customer or the vehicle does not exist, show a user-friendly error message.
## If the vehicle is currently being rented, show a relevant error message.
class RentalCreateView():
    model = Rental
    fields = ['customer', 'vehicle']
    sucess_url = reverse_lazy('index')

    def form_valid(self, form):
        customer_id = form.cleaned_data['customer']
        vehicle_id = form.cleaned_data['vehice']

        try:
            customer = Customer.objects.get(id = customer_id)
        
        except Customer.DoesNotExist:
            messages.error(self.request, f'Customer with ID{customer_id} does not exist')
            return super().form_invalid(form)
        
        try:
            vehicle = Vehicle.objects.get(id = vehicle_id)

        except Vehicle.DoesNotExist:
            messages.error(self.request, f'Vehicle with ID{vehicle_id} does not exist')
            return super().form_invalid(form)
        
        if Rental.objects.filter(vehicle=vehicle, return_on = None).exists():
            messages.error(self.request, f'Vehicle with ID {vehicle_id} is currently being rented')
            return super().form_invalid(form)
        
        rental = form.save(commit = False)
        rental.customer = customer
        rental.vehicle = vehicle
        rental.save()

        return super().form_valid(form)
    
# /rent/customer/<pk> - show the customer matching the given ID
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context = {'customer': customer}
    return render(request, 'index.html', context)

# /rent/customer/ - show all customers, in alphabetical order    
def customer_list(request):
    customers = Customer.objects.order_by('name')
    context = {'customers': customers}
    return render(request, 'inddex.html', context)

# /rent/customer/add – provide a form to add a new customer
def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = CustomerForm()
    
    context = {'form': form}
    return render(request, 'index.html', context)

# /rent/vehicle/ - show all vehicles, grouped into their groups (‘bike’ and ‘scooter’)
def vehicle_list(request):
    vehicles = Vehicle.objects.order_by('vehicle_group': 'name')
    vehicle_groups = []
    for key, group in groupby(vehicles, attrgetter('vehicle_group')):
        vehicle_groups.append({
            'name': key,
            'vehicles': list(group)
        })
    context = {'vehicle_groups': vehicle_groups}
    return render(request, 'index.html', context)

# /rent/vehicle/<pk> - show the specific vehicle & also show whether it’s currently being rented
def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    is_rented = vehicle.rented
    context = {'vehicle': vehicle, 'isrented': is_rented}
    return render(request, 'index.html', context)


# /rent/vehicle/add – provide a form to add a new vehicle.
def vehicle_add(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        else:
            form = VehicleForm()
        context = {'form': form}
        return render(request, 'index.html', context)