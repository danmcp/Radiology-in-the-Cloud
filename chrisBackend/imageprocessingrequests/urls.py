from django.conf.urls import url
from imageprocessingrequests import views

urlpatterns = [
    url(r'^imageprocessingrequests/$', views.imageprocessingrequest_list),
    url(r'^imageprocessingrequests/(?P<pk>[0-9]+)/$', views.imageprocessingrequest_detail),
]