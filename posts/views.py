from django.shortcuts import render
from .models import Post
from comment.models import Comment
from django.shortcuts import render, redirect
from django.http import HttpResponse

def post_list_view(request):
    post_list = Post.objects.all().order_by('-created_at') 
    context={
        'post_list' : post_list
    }
    return render(request, 'postList.html', context)


def post_create(request):
    if request.method == "GET": #화면 띄우기 용도
        return render(request, 'post_create.html')
    
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(user=request.user, title=title, content=content)
        post.save()
            
        return redirect('post_detail', post.id)
    

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_list = Comment.objects.filter(post=post).order_by('-created_at')

    context = {
        'post' : post,
        'comment_list': comment_list
    }
    post.views +=1
    post.save()
    return render(request, 'post.html', context)
    
def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user != post.user:
        return redirect('post_detail')
    
    post.delete()
    return redirect('post_list')
