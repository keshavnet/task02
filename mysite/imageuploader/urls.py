from django.urls import path
from . import views

app_name = 'imageuploader'
urlpatterns = [
    path('editPost/<:postId>/', views.editPost, name='editPost'),
    path('imageUpload/', views.post, name='post'),
    path('imageDetails/', views.postDetails, name='postDetails'),
    path('postSuccessfully/', views.posted, name='posted'),
    path('imageList/', views.ImageList, name='imageList'),
]