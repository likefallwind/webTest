import cv2
import os
import numpy as np


def changeImgStyle(imgStyle, imgSrc, imgDst):
    #embed()
    #net = cv2.dnn.readNetFromTorch('models/starry_night.t7')
    print(imgStyle)
    net = cv2.dnn.readNetFromTorch(imgStyle)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    #embed()
    imgDst = imgDst.replace('\\', '/')
    imgSrc = imgSrc.replace('\\', '/')
    print(imgSrc)
    print(imgDst)
    #embed()
    img_resize(imgSrc)

    image = cv2.imdecode(np.fromfile(imgSrc,dtype=np.uint8),-1)
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

def img_resize(imageSrc, width_new = 1280, height_new = 720):
    img = cv2.imdecode(np.fromfile(imageSrc,dtype=np.uint8),-1)
    height, width = img.shape[0], img.shape[1]
    if width / height > width_new / height_new:
        newHeight = int(height * width_new / width)
        newWidth = width_new
    else:
        newHeight = height_new
        newWidth = int(width * height_new / height)
    img_new = cv2.resize(img, (newWidth, newHeight))
    print(img_new.shape)
    #cv2.imwrite(imageSrc, img_new)
    cv2.imencode('.jpg', img_new)[1].tofile(imageSrc)
    return