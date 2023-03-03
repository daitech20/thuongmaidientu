from django.urls import include, path
from apps.profiles.api.api_views import AddressCreate, AddressList, \
    AddressUpdate, WardsUpdate, WardsList, DistrictsList, DistrictsUpdate, \
    ProvincesUpdate, ProvincesList



urlpatterns = [
    path('address-create/', AddressCreate.as_view()),
    path('address-list/', AddressList.as_view()),
    path('address/<int:id>/', AddressUpdate.as_view()),
    path('wards/<str:code>/', WardsUpdate.as_view()),
    path('wards-list/<str:district_code>/', WardsList.as_view()),
    path('districts/<str:code>/', DistrictsUpdate.as_view()),
    path('districts-list/<str:province_code>/', DistrictsList.as_view()),
    path('provinces/<str:code>/', ProvincesUpdate.as_view()),
    path('provinces-list/', ProvincesList.as_view()),
]