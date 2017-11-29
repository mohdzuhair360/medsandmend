
from django.conf.urls import include, url
from django.contrib import admin
from homepage import views


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^index.html$', views.index),
    url(r'^search/', include ('homepage.urls')),
   # url(r'^homepage/medicine/', include ('homepage.urlmeds')),
    #url(r'^homepage/supplement/', include ('homepage.urlsupp')),

]
