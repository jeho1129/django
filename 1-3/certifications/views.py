from django.shortcuts import render

# Create your views here.
def certification1(request):
    name = 'kim happy'
    age = range(25, 31)
    grade = ['a','b','c','s']
    context = {
        'name' : name,
        'age' : age,
        'grade' : grade
    }
    return render(request, 'certifications/certification1.html', context)

def certification2(request):
    name = 'park happy'
    age = range(25, 31)
    grade = ['a','b','c','s']
    context = {
        'name' : name,
        'age' : age,
        'grade' : grade
    }
    return render(request, 'certifications/certification2.html', context)

def certification3(request):
    name = 'lee happy'
    age = range(25, 31)
    grade = ['a','b','c','s']
    context = {
        'name' : name,
        'age' : age,
        'grade' : grade
    }
    return render(request, 'certifications/certification3.html', context)