from django.shortcuts import render
# from django.http  import HttpResponse
from .models import Gallery


def welcome(request):
    photos = Gallery.objects.all()
    return render(request, 'welcome.html',{"photos":photos})    

