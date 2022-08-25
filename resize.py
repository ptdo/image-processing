import cv2

def resize_image(path):
    # Changing image size by factors and by custom size entered by user
    # This will go from 4k to 2k, FHD or HD
    # This function will retain the 16:9 aspect ratio as the resizing is done by factors and not by pixels

    img = cv2.imread(path)
    height = img.shape[0]
    width = img.shape[1]

    print("====== Resize ======")
    print("Base image is in 4K quality, you can can choose a factor to reduce the size")
    print("1. 2560*1440. This is 2K quality image")
    print("2. 1920*1080. This is FHD quality image")
    print("3. 1280*720. This is HD quality image")
    print("4. Custom resolution")

    option = int(input("Please enter your option:  "))

    if option == 1:
        img1 = cv2.resize(img, (2560, 1440), interpolation=cv2.INTER_AREA)
        cv2.imwrite('results/pic_2k.jpg', img1)
        print("File created: pic_2k.jpg")

    elif option == 2:
        img2 = cv2.resize(img, (width / 2, height / 2), interpolation=cv2.INTER_AREA)
        cv2.imwrite('results/pic_fhd.jpg', img2)
        print("File created: pic_fhd.jpg")


    elif option == 3:
        img3 = cv2.resize(img, ( width / 3, height / 3), interpolation=cv2.INTER_AREA)
        cv2.imwrite('results/pic_hd.jpg', img3)
        print("File created: pic_hd.jpg")
    
    elif option == 4:
        h = int(input("Enter custom height: "))
        w = int(input("Enter custom width: "))
        img4 = cv2.resize(img, (w , h), interpolation=cv2.INTER_AREA)
        cv2.imwrite('results/pic_custom.jpg', img4)
        print("File created: pic_custom.jpg")

    else:
        print("Input out of range. Please enter number from 1 to 4")