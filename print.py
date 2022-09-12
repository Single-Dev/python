from time import sleep
import os

mb=100

for i in range(mb):
   sleep(0.1)
   print(f"{i/mb*100:.1f} % shuncha yuklandi.", end="\r")

# for windows terminal clear
os.system('cls')
