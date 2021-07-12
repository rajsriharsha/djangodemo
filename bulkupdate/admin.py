from django.contrib import admin

# Register your models here.

from .models import Todo, Todo_Child

# Register your models here.
# class ParentAdmin(admin.ModelAdmin):
#     model = Parent

admin.site.register(Todo)
admin.site.register(Todo_Child)
