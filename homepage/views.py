from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PageSource, Description, SearchItem
from .search import guardian
from django.template import Context, loader
from . import templates
from django.http import Http404
from bs4 import BeautifulSoup as soup
import requests
import csv
from datetime import datetime


def index (request):
    SearchItem.objects.all().delete()
    page = PageSource.objects.all()
    return render(request, 'index.html', {'page' : page})

def result (request):
    search_input = request.POST.get('userkeyword', None)
    print(search_input)
    userkeyword = search_input
    first_url = 'https://guardian.com.my/index.php/'
    a_second_url = 'pbrand/'
    a_third_url = '.html'
    a_concat_url = first_url + a_second_url + userkeyword + a_third_url
    a_my_url = a_concat_url
    scrapGuardianResult = guardian.guardianScrapEngine()
    scrapGuardianResult.scrapIt(a_my_url)
    page = PageSource.objects.all()
    return render(request, 'search.html', {'item' : page, 'userkeyword' : userkeyword})



#def index_meds (request):
 #   all_medicine = Medicine.objects.all()
    #template = loader.get_template('homepage/index1.html')
    #context = {'all_medicine' : all_medicine,}
  #  return render(request, 'homepage/index_meds.html', context)
    #html = ''
    #or medicine in all_medicine:
    #    url = '/homepage/'+ str(medicine.id) + '/'
    #    html += '<a href = "'+ url +'">' + str(medicine.meds_name) + '</a><br>'
    #return HttpResponse(html)
    #return render(request, 'index.html')

#def index_supp (request):
 #   all_supplement = Supplement.objects.all()
    #template = loader.get_template('homepage/index1.html')
#    context = {'all_supplement' : all_supplement,}
  #  return render(request, 'homepage/index_supp.html', context)

#def detail_medicine (request, medicine_id):
  #  medicine = get_object_or_404(Medicine, pk=medicine_id)
 #   return render(request, 'homepage/details_meds.html', {'medicine' : medicine})

    #return HttpResponse("<h1>This is medicine : " + str(medicine_id) + "</h2>")
#def detail_supplement (request, supplement_id):
 #   supplement = get_object_or_404(Supplement, pk=supplement_id)
  #  return render(request, 'homepage/details_supp.html', {'supplement' : supplement})

