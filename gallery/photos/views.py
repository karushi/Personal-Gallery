from django.shortcuts import render
# from django.http  import HttpResponse
from .models import Gallery


def welcome(request):
    photos = Gallery.objects.all()
    return render(request, 'welcome.html',{"photos":photos})    

def image(request, image_id):
     try:
           image = Gallery.objects.get(id = image_id)
     except Gallery.DoesNotExist:
           raise Http404()

     return render(request,"image.html", {"image":image})
     

def search_results(request):
     if 'category' in request.GET and request.GET['category']:
           search_category = request.GET.get('category')
           searched_categories = Gallery.search_by_category(search_category)
           message = f"{search_category}"

           return render(request, 'search.html', {"message":message, "categories":searched_categories})

     else:
           message = "You haven't searched for any term"

           return render(request, 'search.html',{"message":message})