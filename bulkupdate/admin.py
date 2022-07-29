from django.contrib import admin

# Register your models here.

from .models import Todo, Todo_Child, Type, Status, Region

# Register your models here.
# class ParentAdmin(admin.ModelAdmin):
#     model = Parent

admin.site.register(Todo)
admin.site.register(Todo_Child)
admin.site.register(Status)
admin.site.register(Region)

