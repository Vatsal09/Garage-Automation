
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

#from . import views
#import sys
#sys.setrecursionlimit(10000)
app_name="manager"
# /manager/
urlpatterns =[
	url(r'^$', views.index, name='index'), #index page
	
	
#	url(r'^main/$', views.main, name='main'),



]

urlpatterns += staticfiles_urlpatterns()
