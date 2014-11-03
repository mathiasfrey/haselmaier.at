# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
from views import CategoryPictureList, GalleryOverview, CategoryEdit, PictureEdit, \
           CategoryCreate, PictureCreate, CategoryList, CategoryDelete, PictureDelete
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView


direct = TemplateView.as_view

def is_authorized(user):
    # user has to be authenticated
    if not user.is_anonymous() and user.is_authenticated():
        return user.is_staff

auth_check = user_passes_test(is_authorized)

urlpatterns = patterns('',
    url(r'^$', 
        auth_check(
            RedirectView.as_view(url=reverse_lazy('management-list-galleries'))
                   ), 
        name='browse-galleries'),
    #
    url(r'^view/(?P<gallery>[\w\-]+)/(?P<category>[\w\-]+)/$', 
        CategoryPictureList.as_view(template_name='gal/preview/category.html'), 
        name='preview-category'),
    url(r'^view/(?P<gallery>[\w\-]+)/$',
        direct(template_name='gal/preview/gallery_mgr.html'),
        name='preview-gallery'),
    url(r'^mgr/$', auth_check(GalleryOverview.as_view()),  
        name='management-list-galleries'),
    #url(r'^categories/(?P<category>[\w\-]+)/$', CategoryPictureList.as_view(), name='management-list-category'),
    url(r'^mgr/(?P<gallery>[\w\-]+)/_edit/(?P<category>[\w\-]+)/$', 
        auth_check(CategoryEdit.as_view()), 
        name='management-edit-category'),
    url(r'^mgr/(?P<gallery>[\w\-]+)/_add/$', 
        auth_check(CategoryCreate.as_view()), 
        name='management-add-category'),
    
    url(r'^mgr/(?P<gallery>[\w\-]+)/$', 
        auth_check(CategoryList.as_view()), 
        name='management-list-gallery'),
    url(r'^mgr/(?P<gallery>[\w\-]+)/(?P<category>[\w\-]+)/$', 
        auth_check(CategoryPictureList.as_view()), 
        name='management-list-category'),
    url(r'^mgr/(?P<gallery>[\w\-]+)/_delete/(?P<category>[\w\-]+)/$', 
        auth_check(CategoryDelete.as_view()), 
        name='management-delete-category'),
    
    url(r'^mgr/(?P<gallery>[\w\-]+)/(?P<category>[\w\-]+)/_add/$', 
        auth_check(PictureCreate.as_view()), 
        name='management-add-picture'),
    url(r'^mgr/(?P<gallery>[\w\-]+)/(?P<category>[\w\-]+)/_edit/(?P<pk>\d+)/$', 
        auth_check(PictureEdit.as_view()), 
        name='management-edit-picture'),
    url(r'^mgr/(?P<gallery>[\w\-]+)/(?P<category>[\w\-]+)/_delete/(?P<pk>\d+)/$', 
        auth_check(PictureDelete.as_view()), 
        name='management-delete-picture'),
    )
