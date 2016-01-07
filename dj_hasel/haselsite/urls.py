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
    
    url(r'^blog/$', 'haselsite.views.blog', name='blog'),
    
    url(r'^blog/autor/(?P<id>[\d]+)/$', 'haselsite.views.blog_author', name='blog_author'),
    url(r'^blog/schlagwort/(?P<tag>[\w-]+)/$', 'haselsite.views.blog_tag', name='blog_tag'),
    url(r'^blog/organisation/(?P<brand>[\w-]+)/$', 'haselsite.views.blog_brand', name='blog_brand'),
    
    url(r'^blog/(?P<slug>[\w-]+)/$', 'haselsite.views.blog_detail', name='blog_detail'),
 
    url(r'^test/$', 'haselsite.views.test', name='test'), 
)