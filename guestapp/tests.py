from django.test import TestCase

from .models import Rental,Reservation

# Create your tests here.
# Set up method
"""
testing the instation of the Rntal Class
"""
def setUp(self):
    self.new_rental= Rental(name= 'rental_1')
    self.new_reservation = Reservation(checkin = '2022-02-20',checkout='2022-02-10',rental__name = 'rental_1' )
    self.new_rental.save()
    self.new_reservation.save()
    

def test_instance(self):
    self.assertTrue(isinstance(self.new_reservation,Reservation))

def test_save_reservation(self):
    self.new_reservations.save_reservation()
    reservations = Reservation.objects.all()
    self.assertTrue(len(reservations) > 0)

# def tearDown(self):
#     Image.objects.all().delete()
#     User.objects.all().delete()
#     Profile.objects.all().delete()

# def test_delete_image(self):
#     self.new_image.save_images()
#     images = Image.objects.all()
#     self.new_image.delete_images()
#     self.assertTrue(len(images) == 0)