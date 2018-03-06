"""thenewsroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from content_management_system import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home,name='home'),
    url(r'^home/', include('content_management_system.urls'),),
    url(r'^category/', include('content_management_system.urls'),),
    url(r'^content/', include('content_management_system.urls'), ),
    url(r'^about_us$', views.about_us, name='about_us'),
    url(r'^contact_us$', views.contact_us, name='contact_us'),
    url(r'^copyright$', views.copright, name='copright'),
    url(r'^disclaimer$', views.disclaimer, name='disclaimer'),
    url(r'^tinymce/', include('tinymce.urls')),
]
