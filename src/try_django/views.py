from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# {
#     thumb rule for WebD people
#     DRY = Don't Repeat Yourself

#     put everything you require everytime in a single page and render that single page....instaed of rendering the same contents everytime
# }

from .forms import ContactForm

def home_page(request):
    # return HttpResponse("<h1>Hello World!<h1>")  used to render toy-items :D
    # return render(request, "hello.html")    #This is used to render an entire html page

    my_title = "Title of hello.html"
    context = {"title" : my_title}
    return render(request, "hello.html", context)



def about_page(request):
    # return HttpResponse("<h1>About Us</h1>")
    return render(request, "about.html", {"title" :"This is about us"})



def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title" : "contact us",
        "form" : form
    }
    return render(request, "form.html", context)
    # return HttpResponse("<h1>Contact Us</h1>")
