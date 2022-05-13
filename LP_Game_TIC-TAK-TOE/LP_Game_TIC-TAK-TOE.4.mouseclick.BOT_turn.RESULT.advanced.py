# Game_TIC-TAK-TOE.4
# По нажатию ЛКМ добавляет на игровое поле крестик. Добавлет ход бота глупого бота методом random.choice().
# Так же добавлен искусственный интелект для умного бота.
# Добавлена информационная заставка.
# Добавлена клавиша завершения игры (Escape).
# Программа определяет победителя, ведет подсчет очков по завершению раунда в случае победы игрока,
# бота или когда ничья.
# Программа циклична и чередует ход игрока и бота с каждым новым раундом.
import canvas # модуль canvas работает на платформе https://letpy.com
import time
import random


def clear_screen():
    '''Начало/повтор'''
    # Очистка
    canvas.fill_style(colors[0])
    for r in range(30, 250, 10):
        canvas.fill_circle(175, 175, r)
        canvas.draw()

    # Смена первого хода
    tr_flag = trigger.pop(0)
    trigger.insert(0, (tr_flag + 1) % 2)
    trigger.pop()
    trigger.insert(1, tr_flag)

    # Полезная информация (подсказки)
    info_line = ("Your move", "Bot move", "Press 'Escape' to Exit")
    canvas.fill_style(colors[3]) 
    canvas.fill_text (info_line[tr_flag], 175, 180, "Monospace", 50, "center")
    canvas.fill_text (info_line[2], 175, 230, "Monospace", 20, "center")
    canvas.draw()
    time.sleep(3)
    canvas.clear()

    # Обнуление статуса игры
    for i in range(len(GAME_STATE)):
        GAME_STATE.pop(i)
        GAME_STATE.insert(i, None)
    draw_grid ()


def draw_grid():
    '''Отрисовка игрового поля'''
    canvas.line_width(1)
    canvas.set_color(colors[5])
    for x, y, x1, y1, in lpl:
        canvas.move_to(x, y)
        canvas.line_to(x1, y1)
    canvas.draw()


def draw_cross(poz):
    '''Отрисовка крестиков'''
    canvas.line_width(3)
    canvas.set_color(colors[8])
    x, y = lpp[poz]
    for ang in [45, 135, 225, 315]:
        canvas.radius_line(x, y, ang, 40)
    canvas.draw()


def draw_circ(poz):
    '''Отрисовка ноликов'''
    canvas.line_width(3)
    canvas.set_color(colors[4])
    x, y = lpp[poz]
    canvas.circle(x, y, 30)
    canvas.draw()


def draw_state(state):
    '''Отрисовка состояния игры'''
    for i in range(len(state)):
        if state[i] == "x":
            draw_cross (i)
        elif state[i] == "o":
            draw_circ (i)


def get_bot_move(gs):
    '''Глупый бот'''
    list_index_none, poz_bot = [], ""
    # Формирование списка пустых клеток
    for pn in range(len(gs)):
        if gs[pn] is None:
            list_index_none.append(pn)
    # Выбор случайной (рандомной) позиции
    if list_index_none:
        poz_bot = random.choice(list_index_none)
    return poz_bot


def get_smart_bot_move(gs, ts):
    '''Умный бот'''
    list_index_none, poz_bot = [], ""

    # Game point 'o'
    if ts["2o"] and len(ts["2o"]) == 2:
        cl_1, cl_2 = ts["2o"]
        var_cl = lcw[cl_1]
        poz_bot = var_cl[cl_2]
    elif ts["2o"] and len(ts["2o"]) == 1:
        win_line = ts["2o"].pop()
        for p in llw[win_line]:
            if gs[p] is None:
                poz_bot = p

    # Game point 'x'
    elif ts["2x"] and len(ts["2x"]) == 2:
        cl_1, cl_2 = ts["2x"]
        var_cl = lcw[cl_1]
        p = var_cl[cl_2]
        if gs[p] is None:
            poz_bot = p
        else:
            poz_bot = get_bot_move(gs)
    elif ts["2x"] and len(ts["2x"]) == 1:
        win_line = ts["2x"].pop()
        for p in llw[win_line]:
            if gs[p] is None:
                poz_bot = p

    # Захват центра
    elif gs[4] is None:
        poz_bot = 4

    # Потенциальный Game point 'o'
    elif ts["1o"] and len(ts["1o"]) == 2:
        cl_1, cl_2 = ts["1o"]
        var_cl = lcw[cl_1]
        p = var_cl[cl_2]
        if gs[p] is None:
            poz_bot = p
        else:
            poz_bot = get_bot_move(gs)

    # Потенциальный Game point 'x'
    elif ts["1x"] and len(ts["1x"]) == 2:
        cl_1, cl_2 = ts["1x"]
        var_cl = lcw[cl_1]
        p = var_cl[cl_2]
        if p and gs[p] is None:
            poz_bot = p
        else:
            poz_bot = get_bot_move(gs)

    # Случайный выбор
    else:
        # Углы
        corners = []
        for pn in [0, 2, 6, 8]:
            if gs[pn] is None:
                corners.append(pn)
        if corners:
            poz_bot = random.choice(corners)
        # Что осталось
        else:
            poz_bot = get_bot_move(gs)

    # Вернуть
    return poz_bot

          
