
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
   
	url(r'^', views.BlogIndex.as_view(), name = "index"),
	 url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
	
]
