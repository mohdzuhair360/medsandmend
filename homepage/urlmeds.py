from django.conf.urls import include, url
from . import views

app_name = 'medicine'
#app_name1 = 'supplement'
urlpatterns = [

    url(r'^$', views.index_meds, name = 'index'),
    url(r'^(?P<medicine_id>[0-9]+)/$', views.detail_medicine, name = 'details_meds'),
    #url(r'^(?P<supplement_id>[0-9]+)/$', views.detail_supplement, name = 'detail_supp'),

]