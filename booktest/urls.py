from django.conf.urls import  url
from booktest import views

urlpatterns = [

    url(r'^index$',views.index),
    url(r'^prov$',views.prov),
    url(r'^city(\d+)$',views.city),
    url(r'^show_area(?P<pindex>\d*)$',views.show_area)


]
