from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def petdetails(request):
    return render(request, 'petdetails.html')

def petpreview(request):
    return render(request, 'petpreview.html')