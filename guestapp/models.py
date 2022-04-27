from django.db import models
from datetime import datetime

class Rental(models.Model):
   name = models.CharField(max_length = 200,unique = True)
   
   def __str__(self):
       return self.name

class Reservation(models.Model):
   id = models.AutoField(primary_key=True)
   rental = models.ForeignKey(Rental,on_delete = models.CASCADE,null = True,blank = True)
   checkin = models.DateField()
   checkout = models.DateField()
   previous_reservation = models.IntegerField(default = 0,null = True,blank=True)

   def __str__(self):
       return self.rental.name

   @property
   def previous_reservation_id(self):
         previous_reservation = Reservation.objects.filter(id = id).order_by('id').exclude(id = self.id).last()
         return previous_reservation

class Previous_reservation(models.Model):
    pre_rental = models.ForeignKey(Rental,on_delete = models.CASCADE,null = True,blank = True,related_name='pre_rental')
    pre_reservation = models.ForeignKey(Reservation,on_delete = models.CASCADE,null = True,blank = True,related_name='pre_reservation')
   
    def __str__(self):
       return self.pre_rental.name



#    @property
#    def previous_reservation_id(self):
#          next_issue = Reservation.objects.filter(id = id).order_by('id').exclude(id = self.id).last()
#          return next_issue
         

#    @property
#    def previous_reservation_id(self):
#         rental = self.rental
#         reservations_id = Reservation.objects.filter_by(rental = rental, id__lte=self.id).exclude(id = self.id).last()
#         if reservations_id != None:
#             return reservation.id
            
#         else:
#             return("-")
     
     

