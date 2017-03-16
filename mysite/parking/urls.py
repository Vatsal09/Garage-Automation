from django.conf.urls import url
from . import views

app_name = 'parking'

urlpatterns = [
	# /parking/
    url(r'^$', views.index, name='index'),
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
    
    
]
