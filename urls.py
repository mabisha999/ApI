"""
URL configuration for back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import geeks_home,geeks_page1,geeks_page2,Api3,Api4,Api5,Gallery
urlpatterns = [
    path('',geeks_home),
    path('admin/', admin.site.urls),
    path('page1',geeks_page1,name="page1"),
    path('page2',geeks_page2,name="page2"),
    path('Api3',Api3,name="Api3"),
    path('Api4',Api4,name="Api4"),
    path('Api5',Api5,name="Api5"),
    path('Gallery',Gallery,name="Gallery")
]
