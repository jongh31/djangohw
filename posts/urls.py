from django.urls import path
from . import views as views

urlpatterns = [
    path('post_list/', views.post_list_view, name = "post_list"),
    path('post_create/', views.post_create, name = "post_create"),
    path('<int:post_id>/delete//', views.post_delete, name = "post_delete"),
    path('<int:post_id>/post_detail/', views.post_detail, name = "post_detail"),
]