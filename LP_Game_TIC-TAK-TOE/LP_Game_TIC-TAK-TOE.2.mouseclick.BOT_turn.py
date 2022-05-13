# Game_TIC-TAK-TOE.2
# По нажатию ЛКМ добавляет на игровое поле крестик. Добавлет ход бота методом random.choice().
import canvas # модуль canvas работает на платформе https://letpy.com
import random


def draw_element(x, y, element):
    '''Отрисовка крестиков и ноликов'''
    canvas.line_width(5)
    if element == "o":
        canvas.set_color("Green")
        canvas.circle(x, y, 30)
    elif element == "x":
        canvas.set_color("Blue")
        canvas.radius_line(x-30, y-30, 135, 84)
        canvas.radius_line(x-30, y+30, 45, 84)
    canvas.draw()


def draw_state(grid_state):
    '''Отрисовка состояние игры'''
    # Центровка
    center = {
        0:(58,58),
        1:(174,58),
        2:(290,58),
        3:(58,174),
        4:(174,174),
        5:(290,174),
        6:(58,290),
        7:(174,290),
        8:(290,290)
        }

    for position,element in enumerate(grid_state):
        if element != None:
            x,y = center[position]
            draw_element(x,y, element)


def draw_grid():
    '''Отрисовка игрового поля'''
    canvas.move_to(116,0)
    canvas.line_to(116,350)
    canvas.move_to(232,0)
    canvas.line_to(232,350)
    canvas.move_to(0,116)
    canvas.line_to(350,116)
    canvas.move_to(0,232)
    canvas.line_to(350,232)
    canvas.draw()


def get_bot_move(GAME_STATE):
    '''Ход бота'''
    open_squares = []
    try:
        for i,val in enumerate(GAME_STATE):
            if val == None:
                open_squares.append(i)
        return random.choice(open_squares) 
    except IndexError:
        return None


def click(x, y):
    '''Объявляет о новом состоянии игры по позиции клика'''
    global GAME_STATE
    # Ход игрока
    sq_pos = (y//116) * 3 + (x//116)
    if GAME_STATE[sq_pos] == None:
        GAME_STATE[sq_pos] = 'x'
        draw_state(GAME_STATE)
        # Ход бота
        bot_move = get_bot_move(GAME_STATE)
        if bot_move != None:
            GAME_STATE[bot_move] = 'o'
            draw_state(GAME_STATE)
        else:
            print("No more moves. Game is over")
    elif GAME_STATE.count(None) > 0:
        print("Not empty. Try again") # Нажатие на заполненную клетку. 


# объявляем начальное состояние игры
GAME_STATE = [None,None,None,None,None,None,None,None,None]

# рисуем игровое поле
draw_grid()

canvas.set_onclick(click)
canvas.listen()
