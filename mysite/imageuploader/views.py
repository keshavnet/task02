from django.shortcuts import render
from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage

from .models import ImageUpload

# Create your views here.


def post(request):

    return render(request, 'imageuploader/imageUpload.html')


def postDetails(request):
    image = []
    return render(request, 'imageuploader/imageDetails.html',
                  {'image': image})

# def posted(request):
#         print('-------------------------------------')
#         print(request.POST['image_name'])
#         print(request.POST.get('image'))

#         image_url =
#         image_name = request.POST['image_name']
#         image_des = request.POST['image_des']

#         image = ImageUpload(name=image_name, description=image_des)
#         image.save()
#         return HttpResponse('Posted successfully!!!')


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
        
#     return render(request, 'core/simple_upload.html')


def ImageList(request):
    image_list = ImageUpload.objects.all()
    print('-------------------------------')
    print(image_list)

    for e in image_list:
        print('name name name', e.name)
        print('url url url', e.actual)

    return render(request, 'imageuploader/imageList.html', {'image_list': image_list})
