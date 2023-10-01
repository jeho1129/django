from django.shortcuts import render

# Create your views here.
def first(request):
    messages = request.GET.get('messages')
    context = {
        'messages' : messages
    }
    return render(request, 'throw_catch/first.html', context)

def second(request):
    messages = request.GET.get('messages')
    context = {
        'messages' : messages
    }
    return render(request, 'throw_catch/second.html', context)