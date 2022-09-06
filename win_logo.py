
from turtle import begin_fill, bgcolor, color, done, end_fill, goto, pendown, penup, speed, width, write
import time
speed(1)
bgcolor("black")
penup()
goto(-50, 60)
pendown()
color('blue')
begin_fill()
goto(100, 100)
goto(100, -100)

goto(-50, -80)
goto(-50, 60)
end_fill()

# bu yerda penup() yozmaslig uchun pendown() yozish uchun
penup()
goto(-50, -20)

pendown()
color("black")
width(10)
goto(100, 0)

penup()
goto(30, 100)

pendown()
color("black")
goto(25, -100)

penup()
goto(-50, -20)

# time.sleep(2)
# bgcolor("white")

done()


