from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'name':'Hello World'})
def crush(request):
    return render(request, 'result.html')


