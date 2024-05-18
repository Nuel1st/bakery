from django.shortcuts import render

# Create your views here.

def home(request):
    return render( request, 'bake/index.html')


def about(request):
    return render( request, 'bake/about.html')

def blog(request):
    return render( request, 'bake/blog.html')

def book(request):
    return render( request, 'bake/book.html')

def contact(request):
    return render( request, 'bake/contact.html')

def event(request):
    return render( request, 'bake/event.html')

def menu(request):
    return render( request, 'bake/menu.html')

def service(request):
    return render( request, 'bake/service.html')

def team(request):
    return render( request, 'bake/team.html')

def testimonial(request):
    return render( request, 'bake/testimonial.html')