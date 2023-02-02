import cv2
import os

image_path = './data/SD301/images/latent/png/'
save_path = './slap/'

images = os.listdir(image_path)

for image in images:
    img = cv2.imread(save_path + image, 0)
    
    s = max(img.shape)
    
    if s < 512:
        s = 512

    bottom = (s-img.shape[0])//2
    left = (s-img.shape[1])//2

    if (s-img.shape[0])%2 != 0:
        top = bottom + 1
    else:
        top = bottom
    if (s-img.shape[1])%2 != 0:
        right = left + 1
    else:
        right = left
        
    img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, None, value = 255)

    img = cv2.resize(img, (512,512),cv2.INTER_LANCZOS4)

    cv2.imwrite('./r/'+image,img)