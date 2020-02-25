from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    my_title = "Hello there ....."
    context = { "title": my_title }

    # check authentication here rather than in the template
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    return render(request, "index.html", context)


def about_page(request):
    # return HttpResponse("<h1>About us</h1>")
    return render(request, "about.html", {"title" : 'About us'})


def contact_page(request):
    # return HttpResponse("<h1>Contact</h1>")
    return render(request, "index.html", {"title" : 'Contact'})


def example_page(request):
    context = { "title": "Example"}
    template_name = "example.txt"
    template_obj = get_template(template_name)
    # template_item = template_obj.render(context)
    return HttpResponse(template_obj.render(context))
