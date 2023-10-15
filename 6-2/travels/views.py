from django.shortcuts import render, redirect
from .models import travels
from .forms import travelsForm

# Create your views here.
def index(request):
    travel = travels.objects.all()
    context = {
        'travel' : travel
    }
    return render(request, 'travels/index.html', context)

def create(request):
    if request.method == "POST":
        form = travelsForm(request.POST)
        if form.is_valid():
            travel = form.save()
            return redirect('travels:detail', travel.pk)
    else:
        form = travelsForm()
    context = {
        'form' : form
    }
    return render(request, 'travels/create.html', context)

def detail(request, pk):
    travel = travels.objects.get(pk=pk)
    context = {
        'travel' : travel
    }
    return render(request, 'travels/detail.html', context)

def delete(request, pk):
    travel = travels.objects.get(pk=pk)
    travel.delete()
    return redirect("travels:index")

def update(request, pk):
    travel = travels.objects.get(pk=pk)
    if request.method == "POST":
        form = travelsForm(request.POST, instance=travel)
        if form.is_valid():
            form.save()
            return redirect('travels:detail', travel.pk)
    else:
        form = travelsForm(instance=travel)
    context = {
        'form' : form,
        'travel' : travel
    }
    return render(request, 'travels/update.html', context)