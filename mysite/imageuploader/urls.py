from django.urls import path
from . import views

urlpatterns = [
    path('imageUpload/', views.post, name='post'),
    path('imageDetails/', views.postDetails, name='postDetails'),
    path('postSuccessfully/', views.posted, name='posted'),
    path('imageList/', views.ImageList, name='imageList')
]