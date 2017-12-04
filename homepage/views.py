from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PageSource, Description, SearchItem
from .search import guardian, guardianDescription
from django.template import Context, loader
from . import templates
from django.http import Http404
from bs4 import BeautifulSoup as soup
import requests
import csv
from datetime import datetime


def index (request):
    SearchItem.objects.all().delete()
    page = SearchItem.objects.all()
    return render(request, 'index.html', {'page' : page})

def result (request):
    SearchItem.objects.all().delete()
    product_input = request.POST.get('userkeyword', None)
    allergy_input = request.POST.get('allergyinput', None)
    userkeyword = product_input
    userallergy = allergy_input
    first_url = 'https://guardian.com.my/index.php/'
    a_second_url = 'pbrand/'
    a_third_url = '.html'
    a_concat_url = first_url + a_second_url + userkeyword + a_third_url
    a_my_url = a_concat_url
    scrapGuardianResult = guardian.guardianScrapEngine()
    scrapGuardianResult.scrapIt(a_my_url, userallergy)
    page = PageSource.objects.all()
    return render(request, 'search.html', {'item': page, 'userkeyword': userkeyword})


