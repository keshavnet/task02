from django.urls import path
from . import views

app_name = 'imageuploader'
urlpatterns = [
    path('editPost/<str:post_id>/', views.editPost, name='editPost'),
    path('imageUpload/', views.post, name='post'),
    # path('imageDetails/', views.postDetails, name='postDetails'),
    path('postSuccessfully/', views.posted, name='posted'),
    path('update/<str:post_id>/', views.update, name='update'),
    path('imageList/', views.ImageList, name='imageList'),
]