# -*- coding: utf-8 -*-

from django import template
from ..models import Gallery, Category, Picture
register = template.Library()

@register.assignment_tag
def get_gallery(gallery):
    if isinstance(gallery, basestring):
        # strings go to slugs
        try:
            return Gallery.objects.filter(slug=gallery)[0]
        except:
            
            pass
    else:
        try:
            return Gallery.objects.filter(pk=gallery)[0]
        except:
            
            pass
    return None
    

@register.assignment_tag
def get_category_pictures(category, gallery=None):
    # if gallery is given, we search there.
    if gallery is not None:
        gal = None
        if isinstance(gallery, basestring):
            # strings go to slugs
            try:
                gal = Gallery.objects.get(slug=gallery)
            except:
                pass
        else:
            try:
                gal = Gallery.objects.get(pk=gallery)
            except:
                pass
        if gal is None:
            return ''
        try:
            cat = Category.objects.get(slug=category,
                                       gallery=gal)
        except:
            return ''
    else:
        try:
            cat = Category.objects.get(slug=category)
        except:
            return ''
    return Picture.objects.filter(category=cat)
