from django.shortcuts import render
from models import ImageModel

def index(request):
    return render(request,"index.html")
# Create your views here.
def uploadImg(request):
    if request.method == 'POST':
        new_img = ImageModel(
            imageFile=request.FILES.get('img'),
            imageName = request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'img_tem/uploadimg.html')