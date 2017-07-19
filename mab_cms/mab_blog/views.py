from mab_blog.models import Post, Category
from django.shortcuts import render, get_object_or_404

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })

def view_post(request, year, month, day, slug):
    vars = {
        'post': get_object_or_404(Post, slug=slug)
    }
    return render(request, 'post.html', vars)

def view_category(request, slug):
    my_category = get_object_or_404(Category, slug=slug)
    vars = {
        'category': my_category,
        'posts': Post.objects.filter(category=my_category)[:5]
    }
    return render(request, 'list.html', vars)
