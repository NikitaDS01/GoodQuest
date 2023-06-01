# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define unfamiliar = Character("Незнакомец", color="#f58080")
define hero = Character("Эдвард", color="#33bcce")

# Атрибуты персонажа
define reason = 100 # Рассудок
define power = 0 # Сила

# Количесто таблеток
define medicine_count = 2 

# Музыка и звуки 
define audio.backrooms = "music/CryOfTheUnheard.mp3"

# Включение панели с помогательнами элементами
label enable_panel:
    show screen phone_button()
    return

# Выключение панели с помогательнами элементами
label disable_panel:
    hide screen phone_button
    return

# Повысить рассудок
label reason_up(summa):
    if(medicine_count > 0):
        if(reason+summa <= 100):
            $ reason += summa
            $ medicine_count -= 1
            $ renpy.notify("Ваш рассудок немного повысился")
        else:
            $ renpy.notify("Вы чувствуете себя прекрасно")
    else:
        $ renpy.notify("У вас закончились таблетки")

# Кнопка телефона
screen phone_button():
    imagebutton:
        xalign 0.95
        yalign 0
        idle "images/gui/phone.png"
        hover "images/gui/phone_active.png"
        action [Show("info_panel")]

# Экран телефона с информацией о персонаже
screen info_panel():
    modal True
    frame:
        background "images/gui/phone_panel.png"
        padding(10,10)
        xalign 0.3
        yalign 0.1
        vbox:
            xsize 600
            ysize 860
            # text "Информация" xalign 0.5 yalign 0.9
            text "Имя: [hero]" xalign 0.5 yalign 0.5
            text "Рассудок: [reason]"  xalign 0.5
            text "Сила: [power]"  xalign 0.5
            text "Количество таблеток: [medicine_count]"  xalign 0.5
            textbutton "Принять таблетки" action Function(reason_up, 15) xalign 0.5
            textbutton "->" action Hide("info_panel") xalign 0.5
