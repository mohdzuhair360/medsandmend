from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PageSource, Description, SearchItem
from .search import guardian, googleMaps
from django.template import Context, loader
from . import templates
from django.http import Http404
from bs4 import BeautifulSoup as soup
import requests
import csv
from datetime import datetime
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys


def index (request):
    SearchItem.objects.all().delete()
    page = SearchItem.objects.all()
    return render(request, 'index.html', {'page' : page})
    #return render(request, 'mapsTest.html', {'page' : page})
    #return render(request, 'mapsTestSearch.html', {'page': page})
    #return render(request, 'mapsTestSearch2.html', {'page': page})

def result (request):
    SearchItem.objects.all().delete()
    product_input = request.POST.get('userkeyword', None)
    allergy_input = request.POST.get('userallergy', None)
    maps_input = request.POST.get('userlocation', None)

    userkeyword = product_input
    #if userkeyword == "":
    #    return render(request, 'noproduct.html')
    user_allergy = allergy_input
   # if user_allergy == "":
    #    return render(request, 'index.html')
    #if user_allergy == " ":
    #    return render(request, 'index.html', {'page': page})
    user_location = maps_input
    #if user_location == "":
    #    return render(request, 'resultwithoutlocation.html')
    #if user_location == " ":
    #    return render(request, 'index.html', {'page': page})

    if userkeyword == "" and user_location == "" and user_allergy =="":
        return render(request, 'noinput.html')

    if userkeyword == "" or user_location == "" or user_allergy =="":
        return render(request, 'noinput.html')

    try:
        first_url = 'https://guardian.com.my/index.php/'
        a_second_url = 'pbrand/'
        a_third_url = '.html'
        a_concat_url = first_url + a_second_url + userkeyword + a_third_url
        a_my_url = a_concat_url
        scrapGuardianResult = guardian.guardianScrapEngine()
        resultScrap = scrapGuardianResult.scrapIt(a_my_url, user_allergy, request)
        print("Result Scrap : " + str(resultScrap))

        if resultScrap =="" or str(resultScrap)=="None":
            return render(request, 'noproduct.html')

        scrapGuardianLocation = googleMaps.guardianMapsEngine()
        resultLocation = scrapGuardianLocation.locateIt(user_location)

    except Exception as e:
       print("Wrong input. " + str(e))
       return render(request, 'nolocation.html')

    print ("Result location : " + str(resultLocation))
    print("user keyword = " + userkeyword)

    page = PageSource.objects.all()
    return render(request, 'search.html', {'item': page, 'userkeyword': userkeyword, 'resultLocation': resultLocation})

def about(request):
    return render (request, 'about.html')

def contact(request):
    return render (request, 'contact.html')

def noproduct(request):
    return render (request, 'noproduct.html')



