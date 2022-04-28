from django.db import models
from datetime import datetime
from django.db.models.signals import post_save
 
 
class Rental(models.Model):
   name = models.CharField(max_length=200, unique=True)
 
   def __str__(self):
       return self.name
 
 
class Reservation(models.Model):
   rental = models.ForeignKey(
       Rental, on_delete=models.CASCADE, null=True, blank=True)
   checkin = models.DateField()
   checkout = models.DateField()
   previous_reservation = models.CharField(max_length=10, null=True, blank=True)
 
   def __str__(self):
       return self.rental.name
 
   @property
   def previous_reservation_id(self):
       rental = self.rental
       previous_reservation = Reservation.objects.filter(
           rental=rental.id, id__lte=self.id).order_by('id').exclude(id=self.id).last()
       if previous_reservation:
           return previous_reservation
       return ""
 
 
def reservation_post_save(sender, instance, created, *args, **kwargs):
   if created:
       rental = instance.rental
       previous_reservation = Reservation.objects.filter(
           rental=rental.id, id__lte=instance.id).order_by('id').exclude(id=instance.id).last()
       if previous_reservation:
           instance.previous_reservation = str(previous_reservation.id)
           instance.save()
       else:
           instance.previous_reservation = "-"
           instance.save()
 
 
post_save.connect(reservation_post_save, sender=Reservation)
 
 
class Previous_reservation(models.Model):
   pre_rental = models.ForeignKey(
       Rental, on_delete=models.CASCADE, null=True, blank=True, related_name='pre_rental')
   pre_reservation = models.ForeignKey(
       Reservation, on_delete=models.CASCADE, null=True, blank=True, related_name='pre_reservation')
 
   def __str__(self):
       return self.pre_rental.name
 
 

