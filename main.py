# -*- coding:utf-8 -*-
# Author: Steven Yan

from os import path, system, makedirs, remove, name, getenv
from time import sleep, ctime
from sys import exit
from requests import get as Get
from PIL import Image
from win32api import RegOpenKeyEx, RegSetValueEx
from win32con import HKEY_CURRENT_USER, KEY_SET_VALUE, REG_SZ, SPI_SETDESKWALLPAPER
from win32gui import SystemParametersInfo


def getUrl():
    myUrl = "https://stevenos.com/api/bing"
    return myUrl


def downloadPic(picUrl):
    print("Downloading picture from StevenOS.com...\n")
    try:
        req = Get(picUrl)
        with open("DO-NOT-MOVE-pyDesktopPic.jpg", "wb") as ccc:
            ccc.write(req.content)
        print("Picture saved at TEMP dir.\n")
    except:
        print("Can't download Picture!\n")
        print("Check your Internet access and try again.")
        goodBye()


def moveFile(file, des):
    if not path.isfile(file):
        print(file+" is not exist")
        print("Please contact me@StevenOS.com")
        goodBye()
    else:
        if not path.exists(des):
            makedirs(des)
        else:
            system("move /y "+file+" "+des)
            print("\n")


def convPic(jpg, bmp):
    try:
        img = Image.open(jpg)
        img.save(bmp, 'BMP')
        remove(jpg)
        print("The picture was converted successfully.")
    except BaseException as e:
        print(e)


def setWallpaper(picUri):
    key = RegOpenKeyEx(
        HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, KEY_SET_VALUE)
    RegSetValueEx(key, "WallpaperStyle", 0, REG_SZ, "10")
    RegSetValueEx(key, "TileWallpaper", 0, REG_SZ, "0")
    SystemParametersInfo(SPI_SETDESKWALLPAPER, picUri, 1+2)
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
        sleep(1)
    exit(0)


if __name__ == "__main__":
    if not name == "nt":
        print("This Program only supports Windows")
        exit(1)
    else:
        system("mode con cols=60 lines=30")
        system("color 0e")
        system("title Daily Wallpaper Changer from StevenOS.com")
        printMe()
    print("Now: %s \n" % ctime())
    tempDir = getenv('TEMP')
    print("Your TEMP dir is: "+tempDir+"\n")
    print("Note: cleaning out "+tempDir+" will delete the wallpaper file\n")
    downloadPic(getUrl())
    moveFile("DO-NOT-MOVE-pyDesktopPic.jpg", tempDir)
    convPic(tempDir+"\DO-NOT-MOVE-pyDesktopPic.jpg",
            tempDir+"\DO-NOT-MOVE-pyDesktopPic.bmp")
    setWallpaper(tempDir+"\DO-NOT-MOVE-pyDesktopPic.bmp")
    goodBye()
