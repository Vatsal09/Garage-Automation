from django.conf.urls import url, include
from django.contrib import admin
from . import views
#import sys
#sys.setrecursionlimit(10000)
urlpatterns=[
	url(r'^$',views.index,name="index"), #index page
	#url(r'^manager.page2.page3/',include('manager.views.index')),
	url(r'^admin/',admin.site.urls),
]
