# Game_TIC-TAK-TOE.3
# По нажатию ЛКМ добавляет на игровое поле крестик. Добавлет ход бота методом random.choice().
# Определяет победителя, выводит надпись "x win" или "o win" в консоль
import canvas # модуль canvas работает на платформе https://letpy.com
import random


def draw_state(GAME_STATE):
    '''Отрисовка состояние игры'''
    canvas.line_width(6)
    x, y = 58, 58
    for i in GAME_STATE:
        if i == "o":
            canvas.set_color("green")
            canvas.circle(x, y, 30)
        if i == "x":
            canvas.set_color("blue")
            for i in range(45, 316, 90):
                canvas.radius_line(x, y, i, 40)
        x += 116
        if x > 300:
            x = 58
            y += 116
    canvas.draw()


def click(x, y):
    '''Объявляет о новом состоянии игры по позиции клика'''
    c = 3 * (y // 116) + (x // 116)
    if GAME_STATE[c] is None:
        GAME_STATE[c] = "x"
        s = get_bot_move(GAME_STATE)
        if s:
            GAME_STATE[s] = "o"
        draw_state(GAME_STATE)
        print(get_winner(GAME_STATE))


def get_bot_move(GAME_STATE):
    '''Ход бота'''
    a, b = [], 0
    for i in GAME_STATE:
        if i is None:
            a.append(b)
        b += 1
    if a:
        return(random.choice(a))


def get_winner(a):
    '''Определение победителя'''
    for i in ["x", "o"]:
        # По горизонтали: 0-1-2, 3-4-5, 6-7-8 
        if a[0: 3] == [i, i, i] or a[3: 6] == [i, i, i] or a[6: 9] == [i, i, i]:
            return(i + " win")
        # по вериткали 0-3-6
        elif a[0] == a[3] == a[6] == i:
            return(i + " win")
        # по вериткали 1-4-7
        elif a[1] == a[4] == a[7] == i:
            return(i + " win")
        # по вериткали 2-5-8    
        elif a[2] == a[5] == a[8] == i:
            return(i + " win")
        # по диагонали 0-4-8    
        elif a[0] == a[4] == a[8] == i:
            return(i + " win")
        # по диагонали 2-4-6    
        elif a[2] == a[4] == a[6] == i:
            return i + " win"
    if None in a:
            return None
    else:
        return "draw"


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