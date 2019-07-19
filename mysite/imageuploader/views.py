from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage

from .models import ImageUpload

# Create your views here.


def post(request):

    return render(request, 'imageuploader/imageUpload.html')


# def postDetails(request):
#     image = ImageUpload.objects.get()

#     return render(request, 'imageuploader/imageDetails.html', {'image': image})


def posted(request):
    #     if request.method == 'POST' and request.FILES['myfile']:
    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    image_url = fs.url(filename)

    path = str(image_url)

    image_name = ''
    image_des = ''

    image = ImageUpload(actual=path, name=image_name, description=image_des)
    image.save()
    print('----------------------------------')
    print('image_url ', path, type(path))

    return HttpResponse('Posted successfully!!!')


def update(request, post_id):
    post = ImageUpload.objects.get(pk=post_id)
    print('---------------------------------', request.POST)
    # if request.POST['myfile']:
    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    image_url = fs.url(filename)
    path = str(image_url)

    post.actual = path

    print('image_url ', image_url)

    post.name = request.POST['image_name']
    post.description = request.POST['image_des']
    post.save()
    print('updated')
    return HttpResponse('Post updated successfully!')


def editPost(request, post_id):
    post = ImageUpload.objects.get(pk=post_id)
    print('----------------------- post ', post.name)
    print('post edited successfully!!!!!!!!!', post_id)

    return render(request, 'imageuploader/editPost.html', {'post_detail': post})


def ImageList(request):
    image_list = ImageUpload.objects.all()
    return render(request, 'imageuploader/imageList.html', {'image_list': image_list})
