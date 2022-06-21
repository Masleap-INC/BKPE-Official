from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from vendor.models import  VendorProfile

# Vendor Profile Serializer
class VendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = ('id', 'user', 'name', 'address', 'city', 'state', 'zipcode', 'country', 'phone', 'email')   #, 'website'

