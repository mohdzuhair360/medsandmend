
from django.conf.urls import url
from . import views


app_name = 'navigation'

urlpatterns = [

    url(r'^$', views.result, name = 'result'),
    #url(r'^index.html', include('medsandmend.urls')),
    url(r'^index.html$', views.index, name='index'),
    url(r'^about.html', views.about, name='about'),
    url(r'^contact.html', views.contact, name='contact'),
    url(r'^noproduct.html', views.noproduct, name='noproduct'),


]
