from django.shortcuts import render
from lms_app.models import Cls
from django.core.paginator import Paginator
# Create your views here.
def main(request):
    return render(request,'lms_app/main.html')

def classes(request):
    course_classes = Cls.objects.all()

    # search functionality
    name = request.GET.get('search')
    if name != '' and name is not None:
        course_classes = course_classes.filter(name__icontains=name)

    
    paginator = Paginator(course_classes,2)
    page = request.GET.get('page')
    course_classes = paginator.get_page(page)

    return render(request,'lms_app/classes.html',{"course_classes":course_classes})


def detail(request,class_id):
    cls_id = Cls.objects.get(id=class_id)
    context = {'class_id':cls_id}
    return render(request,'lms_app/detail.html',context)


