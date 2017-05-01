from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from . import views

app_name = 'garageAutomation'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login$', login, {'template_name': 'garageAutomation/login.html'}, name='login'),
    url(r'logout$', logout),
    url(r'register$', views.register, name='register'),
    url(r'^home/(?P<parkingLot_id>[0-9]+)/(?P<level>[0-9]+)$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
]


urlpatterns += staticfiles_urlpatterns()