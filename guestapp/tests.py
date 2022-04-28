from django.test import TestCase
from django.db.models import signals
from .models import Rental,Reservation,reservation_post_save


"""
testing the instation of the Rental and Reservation Class
"""

class ReservationTestClass(TestCase):
    def setUp(self):
        self.new_rental= Rental(name= 'rental_1')
        self.new_rental.save()
        self.new_reservation = Reservation(id = 1,checkin = '2022-02-20',checkout='2022-02-10',rental=self.new_rental)
        self.new_reservation.save()
        

    def test_connection(self):
        result = signals.post_save.connect(reservation_post_save,sender=Reservation)

        self.assertTrue(result == None)
        

    def test_instance(self):
        self.assertTrue(isinstance(self.new_reservation,Reservation))

    def test_save_reservation(self):
        self.new_reservation.save()
        reservations = Reservation.objects.all()
        self.assertTrue(len(reservations) > 0)

    def tearDown(self):
        Rental.objects.all().delete()
        Reservation.objects.all().delete()
       
    def test_delete(self):
        self.new_reservation.save()
        reservation = Reservation.objects.all()
        self.new_reservation.delete()
        self.assertTrue(len(reservation) == 0)