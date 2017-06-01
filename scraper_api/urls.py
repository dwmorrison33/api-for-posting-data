from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api/', include('scrape_data.api.urls', namespace='api')),
    url(r'^', include('scrape_data.urls')),
]
