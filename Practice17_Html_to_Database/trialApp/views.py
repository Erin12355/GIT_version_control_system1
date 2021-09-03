from django.shortcuts import render
from trialApp.models import Trial
# Create your views here.

def home(request):
    return render(request,'trialApp/home.html')

def create_view(request):
    if request.method=='POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('sdate') and request.POST.get('edate') and request.POST.get('course'):
            jsn=Trial()
            jsn.fname=request.POST.get('fname')
            jsn.lname=request.POST.get('lname')
            jsn.sdate=request.POST.get('sdate')
            jsn.edate=request.POST.get('edate')
            jsn.course=request.POST.get('course')
            jsn.save()
            return render(request,'trialApp/success.html')
    return render(request,'trialApp/form.html')