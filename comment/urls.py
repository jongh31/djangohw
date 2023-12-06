from django.urls import path
from . import views as views

urlpatterns = [
    path('<int:post_id>/create/', views.comment_create, name = "comment_create"),
    path('<int:post_id>/delete/<int:comment_id>/', views.comment_delete, name = "comment_delete"),
]