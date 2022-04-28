from django.shortcuts import render
from django.views.generic import ListView,View
from .models import Rental,Reservation
from django.db.models import Count,OuterRef
from itertools import groupby

class Reservations(View):
   

    def get(self,request):
       
         rental =  Rental.objects.all()
         queryset = Reservation.objects.values('id','rental__name','checkin','checkout','previous_reservation')
        
         context = {
              
               'queryset':queryset,
               'rental':rental,
             
         }
        
         return render(self.request,'index.html',context)

        

     


