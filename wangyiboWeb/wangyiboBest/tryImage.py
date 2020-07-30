import cv2

def img_resize(imageSrc, width_new = 1280, height_new = 720):
    img = cv2.imread(imageSrc)
    height, width = img.shape[0], img.shape[1]
    if width / height > width_new / height_new:
        newHeight = int(height * width_new / width)
        newWidth = width_new
    else:
        newHeight = height_new
        newWidth = int(width * height_new / height)
    img_new = cv2.resize(img, (newWidth, newHeight))
    print(img_new.shape)
    cv2.imwrite(imageSrc, img_new)

a = img_resize('a.jpg')