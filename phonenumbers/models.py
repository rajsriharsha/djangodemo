from django.db import models


# Create your models here.
class PhoneNumbers(models.Model):
    name = models.CharField(max_length=127)
    phone_numbers = models.TextField()

class CountryCode(models.Model):
    name = models.CharField(max_length=127)
    country_code = models.CharField(max_length=25)
    country_info = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        default=""
    )
