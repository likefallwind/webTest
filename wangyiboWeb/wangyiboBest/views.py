from django.shortcuts import render
from .models import ImageModel

def index(request):
    return render(request,"index.html")
# Create your views here.
#@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        new_img = ImageModel(
            imageFile=request.FILES.get('img'),
            imageName = request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'uploadimg.html')

#@csrf_exempt
def showImg(request):
    imgs = ImageModel.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print(i.imageFile.url)
    return render(request, 'showing.html', content)