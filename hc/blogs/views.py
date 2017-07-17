from django.shortcuts import render
from hc.blogs.models import Blog, Category
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    categories = Category.objects.all(),
    posts = Blog.objects.all()[:5]
    return render(request, 'blogs/index.html', {'posts': posts, 'categories':categories})


def view_post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render('blogs/view_post.html', {'post':post})


def view_categories(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'blogs/all-posts.html', {'category': category,
                                       'posts': Blog.objects.filter(category=category)[:5]
                                       })


def new_post(request):
    return render(request, 'blogs/new_post.html')
