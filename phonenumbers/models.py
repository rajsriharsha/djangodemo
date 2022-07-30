from django.db import models


# Create your models here.
class PhoneNumbers(models.Model):
    name = models.CharField(max_length=127)
    phone_numbers = models.TextField()

class CountryCode(models.Model):
    name = models.CharField(max_length=127)
    country_code = models.CharField(max_length=40)
    country_info = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        default=""
    )
    geography_remarks = models.TextField(max_length=1000)

    
    class CountryCode_New(models.Model):
    name = models.CharField(max_length=127)
    country_code = models.CharField(max_length=40)
    country_info = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        default=""
    )
    geography_remarks = models.TextField(max_length=1000)
