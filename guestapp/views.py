from django.shortcuts import render
from django.views.generic import ListView,View
from .models import Rental,Reservation,Previous_reservation
from django.db.models import Count,OuterRef
from itertools import groupby

class Reservations(View):
   

    def get(self,request):
         values_list_queryset =  Reservation.objects.values_list('id','rental__name','checkin','checkout').annotate(dcount=Count('rental__id'))
      
        

       

         reservations = Reservation.objects.values('id','rental__name','checkin','checkout')
         
         context = {
              
               'values_list_queryset':values_list_queryset,
               'reservations':reservations,
               
         }
        
         return render(self.request,'index.html',context)

        

     


