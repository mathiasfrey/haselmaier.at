from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from models import Category, Gallery, Picture
from django.views.generic.base import TemplateView
from forms import CategoryForm, PictureForm
from django.views.generic.edit import FormView, UpdateView, CreateView,\
    DeleteView
from django.core.urlresolvers import reverse
from gal.forms import DeleteForm

class AjaxTemplateMixin(object):    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'template_name_ajax'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.template_name_ajax = ''.join(split)
        if request.is_ajax():
            self.template_name = self.template_name_ajax
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

class SideMenuMixin(object):
    def set_my_category(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
    
    def set_my_gallery(self):
        self.gallery = get_object_or_404(Gallery, slug=self.kwargs['gallery'])
    
    def get_sidemenu_context(self, context, **kwargs):
        context['galleries'] = Gallery.objects.all()
        # make sure gallery and category if supplied in the url are always in the context.
        if 'gallery' in self.kwargs.keys():
            if not hasattr(self, 'gallery'):
                self.set_my_gallery()
            context['gallery'] = self.gallery
        
        if 'category' in self.kwargs.keys():
            if not hasattr(self, 'category'):
                # most likely for categoryviews this will be set since they actually view pictures.
                self.set_my_category()
            context['category'] = self.category
            if self.category.gallery:
                context['categories'] = Category.objects.filter(gallery=self.category.gallery).order_by('order', 'title')
        return context

class CategoryPictureList(SideMenuMixin,  AjaxTemplateMixin, ListView):
    template_name = 'gal/list-pictures.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        return Picture.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryPictureList, self).get_context_data(**kwargs)
        print ""
        print self.kwargs
        return self.get_sidemenu_context(context)

class GalleryOverview(SideMenuMixin, ListView):
    
    template_name='gal/list-galleries.html'

    def get_queryset(self):
        return Gallery.objects.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GalleryOverview, self).get_context_data(**kwargs)
        return self.get_sidemenu_context(context)

class CategoryList(CategoryPictureList):
    
    def get_queryset(self):
        self.set_my_gallery()
        if 'category' in self.kwargs.keys():
            self.category = get_object_or_404(Category, slug=self.kwargs['category'])
        else:
            if not self.gallery.categories.count():
                self.category = None
                return Picture.objects.none()
            else:
                self.category = self.gallery.categories.all()[0]
        return Picture.objects.filter(category=self.category)
    

class CategoryCreate(SideMenuMixin,  AjaxTemplateMixin, CreateView):
    template_name = 'gal/category_create.html'
    form_class = CategoryForm
    success_url = ''
    model = Category
    
    def get_initial(self):
        self.set_my_gallery()
        return {'gallery': self.gallery}
    
    def get_success_url(self):
        self.set_my_gallery()
        self.category = self.object
        return reverse('management-list-category', kwargs={'gallery': self.gallery.slug,
                                                           'category': self.category.slug})
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryCreate, self).get_context_data(**kwargs)
        return self.get_sidemenu_context(context)


class CategoryEdit(SideMenuMixin, AjaxTemplateMixin,  UpdateView):
    template_name = 'gal/category_edit.html'
    form_class = CategoryForm
    model = Category
    success_url = ''
    
    def get_object(self):
        self.set_my_category()
        return self.category
    
    def get_success_url(self):
        self.set_my_gallery()
        self.set_my_category()
        return reverse('management-list-category', kwargs={'gallery': self.gallery.slug,
                                                           'category': self.category.slug})
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryEdit, self).get_context_data(**kwargs)
        return self.get_sidemenu_context(context)

class CategoryDelete(SideMenuMixin, AjaxTemplateMixin, DeleteView):
    template_name = 'gal/category_confirm_delete.html'
    model = Category
    
    def get_object(self):
        self.set_my_category()
        return self.category

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategoryDelete, self).get_context_data(**kwargs)
        return self.get_sidemenu_context(context)
    
    def get_success_url(self):
        self.set_my_gallery()
        if self.gallery.categories.count() > 1:
            
            return reverse('management-list-category', kwargs={'gallery': self.gallery.slug,
                                                           'category': self.gallery.categories.exclude(pk=self.object.pk)[0].slug})
        else:
            return reverse('management-list-gallery', kwargs={'gallery': self.gallery.slug}) 


class PictureEdit(SideMenuMixin, AjaxTemplateMixin,  UpdateView):
    template_name = 'gal/picture_edit.html'
    form_class = PictureForm
    model = Picture
    success_url = ''
    
    def get_success_url(self):
        self.set_my_category()
        self.set_my_gallery()
        return reverse('management-list-category', kwargs={'gallery': self.gallery.slug,
                                                           'category': self.category.slug}) 
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PictureEdit, self).get_context_data(**kwargs)
        context = self.get_sidemenu_context(context)
        
        return context
    
    def get_queryset(self):
        # set our success url.
        self.set_my_category()
        self.set_my_gallery()
        return Picture.objects.all()

class PictureCreate(SideMenuMixin, AjaxTemplateMixin,  CreateView):
    template_name = 'gal/picture_create.html'
    form_class = PictureForm
    success_url = ''
    model = Picture
    
    def get_success_url(self):
        self.set_my_category()
        self.set_my_gallery()
        return reverse('management-list-category', kwargs={'gallery': self.gallery.slug,
                                                           'category': self.category.slug}) 
    
    def get_initial(self):
        self.set_my_category()
        return {'category': self.category}
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PictureCreate, self).get_context_data(**kwargs)
        return self.get_sidemenu_context(context)

class PictureDelete(SideMenuMixin, AjaxTemplateMixin, DeleteView):
    template_name = 'gal/picture_confirm_delete.html'
    model = Picture
    success_url = ''
    
    def get_success_url(self):
        self.set_my_category()
        self.set_my_gallery()
        return reverse('management-list-category', kwargs={'gallery': self.gallery.slug,
                                                           'category': self.category.slug}) 
    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PictureDelete, self).get_context_data(**kwargs)
        return self.get_sidemenu_context(context)
