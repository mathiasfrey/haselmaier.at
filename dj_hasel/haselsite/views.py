from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count

from models import BlogEntry, BlogTag, BlogAuthor, LeitstellenProject

def home(request):
    
    return render(request, 'haselsite/home.html')
    
def group(request):
    
    blogs = BlogEntry.objects.filter(publish=True, brand='GR').order_by('-publish')
    
    context = {
        'blogs': blogs,
    }
    
    return render(request, 'haselsite/group.html', context)
    
def wohn_art(request):

    blogs = BlogEntry.objects.filter(publish=True, brand='WA').order_by('-publish')
    
    context = {
        'blogs': blogs,
    }
    
    return render(request, 'haselsite/wohn-art.html', context)
    
def leitstellen(request):

    #blogs = BlogEntry.objects.filter(publish=True, brand='LS').order_by('-publish')
    #projects = LeitstellenProject.objects.all()

    #context = {
    #    'blogs': blogs,
    #    'request': request,
    #    'projects': projects,
    #}
    
    #return render(request, 'haselsite/leitstellen.html', context)

    return redirect("https://www.dieleitstelle.at/")
    
def tischlerei(request):

    #blogs = BlogEntry.objects.filter(publish=True, brand='TI').order_by('-publish')
    #
    #context = {
    #    'blogs': blogs,
    #}
    #
    #return render(request, 'haselsite/tischlerei.html', context)

    return redirect("https://haselmaier-tischlerei.at/")
    
def e_technik(request):

    #blogs = BlogEntry.objects.filter(publish=True, brand='ET').order_by('-publish')
    #
    #context = {
    #    'blogs': blogs,
    #}
    #
    #return render(request, 'haselsite/e-technik.html', context)

    return redirect("https://www.haselmaier-elektro.at/")

def test(request):
    
    return render(request, 'haselsite/test.html')

def blog(request):
    
    def _get_brand_value(brand):
        
        brand_names = BlogEntry.BRAND_CHOICES
        
        for x in brand_names:
            if x[0] == brand:
                return x[1]
    
    # all entries
    entries = BlogEntry.objects.filter(publish=True)
    
    # all used tags + count
    tags = BlogTag.objects.filter(blogentry__publish=True).annotate(Count('blogentry')).order_by('name')
    
    # all active authors + blogentry__count
    authors = BlogAuthor.objects.filter(blogentry__publish=True).annotate(Count('blogentry')).order_by('blogentry__count')
    
    # existing brand blogs
    tbrands =  BlogEntry.objects.filter(publish=True).order_by('brand').values_list('brand').distinct()
    brands= []
    
    for b in tbrands:
        
        v = b[0]
        n = _get_brand_value(v)
        u = n.lower()
        
        cnt = BlogEntry.objects.filter(publish=True, brand=v).count()
        brands.append({'name': n, 'count': cnt, 'url': u})
    
    context = {
        'entries': entries,
        'tags': tags,
        'authors': authors,
        'brands': brands,
    }
    
    #return HttpResponse(template.render(context, request))
    return render(request, 'haselsite/blog.html', context)

def blog_author(request, id):
    
    entries = BlogEntry.objects.filter(publish=True, author=id)
    
    context = {
        "entries": entries,
        "author": BlogAuthor.objects.get(pk=id),
    }
    
    return render(request, 'haselsite/blog_author.html', context)

def blog_brand(request, brand):
    
    
    def _get_brand_key(brand):
        
        brand_names = BlogEntry.BRAND_CHOICES
        
        for x in brand_names:
            if x[1].lower() == brand:
                return x[0]
    
    brand_key = _get_brand_key(brand)
      
    entries = BlogEntry.objects.filter(publish=True, brand=brand_key)
    
    
    context = {
        "entries": entries,
        "brand": {'name': brand, 'key': brand_key},
    }
    
    return render(request, 'haselsite/blog_brand.html', context)

def blog_tag(request, tag):
    
    # get real tag
    tag_object = BlogTag.objects.get(name__iexact=tag)
    
    entries = BlogEntry.objects.filter(publish=True, tags=tag_object)
    
    context = {
        "tag": tag_object,
        "entries": entries,
    }
    
    return render(request, 'haselsite/blog_tag.html', context)

def blog_detail(request, slug):
    
    entry = get_object_or_404(BlogEntry, slug=slug)
    
    template = loader.get_template('haselsite/blog_detail.html')
    
    context = {
        'entry': entry,
    }
    
    return HttpResponse(template.render(context, request))

