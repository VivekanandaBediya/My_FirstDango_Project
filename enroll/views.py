from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

#This is the add function
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']

            reg=User(name=nm, email=em, password=pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()  #all() method give us all data from the database
    return render(request,'enroll/addandshow.html',{'stu':stud, 'form':fm})

#This is the update/Edit function
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})


#This is the delete function
def delete_data(request,id):
    if request.method == 'POST':
            pi=User.objects.get(pk=id)  #pk is the primary key
            pi.delete()
            return HttpResponseRedirect('/')