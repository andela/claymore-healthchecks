from django.conf.urls import include, url
from django.contrib import admin
import debug_toolbar

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('hc.accounts.urls')),
    url(r'^__debug__/', include(debug_toolbar.urls))
    url(r'^', include('hc.api.urls')),
    url(r'^', include('hc.front.urls')),
    url(r'^', include('hc.payments.urls'))
]
