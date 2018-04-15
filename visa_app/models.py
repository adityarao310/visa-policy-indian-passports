from django.db import models

# Create your models here.

class VisaChoices(models.Model):
    visa_desc = models.CharField(max_length=200)
    def __str__(self):
        return self.visa_desc

class Country(models.Model):
    country_name = models.CharField(max_length=200)
   
    country_visa = models.ManyToManyField(VisaChoices)

    country_image = models.ImageField(upload_to='media', default='../default.jpg')

    def __str__(self):
        return self.country_name


