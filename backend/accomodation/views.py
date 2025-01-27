from accomodation.models import Hotel, Hostel, Appartment, AppartHotel
from accomodation.serializers import HotelSerializer, HostelSerializer, AppartmentSerializer, AppartHotelSerializer
from rest_framework import permissions, viewsets



class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]



class HostelViewSet(viewsets.ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [permissions.IsAuthenticated]


class AppartmentViewSet(viewsets.ModelViewSet):
    queryset = Appartment.objects.all()
    serializer_class = AppartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class AppartHotelViewSet(viewsets.ModelViewSet):
    queryset = AppartHotel.objects.all()
    serializer_class = AppartHotelSerializer
    permission_classes = [permissions.IsAuthenticated]





