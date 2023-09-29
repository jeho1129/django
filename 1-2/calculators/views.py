from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    multi = num1 * num2
    sub = num1 - num2
    if num2 == 0:
        div = '계산할 수 없습니다'
    else:
        div = num1 / num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'multi' : multi,
        'sub' : sub,
        'div' : div
    }
    return render(request, 'calculators/result.html', context)