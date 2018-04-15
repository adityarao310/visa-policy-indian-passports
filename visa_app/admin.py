from django.contrib import admin
from .models import Country, VisaChoices

# Register your models here.

admin.site.register(Country)
admin.site.register(VisaChoices)
