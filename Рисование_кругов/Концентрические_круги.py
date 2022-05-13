# Концентрические_круги
'''
Напишите программу, которая рисует на холсте концентрические круги с центром в точке
(175, 175) и радиусами от 7 до 180. Шаг изменения радиуса должен быть равен 7.

Результатом работы программы должен быть такой вот рисунок

"Тут образец рисунка"

Для рисования круга нужно использовать функцию .circle() модуля canvas

canvas.circle(x, y, radius)
Если радиус делится на 2 без остатка — цвет круга должен быть красным, иначе — серым. Для
смены цвета используйте функцию .set_color() модуля canvas.

Для переключения на красный цвет пишите так:
canvas.set_color("Red") 

а для переключения на серый — так:
canvas.set_color("Grey") 

В программе обязательно используйте цикл for и функцию range
'''
# Вариант_1.Пограмма отрисует круги с каждым вызовом итерации (функция .draw() вызывается каждый раз).
import canvas # модуль canvas работает на платформе https://letpy.com


x = 175
y = 175
radius = 7

for r in range(radius, 180, radius):
    if r % 2 == 0:
        canvas.set_color("Red")
        canvas.circle(x, y, r)
        canvas.draw()
    else:
        canvas.set_color("Grey") 
        canvas.circle(x, y, r)
        canvas.draw()

# Вариант_2.Пограмма отрисует ВСЕ круги сразу (функция .draw() вызывается один раз).
import canvas # модуль canvas работает на платформе https://letpy.com


x = 175
y = 175
radius = 7

for r in range(radius ,180 ,radius):
    if r % 2 == 0:
        canvas.set_color("Red")
    else:
        canvas.set_color("Grey") 
    canvas.circle(x, y, r)
canvas.draw()
