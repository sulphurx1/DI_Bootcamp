from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    real_cost = models.DecimalField(max_digits = 10, decimal_places=2)
    size = models.ForeignKey('VehicleSize', on_delete=models.CASCADE)

class VehicleType(models.Model):
    name = models.CharField(max_length=100)

class VehicleSize(models.Model):
    name = models.CharField(max_length=100)

class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)

class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits = 10,decimal_places=2)
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey('VehicleSize', on_delete=models.CASCADE)