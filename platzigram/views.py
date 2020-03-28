
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    return HttpResponse('Current time server {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sort_integers(request):
    numbers =  request.GET['numbers']
    numbers = list(map(int, numbers.split(','))) 
    return JsonResponse({'numeros':sorted(numbers)})

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)
