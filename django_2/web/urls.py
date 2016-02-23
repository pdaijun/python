"""django_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from web.views import Add,Delet,Updet,Get,asset_list
urlpatterns = [
              
    #url(r'^add/(?P<name>\w*)/$',Add),
        #r'^admin/', include(admin.site.urls)),
    #url(r'^delet/(?P<id>\d*)/$',Delet),
    #url(r'^updet/(?P<id>\d*)/(?P<hostname>\w*)/$',Updet),
    #url(r'^get/(?P<name>\w*)/$',Get),
    url(r'^get/',asset_list)
]
