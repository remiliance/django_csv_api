from django.conf.urls import url

from airport import views

urlpatterns = [
    url(r'^$', views.index),  # "/airport" will call the method "index" in "views.py"
]
