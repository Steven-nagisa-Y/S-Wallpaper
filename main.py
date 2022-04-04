# -*- coding:utf-8 -*-
# Author: Steven Yan

import time
import os
import sys
import requests
import win32api
import win32con
import win32gui
from PIL import Image


def getUrl():
    myUrl = "https://stevenos.com/api/bing"
    return myUrl


def downloadPic(picUrl):
    print("Downloading picture from StevenOS.com...\n")
    try:
        req = requests.get(picUrl)
        with open("pyDesktopPic.jpg", "wb") as ccc:
            ccc.write(req.content)
        print("Picture saved at TEMP dir.\n")
    except:
        print("Can't download Picture!\n")
        print("Check your Internet access and try again.")
        goodBye()


def moveFile(file, des):
    if not os.path.isfile(file):
        print(file+" is not exist")
        print("Please contact me@StevenOS.com")
        goodBye()
    else:
        if not os.path.exists(des):
            os.makedirs(des)
        else:
            os.system("move /y "+file+" "+des)
            print("\n")


def convPic(jpg, bmp):
    try:
        img = Image.open(jpg)
        img.save(bmp, 'BMP')
        os.remove(jpg)
        print("The picture was converted successfully.")
    except BaseException as e:
        print(e)


def setWallpaper(picUri):
    key = win32api.RegOpenKeyEx(
        win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, picUri, 1+2)
    print("\n->>TODAY Wallpaper set!!!")


def printMe():
    print("##########################################################")
    print("##                 Website: StevenOS.com                ##")
    print("##                     By Steven Yan                    ##")
    print("##########################################################")


def goodBye():
    print("\nGood Bye! See you next time!\n")
    for i in range(1, 4):
        print("-> %s" % str(4-i))
        time.sleep(1)
    sys.exit(0)


if __name__ == "__main__":
    if not os.name == "nt":
        print("This Program only supports Windows")
        sys.exit(1)
    else:
        os.system("mode con cols=60 lines=30")
        os.system("color 0e")
        os.system("title Daily Wallpaper Changer from StevenOS.com")
        printMe()
    print("Now: %s \n" % time.ctime())
    tempDir = os.getenv('TEMP')
    print("Your TEMP dir is: "+tempDir+"\n")
    print("Note: cleaning out "+tempDir+" will delete the wallpaper file")
    time.sleep(1)
    downloadPic(getUrl())
    moveFile("pyDesktopPic.jpg", tempDir)
    convPic(tempDir+"\pyDesktopPic.jpg", tempDir+"\pyDesktopPic.bmp")
    time.sleep(1)
    setWallpaper(tempDir+"\pyDesktopPic.bmp")
    goodBye()
