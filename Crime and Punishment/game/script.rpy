﻿# Определение персонажей игры.
define r = Character('Раскольников', color="#CD5C5C")
define s = Character('Рассказчик', color="#E0FFFF")
define m1 = Character('Мужчина', color="#FFFFE0")
define m2 = Character('Девушка', color="#D8BFD8")
define v1 = Character('Голос 1', color="#D8BFD8")
define v2 = Character('Голос 2', color="#87CEEB")
define off = Character('Офицер', color="#191970")
define stud = Character('Студент', color="#B8860B")
define sis = Character('Сестра', color="#FF4500")
define author = Character('Автор', color="#E0FFFF")
define marf = Character('Марфа', color="#FA8072")

# Игра начинается здесь:
label start:
    stop music
    scene pismo
    with Fade(1,1,1)
    s "Действия будут происходить во мрачном, немного отдающим желтизной Петербурге."
    s "В этом городе живёт Родион Раскольников."
    s "Студент юридического университета, который находится в крайне скудном финансовом положении."
    s "Родион не ел уже 2 дня."
    s "Он должен хозяйке квартиры крупную сумму."
    s "Поэтому решил заложить часы."
    scene out
    with Dissolve(0.5)
    show rask_s:
        xalign 0.0
        yalign 1.0
    s "В квартале стоит невыносимая вонь."
    s "Она вызывает у Раскольникова отвращение."
    s "По дороге он обдумывает дело."
    show rask_s:
        xalign 0.10
        yalign 1.0
    s "Которое уже долго не даёт ему покоя."
    s "Родион хочет убить жадную старуху процентщицу."
    show rask_s:
        xalign 0.25
        yalign 1.0
    r "*Эта старуха кровопийца всем жизнь портит.*"
    r "*От её действий наш город погружается во мрак.*"
    show rask_s:
        xalign 0.50
        yalign 1.0
    r "*Делать что то таких масштабов могут только “Право имеющие”.*"
    r "*Вроде Наполеона*"
    show rask_s:
        xalign 0.80
        yalign 1.0
    r "*А кто же тогда я?*"
    r "*Я тварь дрожащая или право имею?*"
    scene lombard
    with Fade(1,1,1)
    show rask_s:
        xalign 0.25
        yalign 1.0
    s "Пока студент обдумывал это всё, уже дошел до ломбарда."
    s "Заложив часы, он выдвинулся обратно."
    s "Мысль никак не могла его отпустить."

    scene out
    with Fade(1,1,1)
    show rask_sr:
        xalign 0.90
        yalign 1.0
    r "*А если всё таки проверить?*"
    r "*Если я всё таки не тварь дрожащая.*"
    show rask_sr:
        xalign 0.75
        yalign 1.0
    r "*То я смогу изменить этот…*"

    m2 "ДА ТЫ НИКЧЁМНЫЙ!"
    m2 "Я ВЫШЛА ЗА ТЕБЯ ИЗ БЕЗЫСХОДНОСТИ!"
    m2 "ТЫ ЧЕРТОВ ПЬЯНИЦА!"

    m1 "НЕ КРИЧИ ТЫ ТАК!"
    m1 "ТЕБЯ ДАЖЕ НА УЛИЦЕ СЛЫШАТ!"
    m1 "ПЕРЕЙДИ НА СПОКОЙНЫЙ ТОН!"

    r "*Эти Мармеладовы снова скандалят на всю улицу.*"
    show rask_sr:
        xalign 0.50
        yalign 1.0
    r "*Отец пьяница.*"
    r "*Мать безработная.*"
    show rask_sr:
        xalign 0.35
        yalign 1.0
    r "*Дочь, в попытках заработать, вообще подалась в простигосподи.*"
    r "*Это точный пример дрожащих тварей.*"
    show rask_sr:
        xalign 0.15
        yalign 1.0
    r "*Завтра я обязан проверить себя!*"

    scene pismo
    with Dissolve(1)
    s "За своими мыслями Родион не заметил как оказался дома."
    s "Бегло прочитав письмо от матери и не запомнив ни слова, лег спать."
    scene pismo
    with Fade(1,1,1)
    s "На утро Родион решает немного подготовиться и пройтись по улицам."
    
    r "Надо бы подготовиться и постараться что то узнать."

    s "Он выходит из дома и пройдя совсем немного, садиться под дерево."
    s "Раскольников засыпает."

    r "Что?Где я?"
    r "Фух…Я всего то задремал."

    v1 "Да, моя сестра процентщица."
    v1 "Я завтра уйду почти на весь день, не могли бы вы немного присмотреть за домом?"

    v2 "Да, без проблем"

    v1 "Спасибо большое."

    r "Точно, подготовиться."

    s "Наш “Герой” отправился домой и уже поднимаясь к себе домой, он подслушал разговор офицера с другим студентом."

    off "Эта старуха последние деньги из людей тащит!"

    stud "Да! Она всем жизнь портит!"

    off "Я вообще считаю, что с такими делишками, она и жизни не достойна!"

    stud "Согласен с вами!"

    off "Да на её деньги можно половине города помочь!"

    r "*Эта старушка даже офицеров достала…*"
    
    s "Раскольникова сильно взволновали слова офицера и он приступил к подготовке."
    s "Он крадет топор."
    s "Пришивает к подкладке пальто петлю для него."
    s "И достаёт папиросочницу, которая должна отвлечь старуху."
    s "На следующий день Раскольников выходит из дома сам не свой."
    s "С диким волнением он приходит к старушке и старается действовать даже под гнётом волнения."

    r "*Тварь я дрожащая или право имею?!?!?!*"
    r "*Смогу ли я сейчас это сделать?!?!?!*"
    r "*Смогу ли оборвать чью то жизнь?!?!?!?*"

    s "Немного замешкавшись, студент дважды ударяет процентщицу топором."

    r "*Я смог, я право имею, я не тварь дрожащая!!!!*"
    r "*Порадуюсь немного позже, а сейчас мне нужны деньги.*"

    s "Пока наш “Герой” набивает карманы драгоценностями и деньгами, возвращается сестра старушки."

    sis "Что?! Кто ты такой?! Что ты сделал с моей сестрой?!?!"

    r "*Что? Её же весь день не должно быть!!!!*"

    s "В растерянности Раскольников убивает сестру старушки."
    s "Совершив преступление, он поспешно направляется домой."
    s "Возвращает топор в дворницкую и впадает в забытье."
    s "Проснувшись утром, Родион проверяет всю свою одежду и прячет ценное в дыру под обоями."

    "*Стуr*"

    off "Родион Раскольников здесь проживает?"

    r "Да, это я"

    off "Вас вызывают в участок."

    r "Хорошо, сегодня приду."

    s "Этот разговор заставил нашего “Героя” подняться и отправиться в участок."
    s "Как оказалось, от него требовалась только расписка об аренде."
    s "Так же Раскольников услышал разговор об убийстве старухи и упал в обморок."
    s "К его счастью все посчитали, что он нездоров и отпустили."
    s "Испугавшись Родион переложил всё награбленное во двор под камень и впал в бред."
    s "Очнувшись спустя 3 дня, Раскольников узнает, что к товарищу трижды приходил офицер и расспрашивал о вещах Раскольникова"
    s "Он получил денежный перевод от матери на оплату жилья и узнал,что в убийстве подозревают красильщика Миколу"

    author "На этом и закончится наше путешествие по этому чудному произведению."
    author "Если хотите прочитать его полностью, ознакомьтесь  с одноименным произведением Ф.М.Достоевского"
    author "Могу так же предложить прочитать альтернативный сюжет."
    author "В нём немного ломается прывычный смысл, но он может удивить"
    author "Хотите прочитать альтернативу?"
    menu:
        "Да, хочу!":
            jump alt_story
        "Нет, спасибо).":
            return


