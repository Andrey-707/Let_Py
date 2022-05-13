# Движение квадрата по периметру. Рамка.
import canvas # модуль canvas работает на платформе https://letpy.com
import time


tab = 15
max_x = 350 - tab
max_y = 350 - tab
square_x = 50
square_y = 50
x = tab
y = tab
delta = 2
count = 0

while True:
    # canvas.clear() # если раскоментировать, то фигура не оставляет след на холсте
    canvas.stroke_rect(x, y, square_x, square_y)
    canvas.draw()
    time.sleep(0.01)

    if y == tab and x < max_x - square_x:
        x += delta
    elif x == tab:
        y -= delta
    elif y == max_y - square_y:
        x -= delta
    elif x == max_x - square_x:
        y += delta

    count += 1
    if count > (max_x - square_x) + (max_y - square_y) - tab*2:
        break
