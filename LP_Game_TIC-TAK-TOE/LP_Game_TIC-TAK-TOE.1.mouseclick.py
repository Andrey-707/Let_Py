# Game_TIC-TAK-TOE.1
# По нажатию ЛКМ добавляет на игровое поле крестик.
import canvas # модуль canvas работает на платформе https://letpy.com


def draw_state(GAME_STATE):
    '''Рисует состояние игры'''
    canvas.line_width(6)
    x, y = 58, 58
    for i in GAME_STATE:
        if i == "o":
            canvas.set_color("green")
            canvas.circle(x, y, 30)
        if i == "x":
            canvas.set_color("blue")
            for i in range(45, 316, 90):
                canvas.radius_line(x, y, i, 40 )
        x += 116
        if x > 300:
            x = 58
            y += 116
    canvas.draw()


def click(x, y):
    '''Объявляет о новом состоянии игры по позиции клика'''
    a = 3 * (y // 116) + (x // 116)
    GAME_STATE[a] = "x"
    draw_state(GAME_STATE)


# объявляем начальное состояние игры
GAME_STATE = [None, None, None, None, None, None, None, None, None]

# рисуем игровое поле
canvas.set_color("grey") # установить BG

for i in range(0, 350, 116): # геометрия
    canvas.move_to(i, 0)
    canvas.line_to(i, 350)
    canvas.move_to(0, i)
    canvas.line_to(350, i)
canvas.draw() # нарисовать

canvas.set_onclick(click)
canvas.listen()
