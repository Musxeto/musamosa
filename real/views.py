from django.shortcuts import render
from .models import Contact
from django.http import HttpResponseRedirect
from django.urls import reverse
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
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return HttpResponseRedirect(reverse('contact'))
    return render(request, 'contact.html')