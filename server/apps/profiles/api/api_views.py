from apps.profiles.api.serializers import AddressCreateSerializer, \
    AddressListSerializer, WardsSerializer, DistrictsSerializer, ProvincesSerializer
from apps.profiles.models import Address, Wards, Districts, Provinces
from rest_framework import permissions
from rest_framework import generics, status


class AddressCreate(generics.CreateAPIView):
    queryset = Address
    serializer_class = AddressCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddressList(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Address.objects.all()
        return Address.objects.filter(profile__user=user)


class AddressUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address
    serializer_class = AddressCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class WardsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wards
    serializer_class = WardsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'code'


class WardsList(generics.ListAPIView):
    queryset = Wards
    serializer_class = WardsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'district_code'

    def get_queryset(self):
        district_code = self.kwargs['district_code']
        return Wards.objects.filter(district_code=district_code)


class DistrictsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Districts
    serializer_class = DistrictsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'code'

class DistrictsList(generics.ListAPIView):
    queryset = Districts
    serializer_class = DistrictsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'province_code'

    def get_queryset(self):
        province_code = self.kwargs['province_code']
        return Districts.objects.filter(province_code=province_code)

class ProvincesUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provinces
    serializer_class = ProvincesSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'code'

class ProvincesList(generics.ListAPIView):
    queryset = Provinces.objects.all()
    serializer_class = ProvincesSerializer
    permission_classes = [permissions.IsAuthenticated]