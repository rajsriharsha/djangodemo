from django.db import models

# Create your models here.
# Chaitanya from Dev team commiting changes
class Location(models.Model):
    city = models.CharField(max_length=127, null=True, blank=True)
    state = models.CharField(max_length=127, null=True, blank=True)
    country = models.CharField(max_length=127, null=True, blank=True)
    latitude = models.CharField(
        max_length=100, null=True, blank=True
    )
    longitude = models.CharField(
        max_length=100, null=True, blank=True
    )
    geo_attribute = models.CharField(
        max_length=200, null=True, blank=True
    )
    def __str__(self) -> str:
        return f"{self.city}, {self.state}, {self.country}"


class CountrySelect(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.name + self.location.city
