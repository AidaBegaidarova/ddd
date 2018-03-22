"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
'''
urlpatterns = [
    path('admin/', admin.site.urls),
]
'''

from django.conf.urls import url
from qa import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.test, name='test'),
    url(r'^login/', views.test, name='login'),
    url(r'^signup/', views.test, name='signup'),
    url(r'^question/(\d+)/', views.test, name='question'),
    url(r'^ask/', views.test, name='ask'),
    url(r'^popular/', views.test, name='popular'),
    url(r'^new/', views.test, name='new'),
]