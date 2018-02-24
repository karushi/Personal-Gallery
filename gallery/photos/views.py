from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to Photo Gallery')

def welcome(request):
    return render(request, 'welcome.html',{"photos":photos})    

