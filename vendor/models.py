from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# # Vendor Model
# class Vendor(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     phone = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     website = models.CharField(max_length=100)
    

#     def __str__(self):
#         return self.name

# Vendor Profile model
class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    #zipcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # website = models.CharField(max_length=100)
    # vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
