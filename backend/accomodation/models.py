from django.db import models

# Create your models here.

ACCOMODATION_TYPES = (("HOTEL","hotel"), ("HOSTEL","hostel"), ("APPARTMENT","appartment"), ("APPARTHOTEL","apparthotel"))

class Accomodation(models.Model):

    name = models.CharField(max_length=256, default="default")
    address = models.CharField(max_length=256, default="default")
    phone = models.CharField(max_length=256, default="default")
    email = models.EmailField(default="default")
    type = models.CharField(max_length=256,
                  choices=ACCOMODATION_TYPES,
                  default="HOTEL")
    

class Hotel(Accomodation):
    pass

class Hostel(Accomodation):
    pass

class Appartment(Accomodation):
    pass

class AppartHotel(Accomodation):
    pass