from django.shortcuts import render
from .models import Job
# Create your views here.
def jobpage(request,slug):
    value = Job.objects.filter(slug=slug).first()
    params = { value : 'job'}
    return render(request, 'jobs/jobpage',params)