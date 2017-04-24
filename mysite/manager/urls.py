
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
#	url(r'^analytics/',include('manager.page2.urls')),
#	url(r'^history/',include('manager.page3.urls')),
#	url(r'^(?P<>)/$')
	url(r'^analytics/', views.analytics, name='analytics' ),
	url(r'^history/', views.history, name='history' ),
	url(r'^admin/', admin.site.urls),
	url(r'^searchli/', views.searchlicense, name='searchlicense'),
#	url(r'^searchdt/', views.searchdate, name='searchdate'),
]

urlpatterns += staticfiles_urlpatterns()
