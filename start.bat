@echo off
title Program Starter
%1 %2
ver|find "5.">nul&&goto :main
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :main","","runas",1)(window.close)&goto :eof
:main
	cls
	mode con cols=60 lines=20
	color 06
	echo ##########################################################
	echo ##                                                      ##
	echo ##  This Batch Program is to set a program run at start ##
	echo ##                                                      ##
	echo ##                There are many choices                ##
	echo ##                                                      ##
	echo ##        You can just drag your file into here         ##
	echo ##                                                      ##
	echo ##                 Website: StevenOS.com                ##
	echo ##                       By Steven                      ##
	echo ##########################################################
	pause
:ch
	echo ##########################################################
	echo ##   1, Add Program path to Registry (Very good)        ##
	echo ##   2, Add program to scheduled task (Normal)          ##
	echo ##   3, Add program to Right-Click (Nice)               ##
	echo ##########################################################
	echo.
	echo Pleas enter your choice
	set /p a= :
	set /p src= Program path:
	set /p name= Key Name (Important):
	if %a%==1 goto addReg
	if %a%==2 goto addSchtask
	if %a%==3 goto rc
	echo Not good.&pause&goto ch
:addReg
	reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v %name% /d %src% /f
	pause&goto main
:addSchtask
	echo.
	echo CAUTION: Time formatted like this: 10:10:00 
	set /p ttt= What time do you want to change your Wallpaper: 
	schtasks /create /tn %name% /ru system /tr %src% /sc DAILY /st %ttt%
	pause&goto main
:rc
	echo.
	echo Right-Click desktop, you can click "%name%" to change your wallpaper manually.
	echo.
	pause
	reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\%name%" /f
	reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\%name%\command" /f
	reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\%name%\command" /ve /d "%src%" /f
	pause&goto main