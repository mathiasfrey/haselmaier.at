# -*- coding: utf-8 -*-
"""
    Models for gallery.
    
    Defines Galleries, which have categories, which can take pictures.
    uses sorl to upload/thumbnail the images.    

"""
from django.db import models
from django.utils.text import slugify
from sorl.thumbnail import ImageField
from django.conf import settings
import os

# todo: do this properly.

def file_upload(instance, filename):
    cat = 'no-category'
    gal = 'no-gallery'
    if instance.category:
        cat = instance.category.slug
        if instance.category.gallery:
            gal = instance.category.gallery.slug
    base = os.path.join( 'galleries', 
                         gal, cat,
                         filename)
    return base

class Gallery(models.Model):
    title = models.CharField(max_length=250, blank=True, default='')
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Gallery, self).save(*args, **kwargs)
    
    
    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return u'<Untitled: %s>' % (self.slug,)
    
    def get_front_images(self):
        return Picture.objects.filter(category__gallery__pk=self.pk)[:4]

class Category(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='categories')
    title = models.CharField(max_length=250, default='')
    slug = models.SlugField(blank=True)
    
    order = models.IntegerField(blank=True, default=0)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Category, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.title
    
class Picture(models.Model):
    category = models.ForeignKey(Category, related_name='pictures')
    
    # use sorl.ImageField.
    image = ImageField(upload_to=file_upload, 
                       #width_field = 'image_width',
                       #height_field='image_height',
                       )
    #image_width = models.IntegerField(blank=True, editable=False, default=0)
    #image_height = models.IntegerField(blank=True, default=0, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_changed = models.DateTimeField(auto_now=True, blank=True)
    
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    order = models.IntegerField(blank=True, default=0)
    
    def __unicode__(self):
        return u'File: %s, Title %s' % (self.image, self.title)