def click (x, y):
    '''Объявляет о новом состоянии игры по позиции клика'''
    # Первый ход мой?
    try:
        cell = 1
        if trigger[1] == 0:
            # Определение позиции курсора
            for poz in lpp:
                if (poz[0]-58 < x < poz[0]+58) and (poz[1]-58 < y < poz[1]+58):
                    index_poz = lpp.index(poz)
            # Изменение статуса игры
            f_poz = GAME_STATE.pop(index_poz)
            if f_poz is None:
                GAME_STATE.insert(index_poz, "x")
                # Рисование крестика
                draw_state (GAME_STATE)
            # Клетка не пустая
            else:
                GAME_STATE.insert(index_poz, f_poz)
                print("Клетка не пустая.")
                cell = 0
            # Проверка победителя
            res, cross_2 = get_winner(GAME_STATE)
            if res is not None:
                fin_screen (res)
    # Попадание курсора в линию
    except UnboundLocalError:
        print("На линии.")
    else:
        if cell == 1:
            # Сброс флага
            trigger.pop(1)
            trigger.insert(1, 0)
            # Запуск бота
            res, cross_2 = get_winner(GAME_STATE)
            if res != "x win":
                # # Глупый бот
                # bot_poz = get_bot_move (GAME_STATE)
                # Умный бот
                bot_poz = get_smart_bot_move (GAME_STATE, cross_2)
                # Рисование нолика
                if bot_poz != "":
                    GAME_STATE.pop(bot_poz)
                    GAME_STATE.insert(bot_poz, "o")
                    draw_state (GAME_STATE)
                # Проверка победителя
                res, cross_2 = get_winner(GAME_STATE)
                if res is not None:
                    fin_screen (res)
    finally:
        pass


def get_winner (state):
    '''Определение победителя'''
    # Проверка линий

    # Формируем коды
    line_n = []
    for el in llw:
        st_num = ""
        for num in el:
            if state[num]:
                st_num += state[num]
        line_n.append(st_num)
        st_num = ""
    
    # Разбираем коды
    line_full, result = 0, ""
    two_cross = {"2x" : [], "2o" : [], "1x" : [], "1o" : []}
    for poz_l, kod in enumerate (line_n):
        if kod == "xxx":
            result = "x win"
            score[0] += 1
        elif kod == "ooo":
            result = "o win"
            score[2] += 1
        elif kod.count("x") == 1 and not ("o" in kod):
            two_cross["1x"].append(poz_l)
        elif kod.count("x") == 2 and not ("o" in kod):
            two_cross["2x"].append(poz_l)
        elif kod.count("o") == 1 and not ("x" in kod):
            two_cross["1o"].append(poz_l)
        elif kod.count("o") == 2 and not ("x" in kod):
            two_cross["2o"].append(poz_l)
        if len(kod) == 3:
            line_full += 1

    # Вывод результатов
    if not result and line_full == 8:
        result = "draw"
        score[1] += 1
    if result:
        return result, two_cross
    else:
        return None, two_cross


def fin_screen(rez):
    '''Обработка результатов проверки'''
    canvas.clear()
    messages = {"x win": "You win!", "o win": "You lose!", "draw": "Draw!"}
    canvas.fill_style(colors[1])
    canvas.fill_text("Game over", 175, 110,"Monospace", 24, "center")
    score_text = "Win-" + str(score[0]) + "  Draw-" + str(score[1]) + "  Lose-" + str(score[2])
    canvas.fill_text(score_text, 175, 258, "Monospace", 24, "center")
    canvas.fill_style(colors[0])
    canvas.fill_text(messages[rez], 180, 190, "Monospace", 48, "center")
    canvas.stroke_style(colors[2])
    canvas.stroke_text(messages[rez], 180, 190, "Monospace", 48, "center")
    canvas.draw()
    time.sleep (3)
    clear_screen ()
    draw_state (GAME_STATE)


EXIT = False
def key_down(key_code):
    '''Выход из игры'''
    global EXIT

    if key_code == "Escape":
        time.sleep(0.5)
        canvas.clear()
        canvas.fill_text("Goodbye!", 175, 195, "Arial", 50, "center")
        canvas.draw()
        EXIT = True


# Палитра
colors = ("White", "Black", "Red", "Green", "Blue", "Gray", "Brown", "Yellow", "Lime")

# Центры клеток 
lpp = [(58, 58), (175, 58), (292, 58),
       (58, 175), (175, 175), (292, 175),
       (58, 292), (175, 292), (292, 292)]

# Линии сетки
lpl = [(117, 0, 117, 350), (234, 0, 234, 350),
        (0, 117, 350, 117), (0, 234, 350, 234)]

# Выигрышные линии
llw = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
       (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# Пересечения выиграшных линий
lcw = [(None, None, None, 0, 1, 2, 0, 2), (None, None, None, 3, 4, 5, 4, 4),
       (None, None, None, 6, 7, 8, 8, 6), (0, 3, 6, None, None, None, 0, 6),
       (1, 4, 7, None, None, None, 4, 4), (2, 5, 8, None, None, None, 8, 2),
       (0, 4, 8, 8, 0, 4, None, 4), (2, 4, 6, 6, 4, 2, 4, None)]

# Нулевой статус игры
GAME_STATE = [None] * 9

# Запуск игры
# Заставка
canvas.fill_style(colors[6])
canvas.fill_text("TIC-TAK-TOE", 175, 150, "Courier", 50, "center")
canvas.stroke_text("The most intelligent", 175, 200, "Arial", 25, "center")
canvas.stroke_text("game in the world", 175, 240, "Arial", 25, "center")
canvas.draw()
time.sleep(3)

# Счет
score = [0,0,0]

# Первый ход
trigger = [0, 0]
clear_screen()

canvas.onclick(click)
canvas.onkey(key_down)

while canvas.listen(infinity=False):
    if not EXIT:
        continue
    break
