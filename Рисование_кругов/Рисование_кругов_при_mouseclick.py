# Рисование_кругов_при_mouseclick
import canvas # модуль canvas работает на платформе https://letpy.com
import time


def my_click(x, y):
    print("Нажата ЛКМ!")
    canvas.set_color("Black")
    canvas.line_width(6)
    canvas.circle(x, y, r)
    canvas.fill_style("Green")
    canvas.fill_circle(x, y, r)
    canvas.draw()
    time.sleep(0.1)
    canvas.clear()

def my_click2(x, y):
    print("Нажата ПКМ!")
    canvas.reset()

r = 15

canvas.set_onclick(my_click)
canvas.onrightclick(my_click2)
canvas.listen()
