from rest_framework import serializers
from  apps.profiles.models import Profile, Address, Wards, Districts, Provinces



class ProvincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provinces
        fields = '__all__'


class DistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = '__all__'


class WardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wards
        fields = '__all__'


class AddressCreateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Address
        fields = ['specific', 'phone', 'ward_code', 'recipient_last_name', 'recipient_first_name']

    def create(self, validated_data):
        user = self.context['request'].user
        profile = Profile.objects.get(user=user)
        
        address = Address.objects.create(
            specific=validated_data['specific'],
            phone=validated_data['phone'],
            ward_code=validated_data['ward_code'],
            profile=profile,
            recipient_first_name=validated_data['recipient_first_name'],
            recipient_last_name=validated_data['recipient_last_name'],
        )
        address.save()

        return address


class AddressListSerializer(serializers.ModelSerializer):
    info_address = serializers.SerializerMethodField('get_alternate_name')

    class Meta:
        model = Address
        fields = ['id','specific', 'ward_code', 'phone', 'is_default', 'recipient_first_name', 'recipient_last_name', 'info_address']
    
    def get_alternate_name(self, obj):
        return f"{ obj.specific }  { obj.ward_code.full_name}, {obj.ward_code.district_code.full_name}, {obj.ward_code.district_code.province_code.full_name}"