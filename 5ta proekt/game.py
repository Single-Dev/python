import random 
import time as vaqt
sorov = "ha"
dan = 0
gacha = 999

while sorov =="ha":
    compchoice = random.randint(dan, gacha)
    print(f'Diqqat ! !\nRaqam tanlash uchun {dan}dan katta {gacha}dan kichik son tanlang ‼ \naks holda siz tanlagan son 0ga tenglashtiriladi')
    humanchoice = int(input("eng baland uch xonali son tanlang = "))
    if humanchoice > gacha:
        humanchoice = 0
    elif humanchoice < 0:
        humanchoice = 0
    if humanchoice > compchoice:
        
        vaqt.sleep(1)
        print("👌✌️🥳🥳Siz yutdungiz")
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
