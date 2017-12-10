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

def result (request):
    SearchItem.objects.all().delete()
    product_input = request.POST.get('userkeyword', None)
    allergy_input = request.POST.get('userallergy', None)
    maps_input = request.POST.get('userlocation', None)

    userkeyword = product_input
    user_allergy = allergy_input
    user_location = maps_input

    first_url = 'https://guardian.com.my/index.php/'
    a_second_url = 'pbrand/'
    a_third_url = '.html'
    a_concat_url = first_url + a_second_url + userkeyword + a_third_url
    a_my_url = a_concat_url
    scrapGuardianResult = guardian.guardianScrapEngine()
    scrapGuardianResult.scrapIt(a_my_url, user_allergy)
    scrapGuardianLocation = googleMaps.guardianMapsEngine()
    resultLocation = scrapGuardianLocation.locateIt(user_location)

    #driver = webdriver.Firefox()
    #driver.get(resultLocation)

    # open tab
   # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

    # Load a page
    #driver.get(resultLocation)
    # Make the tests...

    print ("Result location : " + str(resultLocation))

    page = PageSource.objects.all()
    return render(request, 'search.html', {'item': page, 'userkeyword': userkeyword, 'resultLocation': resultLocation})

def about(request):
    return render (request, 'about.html')

def contact(request):
    return render (request, 'contact.html')

def faq(request):
    return render (request, 'faq.html')


