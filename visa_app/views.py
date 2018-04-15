from django.shortcuts import render
from .models import Country, VisaChoices
# Create your views here.

def home_page(request):
    number = Country.objects.filter(country_visa='7').count()
    list7 = Country.objects.filter(country_visa='7')
    context = {
        'number': number,
        'list7': list7,
        }
    return render(request, 'visa_app/index.html', context)