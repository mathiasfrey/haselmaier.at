from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
                       
    url(r'^$', 'haselsite.views.home', name='home'),
    
    url(r'^group/$', 'haselsite.views.group', name='group'),
    
    url(r'^wohn-art/$', 'haselsite.views.wohn_art', name='wohn_art'),
    url(r'^wohnart/$', RedirectView.as_view(url='/wohn-art/', permanent=False)),
    
    url(r'^leitstellen/$', 'haselsite.views.leitstellen', name='leitstellen'),
    
    url(r'^tischlerei/$', 'haselsite.views.tischlerei', name='tischlerei'),
    
    url(r'^e-technik/$', 'haselsite.views.e_technik', name='e_technik'),
    url(r'^etechnik/$', RedirectView.as_view(url='/e-technik/', permanent=False)),
 
)