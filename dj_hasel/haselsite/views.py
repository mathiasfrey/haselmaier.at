from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'haselsite/home.html')
    
def group(request):
    
    return render(request, 'haselsite/group.html')
    
def wohn_art(request):
    
    return render(request, 'haselsite/wohn-art.html')
    
def leitstellen(request):
    
    return render(request, 'haselsite/leitstellen.html')      