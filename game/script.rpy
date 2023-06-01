# Вы можете расположить сценарий своей игры в этом файле.

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
init:
    $ topLeft = Position(xalign=0.2, yalign=1.5) 
    $ topright = Position(xalign=1.2, yalign=1.5) 
    $ inventory = Inventory()
    

label start:
    show bg cellar
    "Дисклеймер" '''
    В игре много всякой хуйни, много матов и многого другого. {w=3}
    Поэтому акуратнее :D
    '''

    unfamiliar '''
    *Идёт на физ-ру*
    
    "Что за голос в голове?"
    '''
    "Ещё больший незнакомец" "Иди к углу комнаты"

    unfamiliar "Ок"
    unfamiliar "*Этот чел реально взял предмет в углу комнаты.*"
    
    hide bg
    with fade 

    jump hero_room

    return    

label hero_room:
    scene bg herous_room

    hero '''
    Ебать что за утро гавно?!
    
    Пойду в шарагу. {w=3}Надо только взять телефон.
    '''

    call enable_panel

    # $ renpy.notify()

    menu:
        "Проебать пары":
            jump died
        "Пойти на пары":
            jump run_school
        "Ждать друга":
            jump backrooms
        
    return

label died:
    hero "Нахуй мне шарага. {w=3}Там нифега интересного нет."

    $ reason = 0

    $ renpy.notify("Ваш рассудок упал до критической отметки "+str(reason))
    hero "Мне как-то плохо стало"

    call disable_panel

    "Вы умерли от рака жопы"
    
    return

label run_school:
    hero "*Выходит из свой комнаты*"
    show bg school_rain:
        zoom 2.0
    hero '''
    Почему такая фиговая погода?
    
    И у меня нет даже зонтика...

    Ну что делать, {w=3} пойду так.
    '''
    #call enable_panel
    hero "пздц"
    jump run_school
    return

label backrooms:
    hero "Буду этого пиздюка ждать"
    play music backrooms
    scene bg backrooms:
        zoom 2.0
    call disable_panel
    hero "Где я?"