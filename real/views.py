from django.shortcuts import render, HttpResponse
# Create your views here.
def index(request):
    context ={
        'bladee':"in my bag one second"
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("about")

def services(request):
    return HttpResponse("contact")

def contact(request):
    return HttpResponse("Contact Page")