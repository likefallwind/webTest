from django.shortcuts import render
from .models import ImageModel
import cv2
from django.conf import settings
from IPython import embed
import os
from django.core.files import File 

def index(request):
    return render(request,"index.html")
# Create your views here.
#@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        new_img = ImageModel(
            imageFile=request.FILES.get('img'),
            imageName = request.POST['imgName']
        )
        new_img.save()
    imgs = ImageModel.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print(i.imageFile.url)
    return render(request, 'showing.html', content)

def changeImgStyle(imgStyle, imgSrc, imgDst):
    #embed()
    net = cv2.dnn.readNetFromTorch('models/starry_night.t7')
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    #embed()
    imgDst = os.path.join(settings.BASE_DIR, imgDst).replace('\\', '/')
    imgSrc = os.path.join(settings.BASE_DIR, imgSrc).replace('\\', '/')
    print(imgSrc)
    print(imgDst)

    image = cv2.imread(imgSrc)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)
    net.setInput(blob)
    out = net.forward()
    out = out.reshape(3, out.shape[2], out.shape[3])
    out[0] += 103.939
    out[1] += 116.779
    out[2] += 123.68
    out /= 255
    out = out.transpose(1, 2, 0)    
    cv2.imwrite(imgDst,out * 255)
    #cv2.imencode('.jpg', out * 255)[1].tofile(imgDst) 
    return

def  getAndChangeImg(request):
    if request.method == 'POST':
        new_img = ImageModel(
            imageFile=request.FILES.get('img'),
            imageName = request.POST['imgName']
        )
        new_img.save()
        imgDst = 'media/changeImg/' + request.POST['imgName'] + '.jpg'
        allDst = os.path.join(settings.BASE_DIR, imgDst).replace('\\', '/')
        #embed()
        changeImgStyle(0, new_img.imageFile.url[1:], imgDst)
        tmpFile = File(open(allDst, 'rb'))
        #embed()
        new_img.changeImageFile.save(request.POST['imgName'], tmpFile)
        #embed()
        new_img.save()
        content = {
            'originalUrl':new_img.imageFile.url,
            'changeUrl':new_img.changeImageFile.url,
            'imageName':new_img.imageName,
        }
        return render(request, 'changeImage.html', content)    
    return render(request,"index.html")

#@csrf_exempt
def showImg(request):
    imgs = ImageModel.objects.all()
    content = {
        'imgs':imgs,
    }
    for i in imgs:
        print(i.imageFile.url)
    return render(request, 'showing.html', content)