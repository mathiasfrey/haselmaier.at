# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^gal/', include('gal.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^_admin/', include(admin.site.urls)),
    # login logout.
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/logged_out.html'}, name="logout"),

    url(r'^', include('haselsite.urls')),
    

    #url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG or True:
    urlpatterns += patterns('',
        #url(r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve',
            #{'document_root': settings.STATIC_ROOT}
        #    ),
        #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        #    'document_root': settings.MEDIA_ROOT,
        #}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )
