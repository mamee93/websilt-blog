from django.shortcuts import render
from  .models import Post
# Create your views here.

def post_list(request):
    all_post= Post.objects.all()
    context ={
       'all_post':all_post
    }
    return render(request,'blog/list.html',context)

def post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    context ={
        'post':post_detail
    }
    return render(request, 'blog/details.html', context)