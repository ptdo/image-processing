import cv2
import numpy

def apply_filer(img, filter_to_apply, alpha=0.85, beta=0.15):
    new_img = numpy.zeros(img.shape, img.dtype)
    for x in numpy.arange(img.shape[0]):
        for y in numpy.arange(img.shape[1]):
            new_img[x,y] = filter_to_apply
    new_img = cv2.addWeighted(img, alpha, new_img, beta, 0)
    return new_img

def filter_image(path):

    img = cv2.imread(path)
    height = img.shape[0]
    width = img.shape[1]
    
    print("====== Image Filters ======")
    print("1. Adjust Contrast and Brightness")
    print("2. Greyscale Filter")
    print("3. Color Filter")
    print("4. Dithering Filter")
    print("5. Median Filter")
    print("6. Thermal Filter")
    print("7. Invert Filter")
    
    option = int(input("Enter option: "))
    
    if option == 1:
        #Contrast & Brightness
        new_img = img
        #from 1.0 - 3.0, type: float 
        a = float(input("Enter contrast value: "))
        #from 0-100, type: int
        b = int(input("Enter brightness value: "))
    
        for x in numpy.arange(height): 
            for y in numpy.arange(width):
                new_img[x,y] =  numpy.clip(a*new_img[x,y]+b,0,255)
        cv2.imwrite('results/pic_contrast.jpg', new_img)
        print("File created: pic_contrast.jpg")

    elif option == 2:
        #Greyscale Filter
        new_img = img
        for x in numpy.arange(height): 
            for y in numpy.arange(width):
                grey = img[x,y,0]*0.11 + img[x,y,1]*0.59 + img[x,y,2]*0.3
                new_img[x,y,0] = grey 
                new_img[x,y,1] = grey
                new_img[x,y,2] = grey
        
        cv2.imwrite('results/pic_greyscale.jpg', new_img)
        print("File created: pic_greyscale.jpg")

    elif option == 3:
        #Color Filter
        print("====== Color Filter ======")
        print("1. Red Filter")
        print("2. Green Filter")
        print("3. Blue Filter")
        print("4. Yellow Filter")
        print("5. Cyan Filter")
        print("6. Magenta Filter")
        print("7. Grey Filter")
        print("8. Custom Filter")
        
        color = int(input("Enter your option: "))
        if color == 1:
            filter = (0,0,255)
            new_img = apply_filer(img, filter)
            cv2.imwrite('results/pic_red.jpg', new_img)
            print("File created: pic_red.jpg")
        elif color == 2:
            filter = (0,255,0)
            new_img = apply_filer(img, filter)
            cv2.imwrite('results/pic_green.jpg', new_img)
            print("File created: pic_green.jpg")
        elif color == 3:
            filter = (0,0,255)
            new_img = apply_filer(img, filter)
            cv2.imwrite('results/pic_blue.jpg', new_img)
            print("File created: pic_blue.jpg")
        elif color == 4:
            filter = (255,255,0)
            new_img = apply_filer(img, filter)
            cv2.imwrite('results/pic_yellow.jpg', new_img)
            print("File created: pic_yellow.jpg")
        elif color == 5:
            filter = (0,255,255)
            new_img = apply_filer(img, filter)
            cv2.imwrite('results/pic_cyan.jpg', new_img)
            print("File created: pic_cyan.jpg")
        elif color == 6:
            filter = (255,0,255)
            new_img = apply_filer(img, filter)
            cv2.imwrite('results/pic_magenta.jpg', new_img)
            print("File created: pic_magenta.jpg")
        elif color == 7:
            filter = (105,105,105)
            new_img = apply_filer(img, filter)
            cv2.imwrite('results/pic_grey.jpg', new_img)
            print("File created: pic_grey.jpg")
        elif color == 8:
            filter = (0,0,0)
            r = int(input("Enter R code: "))
            g = int(input("Enter G code: "))
            b = int(input("Enter B code: "))
            filter = list(filter)
            filter[0] = r
            filter[1] = g
            filter[2] = b
            filter = tuple(filter)
            new_img = apply_filer(img, filter, 0.7, 0.3)
            cv2.imwrite('results/pic_color.jpg', new_img)
            print("File created: pic_color.jpg")
        else:
            print("Input out of range. Please enter a number from 1 to 7")

    elif option == 4:
        #Dithering Filter
        #Ref: https://en.wikipedia.org/wiki/Dither
        #Ref2: https://stackoverflow.com/questions/55874902/floyd-steinberg-implementation-python

        new_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for x in range(0, height-1):
            for y in range(0, width-1):
                old = new_img[x,y]
                new = 0
                if old>128:
                    new = 255
                quant_error = old - new
        
                new_img[x,y+1] = new_img[x,y+1] + quant_error*7/16
                if new_img[x,y+1] < 0:
                    new_img[x,y+1] = 0
                if new_img[x,y+1] > 255:
                    new_img[x,y+1] = 255

                if y>0:
                    new_img[x+1,y-1] = new_img[x+1,y-1] + quant_error*3/16
                    if new_img[x+1,y-1] < 0:
                        new_img[x+1,y-1] = 0
                    if new_img[x+1,y-1] > 255:
                        new_img[x+1,y-1] = 255
        
                new_img[x+1,y] = new_img[x+1,y] + quant_error*5/16
                if new_img[x+1,y] < 0:
                    new_img[x+1,y] = 0
                if new_img[x+1,y] > 255:
                    new_img[x+1,y] = 255

                new_img[x+1,y+1] = new_img[x+1,y+1] + quant_error*1/16
                if new_img[x+1,y+1] < 0:
                    new_img[x+1,y+1] = 0
                if new_img[x+1,y+1] > 255:
                    new_img[x+1,y+1] = 255

        cv2.imwrite('results/pic_dithering.jpg', new_img)
        print("File created: pic_dithering.jpg")

    elif option == 5:
        #Median Filter

        img = cv2.imread(path)
        new_img = numpy.zeros(img.shape, img.dtype)
        k = numpy.ones((5,5), numpy.float32)/25
        new_img = img
        new_img = cv2.filter2D(new_img,-1,k)
        cv2.imwrite('results/pic_median.jpg', new_img)
        print("File created: pic_median.jpg")

    elif option == 6:
        #Thermal Filter
        
        height = img.shape[0]
        width = img.shape[1]
        new_img = img
       
        for x in numpy.arange(height): 
            for y in numpy.arange(width):
                if new_img[x,y,2] == 0:
                    new_img[x,y,2] = 0
                elif new_img[x,y,2] > 0 and new_img[x,y,2] <= 64:
                    new_img[x,y,2] = 70
                elif new_img[x,y,2] > 64 and new_img[x,y,2] <= 128:
                    new_img[x,y,2] = 140
                elif new_img[x,y,2] > 128 and new_img[x,y,2] <= 192:
                    new_img[x,y,2] = 210
                elif new_img[x,y,2] > 128 and new_img[x,y,2] <= 256:
                    new_img[x,y,2] = 256
                else:
                    new_img[x,y,2] = new_img[x,y,2]

                if new_img[x,y,0] == 0:
                    new_img[x,y,0] = 0
                elif new_img[x,y,0] > 0 and new_img[x,y,0] <= 64:
                    new_img[x,y,0] = 30
                elif new_img[x,y,0] > 64 and new_img[x,y,0] <= 128:
                    new_img[x,y,0] = 80
                elif new_img[x,y,0] > 128 and new_img[x,y,0] <= 192:
                    new_img[x,y,0] = 120
                elif new_img[x,y,0] > 128 and new_img[x,y,0] <= 256:
                    new_img[x,y,0] = 192
                else:
                    new_img[x,y,0] = new_img[x,y,0]

        new_img = cv2.cvtColor(new_img,cv2.COLOR_BGR2HSV)
        
        for x in numpy.arange(height): 
            for y in numpy.arange(width):
                if new_img[x,y,1] == 0:
                    new_img[x,y,1] = 0
                elif new_img[x,y,1] > 0 and new_img[x,y,1] <= 64:
                    new_img[x,y,1] = 70
                elif new_img[x,y,1] > 64 and new_img[x,y,1] <= 128:
                    new_img[x,y,1] = 140
                elif new_img[x,y,1] > 128 and new_img[x,y,1] <= 192:
                    new_img[x,y,1] = 210
                elif new_img[x,y,1] > 128 and new_img[x,y,1] <= 256:
                    new_img[x,y,1] = 256
                else:
                    new_img[x,y,1] = 256

        cv2.imwrite('results/pic_thermal.jpg', new_img)
        print("File created: pic_thermal.jpg")
    
    elif option == 7:
        #Invert Filter

        new_img = img
        for x in numpy.arange(height): 
            for y in numpy.arange(width):
                new_img[x,y,0] = 255 - new_img[x,y,0]
                new_img[x,y,1] = 255 - new_img[x,y,1]
                new_img[x,y,2] = 255 - new_img[x,y,2]
        cv2.imwrite('results/pic_invert.jpg', new_img)
        print("File created: pic_invert.jpg")

    else:
        print("Input out of range. Please enter number from 1 to 4")