# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define unfamiliar = Character("Незнакомец", color="#bdbdbd")
define hero = Character("Эдвард", color="#33bcce")

#define li = [2, 3, 5]

# Атрибуты персонажа
define reason = 100 # Рассудок
define power = 0 # Сила

# Количесто таблеток
define medicine_count = 2 

# Включение панели с помогательнами элементами
label enable_panel:
    show screen phone_button()
    show screen medicine_button()
    return

# Выключение панели с помогательнами элементами
label disable_panel:
    hide screen phone_button
    hide screen medicine_button
    return

# Повысить рассудок
label reason_up(summa):
    if(medicine_count < 0):
        $ reason += summa
        $ medicine_count -= 1
        $ renpy.notify("Ваш рассудок немного повысился")
    else:
        $ renpy.notify("У вас закончились таблетки")

# Кнопка телефона
screen phone_button():
    imagebutton:
        xalign 0.9
        yalign 0
        idle "images/gui/phone.png"
        hover "images/gui/phone_active.png"
        action [Show("info_panel")]

# Экран телефона с информацией о персонаже
screen info_panel():
    modal True
    frame:
        padding(10,10)
        xalign 0.5
        yalign 0.5
        vbox:
            xsize 460
            ysize 860
            text "Информация" xalign 0.5
            text "Имя: Александр"
            text "Рассудок: [reason]"
            text "Сила: [power]"
            textbutton "->" action Hide("info_panel") xalign 0.5

# Кнопка таблеток
screen medicine_button():
    imagebutton:
        xalign 0.95
        yalign 0
        idle "images/gui/medicine.png"
        # hover "images/gui/phone_active.png"
        action [Call("reason_up", 15)]