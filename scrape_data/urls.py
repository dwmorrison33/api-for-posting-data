from django.conf.urls import url, include
from scrape_data import views

urlpatterns = [
    url(r'^api/post-data-here/$', views.scrape_data),
]