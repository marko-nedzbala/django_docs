from django.contrib import admin

from .models import (
    Person, Album, Musician, Manufacturer, Car,
    Group, Membership
)

# Register your models here.
# @admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'year_in_school', 'my_type']

admin.site.register(Person, PersonAdmin)
admin.site.register(Album)
admin.site.register(Musician)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['man_ref']

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['man_name']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Group._meta.get_fields()]
    list_display = ['name']



















