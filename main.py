# -*- coding:utf-8 -*-
# Author: Steven Yan

import time, os
import requests
import win32api, win32gui, win32con
from PIL import Image


tempDir = ""


def getUrl():
    # month0 = time.strftime("%Y%m",time.localtime())
    # today0 = time.strftime("%d",time.localtime())
    # myUrl = "https://stevenos.com/home/"+month0+"/"+today0+".jpg"
    myUrl = "http://stevenos.com/home/bing.php"
    return myUrl

def downloadPic(picUrl):
    print("Downloading picture from StevenOS.com...\n")
    try:
        req = requests.get(picUrl)
        with open("DONT-MOVE-S-Wallpaper-Pic.jpg","wb") as ccc:
            ccc.write(req.content)
        print("Picture saved at: {}\n".format(tempDir + "\\DONT-MOVE-S-Wallpaper-Pic.jpg"))
    except:
        print("Can't download Picture!\n")
        print("Check your Internet access and try again.")
        goodBye()

def moveFile(file,des):
    if not os.path.isfile(file):
        print(file + " is not exist.")
        print("DON'T MOVE or DELETE picture file!!!")
        goodBye()
    else:
        if not os.path.exists(des):
            os.makedirs(des)
        else:
            os.system("move /y "+file+" "+des)
        
def convPic(jpg,bmp):
    try:
        img = Image.open(jpg)
        img.save(bmp, 'BMP')
    except:
        print("Can't convert picture.")
        goodBye()
        return
    os.remove(jpg)
    print("The picture has been converted successfully.")

def setWallpaper(picUri):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "10") 
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, picUri, 1+2)
    print("\n  --> TODAY Wallpaper has been set!!!")

def printMe():
    print("##########################################################")
    print("##                 Website: StevenOS.com                ##")
    print("##                     By Steven Yan                    ##")
    print("##########################################################")
    
def goodBye():
    print("\n  Good Bye! Program will exit soon!\n")
    for i in range(3):
        print("-> %s" % str(3-i))
        time.sleep(1)
    exit(0)

if __name__ == "__main__":
    if not os.name == "nt":
        print("This Program only supports Windows")
        exit(1)
    else:
        os.system("mode con cols=60 lines=30")
        os.system("color 0e")
        os.system("title Daily Wallpaper from StevenOS.com")
        printMe()
    print("\nNow: %s \n" % time.ctime())
    tempDir = os.getenv('TEMP')
    print("Your TEMP dir is: " + tempDir + "\n")
    downloadPic(getUrl())
    moveFile("DONT-MOVE-S-Wallpaper-Pic.jpg",tempDir)
    convPic(tempDir + "\\DONT-MOVE-S-Wallpaper-Pic.jpg", tempDir + "\\DONT-MOVE-S-Wallpaper-Pic.bmp")
    time.sleep(1)
    setWallpaper(tempDir + "\\DONT-MOVE-S-Wallpaper-Pic.bmp")
    goodBye()
