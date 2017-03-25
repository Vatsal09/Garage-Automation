from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name="manager"
# /manager/
urlpatterns =[
	url(r'^$', views.index, name='index'),
#	url(r'^main/$', views.main, name='main'),



]

urlpatterns += staticfiles_urlpatterns()
