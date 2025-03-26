from django.contrib import admin

from .models import (
    Person, Album, Musician, Manufacturer, Car,
    Group, Membership, Blog, Author, Entry, Dog,
    Contact
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

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ['person', 'group', 'date_joined', 'invite_reason']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline']

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email']

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Entry._meta.get_fields() if not field.many_to_many]

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['name', 'data']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.get_fields()]












