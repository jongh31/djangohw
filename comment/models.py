from django.db import models

# Create your models here.
class Comment(models.Model):
    content = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)

class Like(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    comment = models.ForeignKey('comment.Comment', on_delete=models.CASCADE)
