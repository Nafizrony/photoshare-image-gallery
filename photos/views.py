from django.shortcuts import render,redirect
from .models import Category,Gallery
# Create your views here.


def gallery(request,category_slug=None):
    categories = None
    gallery = None
    if category_slug != None:
        categories = Category.objects.get(slug=category_slug)
        gallery = Gallery.objects.filter(category=categories)
    else:
        gallery = Gallery.objects.all()
    context = {'gallery':gallery}
    return render(request,'photos/gallery.html',context)

def photo(request,category_slug,pk):
    gallery = None
    try:
        gallery = Gallery.objects.get(category__slug=category_slug,id=pk)
    except Exception as e:
        pass
    context = {'gallery':gallery}
    return render(request,'photos/photo.html',context)

def add_photo(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.get('images')
        if data['category'] != 'none':
            category = Category.objects.get(slug=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(category_name=data['category_new'])

        else:
            category = None
        Gallery.objects.create(
            category = category,
            description = data['description'],
            images = images,
            slug = category.id
        )
        return redirect('gallery')
    context = {'categories':categories}
    return render(request,'photos/add_photo.html',context)