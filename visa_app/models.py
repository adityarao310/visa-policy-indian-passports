from django.db import models

# Create your models here.

class Country(models.Model):
    country_name = models.CharField(max_length=200)
    country_visa_choices = (
        ('1', 'No visa required'),
        ('2', 'Visa on arrival'),
        ('3', 'No visa required, if Schengen visa'),
        ('4', 'No visa required, if UK visa'),
        ('5', 'No visa required, if US visa'),
        ('6', 'Simple online application'),
        ('7', 'Fuck all visa process'),
    )
    country_visa = models.CharField(
        max_length=2,
        choices=country_visa_choices,
        default=7,
    )


