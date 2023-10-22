from django.shortcuts import render,redirect
from lms_app.models import Cls
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.base import View

# Create your views here.
def main(request):
    return render(request,'lms_app/main.html')

def classes(request):
    course_classes = Cls.objects.all()

    # search functionality
    name = request.GET.get('search')
    if name != '' and name is not None:
        course_classes = course_classes.filter(name__icontains=name)

    # Pagination
    paginator = Paginator(course_classes,10)
    page = request.GET.get('page')
    course_classes = paginator.get_page(page)

    return render(request,'lms_app/classes.html',{"course_classes":course_classes})


def detail(request,class_id):
    cls_id = Cls.objects.get(id=class_id)
    context = {'class_id':cls_id}
    return render(request,'lms_app/detail.html',context)

def login(request):
    return render(request,'lms_app/login.html')


def create(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        n = request.POST['name']    
        t = request.POST['time']    
        d = request.POST['date']
        try:
            clas=Cls.objects.create(name=n,time=t,started_date=d)
            clas.save()
            error = 'no'
        except:
            error = 'yes'


    return render(request,'lms_app/create.html',{'error':error})

def delete(request,class_id):
    if not request.user.is_staff:
        return redirect('login')
    cls = Cls.objects.get(id=class_id)
    cls.delete()
    return redirect('classes')


def update(request,class_id):
    if not request.user.is_staff:
        return redirect('login')
    clas = Cls.objects.get(id=class_id)
    if request.method == 'GET':
        return render(request,'lms_app/update.html',{'clas':clas})
    else:
        name = request.POST.get('name')    
        time = request.POST.get('time')    
        started = request.POST.get('date') 

        clas.name = name   
        clas.time = time   
        clas.started_date = started
        clas.save()

        return redirect('classes')

