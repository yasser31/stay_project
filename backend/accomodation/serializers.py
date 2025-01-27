from accomodation.models import Hotel, Hostel, Appartment, AppartHotel
from rest_framework import serializers




class HotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ["url", "name", "address", "phone", "email", "type"]


class HostelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hostel
        fields = ["url", "name", "address", "phone", "email", "type"]

class AppartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appartment
        fields = ["url", "name", "address", "phone", "email", "type"]

class AppartHotelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppartHotel
        fields = ["url", "name", "address", "phone", "email", "type"]