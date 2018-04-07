from django.shortcuts import render
from .models import Country
# Create your views here.

def home_page(request):
    list1 = Country.objects.filter(country_visa=1)
    list2 = Country.objects.filter(country_visa=2)
    list3 = Country.objects.filter(country_visa=3)
    list4 = Country.objects.filter(country_visa=4)
    list5 = Country.objects.filter(country_visa=5)
    list6 = Country.objects.filter(country_visa=6)
    list7 = Country.objects.filter(country_visa=7)
    return render(request, 'visa_app/index.html', {'list1':list1, 'list2':list2, 'list3':list3, 'list4':list4, 'list5':list5, 'list6':list6, 'list7':list7,})