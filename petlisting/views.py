from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'petlisting/index.html')

def about(request):
    return render(request, 'petlisting/about.html')

def contact(request):
    return render(request, 'petlisting/contact.html')