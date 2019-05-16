from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost

# obj = BlogPost.objects.get(id=1)

#------------- commenting out after having all 5 crud+1 pages ready -------------------------

# def blog_post_details_page(request , slug):

#     print("DJANGO SAYS", request.method, request.path, request.user)

#     #obj = BlogPost.objects.get(id=post_id)  #query -> daatbase
#     # try : 
#     #     obj = BlogPost.objects.get(id = post_id)
#     # except BlogPost.DoesNotExist:
#     #     raise Http404
#     # except ValueError:
#     #     raise Http404

#     queryset = BlogPost.objects.filter(slug=slug)
#     if queryset.count() >= 1:
#         obj = queryset.first()


#     # obj = get_object_or_404(BlogPost, slug=slug)

#     context = {"object": obj}
#     template_name = "blog_post_details.html"
#     return render(request, template_name, context)  

#----------------------------------commenting out -----------------------------------------------------------------


    # CRUD
    # CREATE RETREIVE UPDATE DELETE

def blog_post_list_view(request):
    # qs = BlogPost.objects.all()   #lists out all objects
    qs = BlogPost.objects.filter(slug__icontains = 'hello')  # searching specific things
    template_name = 'blog/list.html'
    context = {'object_list' : qs}
    return render(request, template_name, context)

def blog_post_create_view(request):
    template_name = 'blog/create.html'
    context = {'form' : None}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    template_name = "blog/detail.html"
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj, 'form' : None}
    template_name = "blog/update.html"
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    template_name = "blog/delete.html"
    return render(request, template_name, context)