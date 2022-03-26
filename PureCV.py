import pyautogui
import pyscreenshot as ImageGrab
import cv2
import numpy as np
import time

def FindResource():
    first_x = -1
    first_y = -1
    last_x = -1
    file_with_path = "tmp.png"
    im = ImageGrab.grab(bbox=(0, 0, 1920, 1080),backend="mss", childprocess=False)
    im.save(file_with_path)
    im = cv2.imread(file_with_path)
    print("converting to grayscale")
    im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    #!!!!!!!! REcolor first 20 height pixels
    print("Start recoloring window frame")
    height, width= im.shape
    for i in range(0,50):
        for j in range(0,width):
            im[i,j] = 0

    for i in range(600, 1080):
        for j in range(0, width):
            im[i, j] = 0

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in range(0,height):
        for j in range(0,width):
            if im[i,j]==255:
                first_y=i+3
                first_x=j
                print("Founded First pixel")
            else:
                im[i, j] = 0
        if first_x!=-1 and first_y!= -1:
            break
    print("!!!!!!!!!!!!!!!!!!!")
    for i in range(1919,0,-1):

        if im[first_y,i]==255:
            last_x = i
            print("Founded right end pixel")
            break

    if first_x!=-1 and first_y!= -1 and last_x!= -1:
        print("Founded Resource")
        print("first x= ", first_x , " first y= ", first_y ," last x= ",last_x)


        center_x = first_x+((last_x -first_x)/2)-6
        center_y = first_y
        print("Start Digging")
        pyautogui.moveTo(center_x,center_y)
        pyautogui.click()
        cv2.imwrite(file_with_path,im)
        return True
    else:
        return False


count_of_digging=0

info_string =""
try:

    while True:

        print("Resource Count = " ,count_of_digging)
        print("Searching for Resource")
        is_finded = FindResource()
        if is_finded:
            print("Sleeping till digging")
            count_of_digging+=1

            time.sleep(15)
        else:
            print("Sleeping till resource will respawn")
            time.sleep(60)
except :
    print("Got Exception... sleeping for 20 seconds")
    time.sleep(20)





