import cv2
import numpy

def effect_image(path):
    #Pencil Sketch and Cartoon Effects 
    img = cv2.imread(path)
    height = img.shape[0]
    width = img.shape[1]

    print("====== Image Effects ======")
    print("1. Pencil Sketch Effect")
    print("2. Cartoon Effect")
    
    option = int(input("Enter your option: "))

    if option == 1:
        #Black and white pencil sketch effect

        new_img = numpy.zeros(img.shape, img.dtype)
        img1 = numpy.zeros(img.shape, img.dtype)
        for x in numpy.arange(height): 
            for y in numpy.arange(width):
                grey = img[x,y,0]*0.11 + img[x,y,1]*0.59 + img[x,y,2]*0.3
                img[x,y,0] = grey 
                img[x,y,1] = grey
                img[x,y,2] = grey
                img1[x,y] = img[x,y]
        k = 25
        img2 = cv2.GaussianBlur(img1,(k,k),0)
        new_img = cv2.divide(img1,img2,scale = 256)
        cv2.imwrite('results/pic_sketch.jpg', new_img)
        print("File created: pic_sketch.jpg")

    elif option == 2:
        #Cartoon Effect
        
        new_img = numpy.zeros(img.shape, img.dtype)
        img1 = numpy.zeros(img.shape, img.dtype)
        new_img = cv2.pyrDown(img)
        new_img = cv2.pyrDown(new_img)
        new_img = cv2.bilateralFilter(new_img,9,55,55)
        new_img = cv2.pyrUp(new_img)
        new_img = cv2.pyrUp(new_img)
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img1 = cv2.medianBlur(img1,5).astype('uint8')
        img2 = cv2.adaptiveThreshold(img1, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,29,5)
        img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
        new_img = cv2.bitwise_and(new_img,img2)
        
        cv2.imwrite('results/pic_cartoon.jpg', new_img)
        print("File created: pic_cartoon.jpg")

    else:
        print("Input out of range. Please enter either 1 or 2")