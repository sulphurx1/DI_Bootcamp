from ...models import *
from django.core.management.base import BaseCommand
from faker import Faker

class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        for i in range(5):
            customer = Customer(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                email = fake.email(),
                phone_number = fake.phone_number(),
                address = fake.street_address(),
                city = fake.city(),
                country = fake.country()
            )
            customer.save()

        for i in range(5):
            vehicle_type = VehicleType(
                name = fake.word()
            )
            vehicle_type.save()

        for i in range(5):
            vehicle_size = VehicleSize(
                name = fake.word()
            )
            vehicle_size.save()

        for i in range(5):
            vehicle = Vehicle(
                vehicle_type=VehicleType.objects.order_by('?').first(),
                date_created = fake.date_this_century(),
                real_cost=fake.pydecimal(left_digits = 5, right_digits = 2, positive = True),
                size = VehicleSize.objects.order_by('?').first()
            )
            vehicle.save()

            self.stdout.write(self.style.SUCCESS('Successfully populated with fake data'))