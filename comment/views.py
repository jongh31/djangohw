from django.shortcuts import render, redirect
from .models import Comment
from posts.models import Post

def comment_create(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        return render(request, 'comment_create.html', {'post': post})
    elif request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment.objects.create(user=request.user, content=content, post=post)
        comment.save()
        return redirect('post_detail', post_id)
    
def comment_delete(request, post_id,comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.user != comment.user:
        return redirect('post_detail')
    
    comment.delete()
    return redirect('post_detail', post_id)