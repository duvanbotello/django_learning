from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def blog(request):
    blogs = Post.objects.all()
    return render(request, "blog/blog.html",{"blogs": blogs})