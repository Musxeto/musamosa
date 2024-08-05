from django.shortcuts import render
from django.http import HttpResponse
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
    if request.method == 'POST':
        return HttpResponse('POST request received')
    return render(request, 'contact.html')
