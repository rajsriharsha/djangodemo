from django.contrib import admin
from countrydropdown.models import *
# Register your models here.
# class ParentAdmin(admin.ModelAdmin):
#     model = Parent

# Start - Changes made by Harsha- Integration Team
admin.site.register(Location)
admin.site.register(CountrySelect)
# End - Changes made by Harsha - Integration Team

# Register your models here.
