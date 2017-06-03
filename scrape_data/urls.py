from django.conf.urls import url, include
from scrape_data import views

urlpatterns = [
    url(r'^api/data/$', views.scrape_data),
    url(r'^api/data/(?P<pk>[0-9]+)$', views.scrape_data_detail)
]