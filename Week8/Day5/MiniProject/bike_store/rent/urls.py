from django.urls import path
from . import views

urlpatten = [
    path('rent/rental/', views.rental_list_view, name = 'rental_list'),
    path('rent/rental/<int:pk>', views.rental_list_view, name = 'rental_list'),
    path('rent/rental/add', views.rental_list_view, name = 'rental_list'),
    path('rent/customer/<int:pk>', views.rental_list_view, name = 'rental_list'),
    path('rent/customer/', views.rental_list_view, name = 'rental_list'),
    path('rent/customer/add', views.rental_list_view, name = 'rental_list'),
    path('rent/vehicle/', views.rental_list_view, name = 'rental_list'),
    path('rent/vehicle/<int:pk>', views.rental_list_view, name = 'rental_list'),
    path('rent/vehicle/add', views.rental_list_view, name = 'rental_list')
]