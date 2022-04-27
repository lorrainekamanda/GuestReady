from django.urls import path
from .views import Reservations

app_name = "guestapp"
urlpatterns = [
    path('',Reservations.as_view(),name = 'home'),

]