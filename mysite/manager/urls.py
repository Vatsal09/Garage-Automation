
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.contrib import admin

#from . import views
#import sys
#sys.setrecursionlimit(10000)
app_name="manager"
# /manager/
urlpatterns =[
	url(r'^$', views.index, name='index'), #index page
	url(r'^page2/',include('manager.page2.urls')),
	url(r'^page3/',include('manager.page3.urls')),
	url(r'^admin/', admin.site.urls),

]

urlpatterns += staticfiles_urlpatterns()
