from django.conf.urls import include, url
from . import views

app_name = 'supplement'

urlpatterns = [

    url(r'^$', views.index_supp, name = 'index'),
    url(r'^(?P<supplement_id>[0-9]+)/$', views.detail_supplement, name = 'details_supp'),

]