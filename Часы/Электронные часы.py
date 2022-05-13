# Электронные часы. Аналог точного времени в интернете.
import canvas # модуль canvas работает на платформе https://letpy.com
import datetime


while True:
    my_datetime = datetime.datetime.now()
    datetime_str = my_datetime.strftime("%H:%M:%S")
    canvas.clear()
    canvas.stroke_rect(40, 130, 260, 65)
    canvas.fill_text(datetime_str, 175, 175, align='center', size=40)
    canvas.draw()
