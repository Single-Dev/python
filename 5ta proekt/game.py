import random 
import time as vaqt
sorov = "ha"
while sorov =="ha":
    compchoice = random.randint(0, 999)
    humanchoice = int(input("eng baland uch xonali son tanlang = "))
    if humanchoice > compchoice:
        print(f"natijalar hioblanmoqda siz {humanchoice}ni tanladingiz bot esa {compchoice}ni tanladi")
        vaqt.sleep(1.2)
        print("Siz yutdungiz")
    elif humanchoice < compchoice:
        print(f"natijalar hioblanmoqda siz {humanchoice}ni tanladingiz bot esa {compchoice}ni tanladi")
        vaqt.sleep(1.2)
        print(f"Siz yutqazdingiz \n Siz botdan kichik son tanladingiz bot tanlagan son {compchoice}")
    else:
        print(f"natijalar hioblanmoqda siz {humanchoice}ni tanladingiz bot esa {compchoice}ni tanladi")
        vaqt.sleep(1)
        print("Do`stlik g`alaba qozondi")
    sorov = input("Yana o`ynashni hohlaysizmi? ")
print("o`yin to`xtatildi")
