from django.contrib import admin
from accomodation.models import Hotel, Appartment, Hostel, AppartHotel



admin.site.register(Hotel)
admin.site.register(Hostel)
admin.site.register(Appartment)
admin.site.register(AppartHotel)
