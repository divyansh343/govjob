from django.shortcuts import render
from home.models import Contact
from jobs.models import Job



def index(request):
    job = Job.objects.all()
    params = {job : 'job'}
    return render(request, 'home/index.html',params)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        contact=Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "home/contact.html")