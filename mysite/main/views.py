from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def calculator(request):
    number1 = request.POST.get('number1')
    char = request.POST.get('char')
    number2 = request.POST.get('number2')
    result = 0
    if char == '+':
        result = int(number1) + int(number2)
    elif char == '-':
        result = int(number1) - int(number2)
    elif char == '*':
        result = int(number1) * int(number2)
    elif char == '/':
        try:
            result = int(number1) / int(number2)
        except ZeroDivisionError:
            result = 'No input 0'
            return render(request, 'calculator.html', context={'result':result})

    return render(request, 'calculator.html', context={'result':result})