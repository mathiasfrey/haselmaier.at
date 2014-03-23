from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
                       
    url(r'^$', 'haselsite.views.home', name='home'),
    
    url(r'^group/$', 'haselsite.views.group', name='group'),
    url(r'^tischlerei/$', 'haselsite.views.group', name='tischlerei'),
    
    url(r'^wohn-art/$', 'haselsite.views.wohn_art', name='wohn-art'),
    url(r'^wohnart/$', RedirectView.as_view(url='/wohn-art/', permanent=False)),
    
    url(r'^leitstellen/$', 'haselsite.views.group', name='leitstellen'),
    
    url(r'^e-technik/$', 'haselsite.views.group', name='e-technik'),
    url(r'^etechnik/$', RedirectView.as_view(url='/e-technik/', permanent=False)),
 
)