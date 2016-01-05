from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from models import BlogEntry, BlogTag

def home(request):
    
    return render(request, 'haselsite/home.html')
    
def group(request):
    
    return render(request, 'haselsite/group.html')
    
def wohn_art(request):
    
    return render(request, 'haselsite/wohn-art.html')
    
def leitstellen(request):
    
    return render(request, 'haselsite/leitstellen.html')
    
def tischlerei(request):
    
    return render(request, 'haselsite/tischlerei.html')
    
def e_technik(request):
    
    return render(request, 'haselsite/e-technik.html')

def test(request):
    
    return render(request, 'haselsite/test.html')

def blog(request):
    
    entries = BlogEntry.objects.filter(publish=True)
    #template = loader.get_template('haselsite/blog.html')
    context = {
        'entries': entries,
    }
    
    #return HttpResponse(template.render(context, request))
    return render(request, 'haselsite/blog.html', context)

def blog_detail(request, slug):
    
    entry = get_object_or_404(BlogEntry, slug=slug)
    
    template = loader.get_template('haselsite/blog_detail.html')
    
    context = {
        'entry': entry,
    }
    
    return HttpResponse(template.render(context, request))