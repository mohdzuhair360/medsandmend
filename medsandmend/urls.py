
from django.conf.urls import include, url
from django.contrib import admin
from homepage import views


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^index.html$', views.index, name='index'),
    url(r'^search/', include ('homepage.urls')),
    #url(r'^about.html', views.about, name='about'),
    #url(r'^faq.html', views.faq, name='faq'),
    #url(r'^contact.html', views.contact, name='contact'),

]
