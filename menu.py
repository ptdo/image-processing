import sys

from effects import effect_image
from resize import resize_image
from filters import filter_image

def menu(path):
    
    print("==========Menu==========")
    print("1. Resize Image")
    print("2. Apply Filters On Image")
    print("3. Apply Effects On Image")
    print("4. Exit")
    
    option = int(input("Please enter an option: "))

    if option == 1:
        resize_image(path)
        menu(path)
    elif option == 2:
        filter_image(path)
        menu(path)
    elif option == 3:
        effect_image(path)
        menu(path)
    elif option == 4:
        sys.exit(0)        
    else:
        print("Input out of range. Please enter number from 1 to 4")


if __name__=="__main__":
    path = 'tests/test.jpg'
    menu(path)