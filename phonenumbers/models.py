from django.db import models


# Create your models here.
class PhoneNumbers(models.Model):
    name = models.CharField(max_length=127)
    phone_numbers = models.TextField()

class CountryCode(models.Model):
    name = models.CharField(max_length=127)
    country_code = models.CharField(max_length=5)
    remarks = models.TextField(
        default="",
        null=True,
        blank=True
    )
