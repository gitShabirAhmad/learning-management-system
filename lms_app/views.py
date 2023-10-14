from django.shortcuts import render
from lms_app.models import Cls
# Create your views here.
def main(request):
    return render(request,'lms_app/main.html')

def classes(request):
    course_classes = Cls.objects.all()

    # search functionality
    name = request.GET.get('search')
    if name != '' and name is not None:
        course_classes = course_classes.filter(name__icontains=name)

    
    return render(request,'lms_app/classes.html',{"course_classes":course_classes})
