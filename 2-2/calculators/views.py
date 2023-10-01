from django.shortcuts import render

# Create your views here.
def calculator(request, num1, num2):
    multi = num1 * num2
    minus = num1 - num2
    if num2 == 0:
        division = False
    else:
        division = num1 / num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'multi' : multi,
        'minus' : minus,
        'division' : division
    }
    return render(request, 'calculators/calculator.html', context)