from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from airport import views
from airport.api import ApiTraffic

router = routers.DefaultRouter()
router.register(r'traffic', ApiTraffic)

urlpatterns = [
    url(r'^$', views.index),  # "/airport" will call the method "index" in "views.py"
    url(r'^listing/', views.listing),
    url(r'^adding/', views.adding, name='adding'),
    url(r'^search/', views.search, name='search'),
    url(r'^api/', include(router.urls)),

]


