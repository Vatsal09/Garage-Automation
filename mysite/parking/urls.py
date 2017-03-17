from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'parking'

urlpatterns = [
	# /parking/
    url(r'^$', views.index, name='index'),
    # /parking/index/
    url(r'^main/$', views.main, name='main'),
    # /parking/add_lot/
    url(r'^add_lot/$', views.add_lot, name='add_lot'),
    # /parking/delete_lot/
    url(r'^(?P<lot_id>[0-9]+)/delete_lot/$', views.delete_lot, name='delete_lot'),
    # /parking/<Parking_Lot ID>/detail	    
    url(r'^(?P<lot_id>[0-9]+)/$', views.detail, name='detail'),
    # /parking/<Parking_Lot ID>/add_spot
    url(r'^(?P<lot_id>[0-9]+)/add_spot/$', views.add_spot, name='add_spot'),
    # /parking/<Parking_Lot ID>/delete_spot
    url(r'^(?P<lot_id>[0-9]+)/delete_spot/(?P<spot_id>[0-9]+)/$', views.delete_spot, name='delete_spot'),
    # /parking/register_manager
    url(r'^register_manager/$', views.register_manager, name='register_manager'),
    # /parking/login_manager
    url(r'^login_manager/$', views.login_manager, name='login_manager'),
    # /parking/logout_manager
    url(r'^logout_manager/$', views.logout_manager, name='logout_manager'),
]

urlpatterns += staticfiles_urlpatterns()
