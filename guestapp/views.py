from django.shortcuts import render
from django.views.generic import ListView,View
from .models import Rental,Reservation,Previous_reservation
from django.db.models import Count,OuterRef
from itertools import groupby

class Reservations(View):
   

    def get(self,request):
         queryset =  Reservation.objects.values('id','rental__name','checkin','checkout')
         rental =  Rental.objects.all()
         reservations = Reservation.objects.values('id','rental__name','checkin','checkout','previous_reservation')
         new_id = Reservation.objects.filter(rental= rental )
         context = {
              
               'queryset':queryset,
               'reservations':reservations,
               'rental':rental,
             
         }
        
         return render(self.request,'index.html',context)

        

     


