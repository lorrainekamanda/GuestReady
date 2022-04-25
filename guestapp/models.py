from django.db import models
from datetime import datetime

class Rental(models.Model):
   name = models.CharField(max_length = 200,unique = True)

   def __str__(self):
       return self.name


