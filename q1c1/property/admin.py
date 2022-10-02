from django.contrib import admin

from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('building_id', 'property', 'first_name',
                    'last_name', 'email')


admin.site.register(Property, PropertyAdmin)