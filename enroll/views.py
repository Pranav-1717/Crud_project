from django.shortcuts import render,HttpResponseRedirect
from .models import User
from .forms import StudentRegistration

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm , email=em , password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return  render(request,'enroll/add&show.html',{'form':fm , 'stu':stud})


def updatedata(request , id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST , instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(instance=pi)
    return render(request , 'enroll/update.html' , {'form':fm})

def deletedata(request , id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id) #pk = primary key
        pi.delete()
        return HttpResponseRedirect('/')