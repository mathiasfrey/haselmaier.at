from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'haselsite/home.html')
    
def group(request):
    
    return render(request, 'haselsite/group.html') 