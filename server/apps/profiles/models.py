from django.db import models
from apps.users.models import User


# Create your models here.
class AdministrativeRegions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrative_regions'


class AdministrativeUnits(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    full_name_en = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    short_name_en = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrative_units'


class Provinces(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    full_name_en = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    administrative_unit = models.ForeignKey(AdministrativeUnits, models.DO_NOTHING, blank=True, null=True)
    administrative_region = models.ForeignKey(AdministrativeRegions, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provinces'


class Districts(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    full_name_en = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    province_code = models.ForeignKey('Provinces', models.DO_NOTHING, db_column='province_code', blank=True, null=True)
    administrative_unit = models.ForeignKey(AdministrativeUnits, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'districts'


class Wards(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    full_name_en = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    district_code = models.ForeignKey(Districts, models.DO_NOTHING, db_column='district_code', blank=True, null=True)
    administrative_unit = models.ForeignKey(AdministrativeUnits, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wards'
    
    def __str__(self):
        return f"{self.full_name}, {self.district_code.full_name}, {self.district_code.province_code.full_name}"


class Profile(models.Model):
    avatar = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=10, blank=True)


class Address(models.Model):
    specific = models.CharField(max_length=255)
    ward_code = models.ForeignKey(Wards, on_delete=models.CASCADE, related_name="address_ward_code")
    phone = models.CharField(max_length=10)
    is_default = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="address_profile")
    recipient_first_name = models.CharField(max_length=50)
    recipient_last_name = models.CharField(max_length=50)