label alt_story:

    scene pismo
    with Fade(1,1,1)
    s "Действия будут происходить во мрачном, немного отдающим желтизной Петербурге."
    s "В этом городе живёт Родион Раскольников."
    s "Студент юридического университета, который находится в крайне скудном финансовом положении."
    s "Родион не ел уже 2 дня."
    s "Он должен хозяйке квартиры крупную сумму."
    s "Поэтому решил заложить часы."
    scene out
    with Dissolve(0.5)
    show rask_s:
        xalign 0.0
        yalign 1.0
    s "В квартале стоит невыносимая вонь."
    s "Она вызывает у Раскольникова отвращение."
    s "По дороге он обдумывает дело."
    show rask_s:
        xalign 0.10
        yalign 1.0
    s "Которое уже долго не даёт ему покоя."
    s "Родион хочет убить жадную процентщицу."
    show rask_s:
        xalign 0.25
        yalign 1.0
    r "*Эта кровопийца всем жизнь портит.*"
    r "*От её действий наш город погружается во мрак.*"
    show rask_s:
        xalign 0.50
        yalign 1.0
    r "*Делать что то таких масштабов могут только “Право имеющие”.*"
    r "*Вроде Наполеона*"
    show rask_s:
        xalign 0.80
        yalign 1.0
    r "*А кто же тогда я?*"
    r "*Я тварь дрожащая или право имею?*"
    scene lombard
    with Fade(1,1,1)
    show rask_s:
        xalign 0.25
        yalign 1.0
    s "Пока студент обдумывал это всё, уже дошел до ломбарда."
    s "Заложив часы, он выдвинулся обратно."
    s "Мысль никак не могла его отпустить."

    scene out
    with Fade(1,1,1)
    show rask_sr:
        xalign 0.90
        yalign 1.0
    r "*А если всё таки проверить?*"
    r "*Если я всё таки не тварь дрожащая.*"
    show rask_sr:
        xalign 0.75
        yalign 1.0
    r "*То я смогу изменить этот…*"

    m2 "ДА ТЫ НИКЧЁМНЫЙ!"
    m2 "Я ВЫШЛА ЗА ТЕБЯ ИЗ БЕЗЫСХОДНОСТИ!"
    m2 "ТЫ ЧЕРТОВ ПЬЯНИЦА!"

    m1 "НЕ КРИЧИ ТЫ ТАК!"
    m1 "ТЕБЯ ДАЖЕ НА УЛИЦЕ СЛЫШАТ!"
    m1 "ПЕРЕЙДИ НА СПОКОЙНЫЙ ТОН!"

    r "*Эти Мармеладовы снова скандалят на всю улицу.*"
    show rask_sr:
        xalign 0.50
        yalign 1.0
    r "*Отец пьяница.*"
    r "*Мать безработная.*"
    show rask_sr:
        xalign 0.35
        yalign 1.0
    r "*Дочь, в попытках заработать, вообще подалась в простигосподи.*"
    r "*Это точный пример дрожащих тварей.*"
    show rask_sr:
        xalign 0.15
        yalign 1.0
    r "*Завтра я обязан проверить себя!*"

    scene pismo
    with Dissolve(1)
    s "За своими мыслями Родион не заметил как оказался дома."
    s "Бегло прочитав письмо от матери и не запомнив ни слова, лег спать."
    scene pismo
    with Fade(1,1,1)
    s "На утро Родион решает немного подготовиться и пройтись по улицам."
    
    r "Надо бы подготовиться и постараться что то узнать."

    s "Он выходит из дома и пройдя совсем немного, садиться под дерево."
    s "Раскольников засыпает."

    r "Что?Где я?"
    r "Фух…Я всего то задремал."

    v1 "Да, моя сестра процентщица."
    v1 "Я завтра уйду почти на весь день, не могли бы вы немного присмотреть за домом?"

    v2 "Да, без проблем"

    v1 "Спасибо большое."

    r "Точно, подготовиться."

    s "Наш “Герой” отправился домой и уже поднимаясь к себе, он подслушал разговор офицера с другим студентом."

    off "Эта девчушка последние деньги из людей тащит!"

    stud "Да! Она всем жизнь портит!"

    off "Я вообще считаю, что с такими делишками, она и жизни не достойна!"

    stud "Согласен с вами!"

    off "Да на её деньги можно половине города помочь!"

    r "*Она даже офицеров достала…*"
    
    s "Раскольникова сильно взволновали слова офицера и он приступил к подготовке."
    s "Он крадет топор."
    s "Пришивает к подкладке пальто петлю для него."
    s "И достаёт папиросочницу, которая должна отвлечь."
    s "На следующий день Раскольников выходит из дома сам не свой."
    s "С диким волнением он приходит к процентщице и старается действовать даже под гнётом волнения."

    "*ТУК**ТУК*"

    marf "Кто там?"

    r "Родион Раскольников"

    marf "А, Родион, секунду."
 
    "*Марфа открывает дверь*"

    marf "Заходи."
    marf "Ну рассказывай, зачем пришел?"

    r "Я тут немного деньжат скопил…"
    r "Не напомнишь сколько я ещё должен?"

    marf "Без проблем."
    marf "Сейчас, только блокнот найду."

    r "*Тварь я дрожащая или право имею?!?!?!*"
    r "*Смогу ли я сейчас это сделать?!?!?!*"
    r "*Смогу ли оборвать чью-то жизнь?!?!?!?*"

    s "Немного замешкавшись, студент дважды махает топором."
    s "Но из-за промедления оба раза пролетели по воздуху"
    s "Девушка отскочила"

    marf "Какого?!?!?!??!"
    marf "Ты чего это удумал?!?!?!?!?"

    s "Раскольников махнул топором ещё раз и снова мимо."

    r "*Неужели я настолько слаб?*"
    r "*Не может быть…*"
    r "*Я сильнее, чем кажусь!*"

    marf "Ты совсем с ума сошёл?"

    s "Родион махнул топором в последний раз перед тем, как получить удар вилкой в живот."

    marf "Ты думал меня можно просто прийти и убить?"
    marf "*Подхватывает вилку со столика и бьёт студента в живот*"

    r "*Что..?*"
    r "*Что это за чувство..?*"
    r "*Почему всё такое мутное и ужасно болит живот…?*"
    r "*Глаза закрываются…*"
    r "*Я не могу это остановить…*"

    s "Раскольников упал замертво."
    s "Марфа хорошо всё продумала"
    s "Спрятала тело"
    s "Оставила следы краски на плаще"
    s "И хорошенько прибрала улики."
    s "В конечном итоге, в убийстве обвинили красильщика Миколу."

    author "На этом и закончится наше путешествие по этому чудному произведению."
    author "Если хотите прочитать его оригинал, ознакомьтесь  с одноименным произведением Ф.М.Достоевского"
    author "Поздравляю с полным прохождением!"
    author "Если хотите можете пройти ещё раз любую из версий или выйтию"
    menu:
        "Перепройти оригинал.":
            jump start
        "Перепройти альтернативу.":
            jump alt_story
        "Выход":
            return






    return
