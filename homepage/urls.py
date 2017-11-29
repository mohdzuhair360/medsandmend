
from django.conf.urls import url
from . import views


app_name = 'search'

urlpatterns = [

    url(r'^$', views.result, name = 'result'),
   # url(r'^(?P<medicine_id>[0-9]+)/$', views.detail_medicine, name = 'details'),
    #url(r'^(?P<supplement_id>[0-9]+)/$', views.detail_supplement, name = 'details'),

]
