from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^gal/', include('gal.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^_admin/', include(admin.site.urls)),
    
    url(r'^', include('haselsite.urls')),
    

    #url(r'^admin/', include(admin.site.urls)),
)
