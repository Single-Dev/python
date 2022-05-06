import random 
import time as vaqt
sorov = "ha"
while sorov =="ha":
    compchoice = random.randint(0, 999)
    print("Diqqat !\nDiqqat !\nRaqam tanlash uchun 0dan katta 999dan kichik son tanlang ‼ \naks holda siz tanlagan son 0ga tenglashtiriladi")
    humanchoice = int(input("eng baland uch xonali son tanlang = "))
    if humanchoice > 999:
        humanchoice = 0
    elif humanchoice < 0:
        humanchoice = 0
    if humanchoice > compchoice:
        print(f"natijalar hioblanmoqda siz {humanchoice}ni tanladingiz bot esa {compchoice}ni tanladi")
        vaqt.sleep(1)
        print("Siz yutdungiz")
    elif humanchoice < compchoice:
        print(f"natijalar hioblanmoqda siz {humanchoice}ni tanladingiz bot esa {compchoice}ni tanladi")
        vaqt.sleep(2)
        print(f"Siz yutqazdingiz")
    else:
        print(f"natijalar hioblanmoqda siz {humanchoice}ni tanladingiz bot esa {compchoice}ni tanladi")
        vaqt.sleep(1)
        print("Do`stlik g`alaba qozondi")
    sorov = input("O`yinni to`xtatish uchun biron nima kiriting \nYana o`ynashni hohlaysizmi? ")
print("o`yin to`xtatildi")
