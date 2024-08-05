from django.shortcuts import render

def index(request):
    context = {
        'bladee': "in my bag one second"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def samosay(request):
    return render(request, 'samosay.html')

def contact(request):
    
    return render(request, 'contact.html')
