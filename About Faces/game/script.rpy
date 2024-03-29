﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define nika = Character('Ника', color="#808080")
define author = Character('Автор', color="ffffff")
define alice = Character('Алиса', color="ff9900")
define sava = Character('Сава', color="95565f")
# define nurse = Caharacter('Медсестра', color="f0768b")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре

# Игра начинается здесь:
label start:
    stop music fadeout 1
    play music "ambient.mp3" fadeout 1
    scene author
    with Dissolve(1)
    author "Здравствуй, человек!"
    author "Я автор, всего лишь плод чьего-то воображения."
    author "Я здесь что бы объяснить некоторые обозначения."
    author "Например *, обозначает мысли персонажа."
    author "К примеру: *Наконец-то!*."
    author "А скобки () обозначают какие-либо действия."
    author "К примеру: (Поднялась)"
    menu quest1:

        author "Всё понятно?"

        "Да":
            jump choice1_yes

        "Нет":
            jump choice1_no

    label choice1_yes:
        author "Прекрасно"
        jump choice1_done
    label choice1_no:
        author "Окей, давай ещё раз"
        author "Например *, обозначает мысли персонажа."
        author "К примеру: *Наконец-то!*."
        author "А скобки () обозначают какие-либо действия."
        author "К примеру: (Поднялась)"
        jump quest1
    label choice1_done:
        author"Ещё увидимся"
        author"Приятной игры!"
label story:
    window hide
    scene bg room
    with Dissolve(1)
    play music "ambient.mp3" fadeout 1
    window show
    show nika:
        xalign 1.00
        yalign 1.00
    nika "*Ну здравствуй, очередной бесполезный день.*"
    nika "*Мой абсолютно пустой взгляд в потолок спровождался звуками собственного тяжёлого дыхания.*"
    nika "*Грудная клетка, казалось, весила тонну, а веки и того больше.*"
    nika "*Зачем я только проснулась? Всё равно планов нет.*"
    nika "*Ни на сегодня, ни на завтра, ни даже на неделю вперед.*"
    nika "*Зачем просыпаться, если день пройдёт мимо? Зачем есть, если не чувствуешь вкуса? Зачем?*"
    nika "*Ну, наверное надо жить.*"
    nika "*Хотя, кому это надо?*"
    nika "*И зачем?*"
    nika "*Небесный создатель наверняка забыл отсыпать мне хоть капельку своего желания миротворствовать.*"
    nika "*Белый потолок кажется таким родным и мягким.*"
    nika "*Одеяло, простыни...*"
    nika "*Все это кажется таким родным.*"
    nika "*Кажется, я сливаюсь в единое целое с этой мягкостью и теплотой.*"
    nika "*Наверное, в куске ткани с наполнителем больше смысла, чем в каждом моем вздохе.*"
    nika "*А вот мысли...*"
    nika "*Мыслей у меня много*"
    nika "*Они переплетаются, а иногда и текут вместе, неся за собой спутники моих эмоций и действий.*"
    nika "*Да, пожалуй это так*"
    scene depht
    with Dissolve(3)
    nika "*В мыслях весь смысл*"
    nika "*В мыслях смысл*"
    nika "*В смыслях мысл*"
    nika "*В мыле...*"
    nika "*В мыслях...*"
    nika "*Вместо белого потолка перед глазами встала кромешная тьма. Уютно.*"
    nika "*Вес моих век и притягаельность тёплой постели достигли своего апогея*"
    nika "*Нет, нет... не хочу... что угодно, только не этот мир*"
    nika "*С каждым новым глотком воздуха я набирала в лёгкие ненависть и отвращение к этому миру*"
    nika "*Становилось тошно от представления новых лиц перед собой*"
    nika "*А впрочем, почему только новых?*"
    nika "*Меня тошнило даже от старых лиц, мест, действий и голосов*"
    nika "*Но вместе с этими мыслями рядом текли и следующие*"
    nika "*Мне некуда деваться. Придётся встать*"
    window hide
    scene bg room
    with Dissolve(2)
    nika "*Эта мысль быстро привела меня в чувства*"
    nika "*Перевернуться на другой бок стоило мне нечеловеческих усилий*"
    "(Села и взяла телефон в руки)"
    nika "*А сесть, открыть глаза в полную силу и взять в руки телефон...*"
    nika "*Пожалуй, это был величайший подвиг из всех, что я совершала*"
    nika "*Экран телефона так неестественно и радостно светил мне в лицо, что тут же захотелось его выключить*"
    nika "*Уведомлений было не так уж и много*"
    nika "*Но мне больше и не нужно*"
    nika "*Пара сообщений, пара новостей*"
    nika "*Все это резко контрастировало с мыслями о значении бытия и казалось смехотворно несущественным*"
    nika "*Казалось, что если я начну об этом думать, то прогоню все мысли уровня мирового масштаба*"
    nika "*Видимо, я слишком люблю мыслить*"
    stop music fadeout 1
    play music "room.mp3" fadeout 1
    nika "*Опять забыла, что я вообще-то собиралась начать жить сегодняшний день*"
    nika "*А что надеть-то?*"
    "(Приоткрывает окно)"
    "На улице солнечно"
    "Ни намёка на тучи"
    nika "*Лицо обдаёт приятный прогретый воздух*"
    nika "*Не люблю я такое*"
    nika "*Был бы дождь*"
    nika "*Осталасть бы дома*"
    nika "*Оденусь по стандарту*"
    "(Открывает шкаф)"
    nika "*Футболка и застиранные джинсы вполне подойдут*"
    "(Убирая волосы с лица, пошла умываться)"
    window hide
    scene bath
    with Dissolve(1)
    show nika:
        xalign 1.00
        yalign 1.00
    window hide
    ""
    window show
    nika "*Звук воды, раздражает и успокаивает одновременно*"
    nika "*Засохшие следы грязной воды, от вчерашних кросовок, на раковине, полностью описывают моё состояние*"
    nika "*Заляпанное зеркало, которое надо помыть уже как две недели*"
    nika "*Количество зубной пасты примерно равно моему желанию жить*"
    nika "*Старая, чугунная ванна разносила звуки капель воды, которые переодический падали на неё, по всей квартире*"
    nika "*Всё так сильно раздаражает*"
    nika "*При этом, всё это создаёт такую успокаивающую атмосферу*"
    nika "*Фух, Слишком много сна, я вся затекла*"
    nika "*Очень хочется завалиться обратно спать*"
    nika "*Но я точно умру, если снова позволю мозгу отключиться"
    "*Вибрация телефона*"
    scene phone
    nika "*Ну кто там ещё?!*"
    scene call_alice
    '(На дисплее высвечивается деликатное "Тётя Алиса")'
    "(Сердце заходится в волнении)"
    nika "*Я очень давно с ней не общалась*"
    nika "*Боюсь представить, что ей от меня нужно*"
    "(Нажимает на ответ)"
    nika "*До меня доносится звонкий запыхавшийся голосок*"
    nika "*Так и не скажешь, что этой женщине идёт пятый десяток*"
    alice "Здравствуй, Ника. Как ты?"
    nika "*Я собираюсь с силами и стараюсь убедительно сыграть радость*"
    nika "Добрый день тёть Алиса!"
    nika "Да справляюсь по-тихоньку, а вы как?"
    nika "*Постараюсь перевести тему*"
    nika "*Желание разговаривать отсутствует*"
    nika "*Но в семейном кругу лучше этого не показывать*"
    nika "*Ни к чему лишние вопросы*"
    alice "Да то же самое, неплохо"
    alice "Я зачем звоню, собственно... Мне мой знакомый по цеху сказал, что его маркетологам помощь нужна."
    nika "Я не буду придумывать маркетинговые ходы"
    alice "Нет-нет-нет."
    alice "Они хотят создать игру про их отель"
    alice "Ищут способного программиста"
    nika "*На моей памяти только тете Алисе доставляло удовольствие решение проблем*"
    nika "*Договоры, капризы и ругань всегда достаются ей*"
    nika "*Поэтому моя пылкая и непробиваемая тетка была рождена, чтобы стать организатором свадеб.*"
    nika "*Но в этом есть свои плюсы*"
    nika "*Например, За столько лет работы она обрела огромное количество влиятельных друзей.*"
    alice "Я как услышала, сразу про тебя вспомнила!"
    alice "Твоя мама говорила, что ты в универе на it факультете учишься."
    alice "А там и проживание в загородном отеле, и питание!"
    nika "*Надо изобразить заинтересованность*"
    nika "Ой, теть Алис."
    nika "Я думаю, это было бы интересно."
    nika "В любом случае, можете мне скинуть контакты работодателя, а там я разберусь?"
    alice "Конечно!"
    alice "Я тороплюсь очень."
    alice "Решила тебе позвонить, пока выдалась минутка."
    alice "Так что чуть позже пришлю его номер. Напишешь, что от меня."
    alice "Даже резюме не понадобится."
    nika "*Я чувствую, как она весело подмигивает.*"
    nika "*Она воодушевляющая, жизнерадостная женщина.*"
    nika "*Может, если бы мы чаще виделись, я бы многому у нее научилась.*"
    nika "*На душе становится гадко. Тянет и морозит.*"
    nika "*Я прощаюсь под аккомпанемент громких гудков. Она сбрасывает меня так же спонтанно.*"
    "(Находясь в смятении, открывает телеграмм)"
    nika "*Пятнадцать новых сообщений*"
    nika "*Большенство из новостных каналов*"
    nika "*Не удивительно*"
    "(Взляд зацепился за какой-то чат)"
    nika "*Ой, точно!*"
    nika "*Я же сегодня должна в два должна выйти!*"
    "(Находит глазами время)"
    nika "*Фух...*"
    nika "*Ещё 2 часа*"
    nika "*Мне нужно только поесть и собраться*"
    nika "*Успеваю*"
    scene hall
    with Dissolve(2)
    "(Выходит из ванной и идёт на кухню)"
    "(Открывает дверь на кухню)"
    scene kitchen
    with Dissolve(2)
    "Тёплый тусклый свет рассеивался по всей кухне"
    "Старая лампочка, давно висящая в гордом одиночестве"
    "Хоть и слабо, но освещала плохо убранный стол"
    "Заляпанные окна, в которые въелись пятна старости"
    "Немытая посуда, которая копилась уже примерно неделю нагнитала атмосферу"
    "Разрушая весь уют"
    "Тёплый свет осветил и Нику"
    "Которая, распахнув дверь, разрушила гробовую тишину"
    "(Подошла и открыла холодильник)"
    nika "*Да уж...*"
    nika "*Из весомого: огрызок колбасы, пара помидоров и минералка*"
    nika "*В магазин я вчера, по дурости, не сходила*"
    "(С надеждой заглядывает в хлебницу)"
    "В хлебнице оказалась половина, ещё относительно свежего, нарезного батона"
    nika "*Что же...*"
    nika "*Бутерброды лучше, чем ничего*"
    "Приготовление и поглощение еды занимет некоторое время"
    nika "*Время идёт...*"
    nika "*А меня продолжает посещать скверная мысль забить и никуда не пойти*"
    menu job:
        "Пойти на работу":
            jump job_yes
        "Забить":
            jump end_1
    label end_1:
        scene depht
        with Dissolve(2)
        scene author
        with Dissolve(3)
        play music "main-menu-theme.mp3"
        author "Снова здравствуй"
        author "Я же говорил, что мы ещё встретимся"
        author "Мои поздравления"
        author "Ты достиг самой простой и быстрой концовки"
        author "Далее я расскажу, что произошло с нашей любимой Никой"
        author "Наша героиня, не пойдя на работу, полностью погрузилась в себя и свои мысли"
        author "К сожелению, Нику полностью охватила депрессия"
        author "В своих мыслях и депрессии она провела огромный период своей жизни"
        author "Мысли о тлене и безсмысленности всего, поглотили её полностью"
    menu back:
        author "Ну что, ты доволен своими действиями?"
        "Да":
            author "Ну... Как скажешь, прощай"
            return
        "Нет":
            author "Ну... У меня есть решение"
            jump story
    label job_yes:
    nika "К чёрту, лукавый"
    nika "*Мне точно надо проветриться*"
    nika "*Всегда мечтала найти работу подальше от этого гнусного городка*"
    nika "*Но... похоже мечтами это и останется*"
    "(Одевшись Ника направилась в коридор)"
    scene hall
    with Dissolve(3)
    show nika:
        xalign 1.00
        yalign 1.00
    "(Стандартные чёрные носки скользят в кеды)"
    nika "*И вот я уже готова*"
    "(Хватает сумку с примитивными вещами вроде паспорта, зарядки и влажных салфеток)"
    nika "*С телефоном в руке осматриваю квартиру так, будто больше не вернусь*"
    nika "*Всё в порядке*"
    nika "*Вечером обязательно схожу в продуктовый*"
    nika "*Ключ проварачивается со скрипом*"
    nika '*Моё больное воображение вторит уничтожительное "Пути назад нет"*'
    "(На лестнечной клетке Ника встречает соседа)"
    scene stairs
    with Dissolve(2)
    show nika:
        xalign 1.00
        yalign 1.00
    nika "*Чёрт...*"
    nika "*Ну только не он*"
    "(Что бы не показать в глазах консервативного мужчины ещё хуже)"
    "(Надо громко поздароваться)"
    nika "*Здравствуйте!*"
    "(Буркнув что-то себе под нос, сосед уходит)"
    nika "*Надо же...*"
    nika "*Даже не назвал сатанисткой, кривя свои противные усы*"
    nika "*Обычно его вымораживают мои кольца.*"
    "(Выходя из подъезда, потирает пальцы)"
    nika "Чёрт, кольца!"
    nika "*Я вышла впритык*"
    nika "*Точно опоздаю, если сейчас вернусь за ними*"
    nika "*Но без колец я как без пальцев*"
    nika "*Выбора нет*"
    "(Раздраженно вздохнув, взлетаю по ступенькам обратно)"
    "(Как назло, некоторые колечки, лежащие в пиале с аксессуарами, запутались в цепочке)"
    nika "*Издевательство какое-то!*"
    "(Наконец я собираюсь и выхожу за дверь)"
    "(За моим плечом мелькает темный силуэт)"
    scene stairs
    with Fade(0.1, 0.1, 0.1)
    show nika:
        xalign 1.00
        yalign 1.00
    nika "*Я конечно с детства слабой психикой известна*"
    nika "*Но такого ещё не было*"
    nika "(Резко оборачиваюсь)"
    nika "*Никого нет!?*"
    nika "*Какого?! Что это было?!*"
    nika "*Я слышала, что от пересыпа бывают галлюцинации*"
    nika "*Но никогда не думала, что меня это затронет*"
    nika "*Ага*"
    nika "*Думаешь, что это будешь не ты*"
    nika "*Но это будешь ты*"
    "(С тревожностью и тыжестью вздыхает и выходит из подъезда)"
    nika "*Вид обшарпанных серых хрущевок не прельщает*"
    nika "*Голова пуста*"
    "(Уже на подходе к гравированным воротам парка додумывается достать телефон)"
    "На экране появляются уведомления о пропущеных"
    nika "*Он машет мне рукой, взъерошенный, как воробей*"
    nika "*Я закатываю глаза, но улыбка мажет по губам.*"
    sava "Я уже думал, что ты не придешь."
    nika "Размечтался."
    nika "*Я борюсь с желанием растрепать его волосы.*"
    nika "*Мы идем по ровной каменной кладке*"
    nika "*Пока мне приходится выслушивать как ему не удалось вернуть деньги.*"
    nika "*За бракованные наушники с вайлдберрис.*"
    "Кроны шелестят от горячего порывистого ветра."
    nika "*Обыденный элемент тлена бесконечного круговорота жизни.*"
    nika "*Через пару месяцев они начнут желтеть, осыпаться, а после гнить в земле*"
    nika "*Никому так и не сгодившиеся.*"
    nika "*Деревья, из величественных, тянущихся к небесам столбов*"
    nika "*Станут черными тенями самих себя, уродливыми иссохшимися старушечьими руками.*"
    nika "*В детстве все красочное.*"
    nika "*В детстве не задумываешься, сколько неизбежных мучений встретит каждый из нас.*"
    nika "*Но что смерть? Если не освобождение?*"
    nika "*Блаженное ничто.*"
    nika "*После смерти от тебя не потребуют оплаты долгов*"
    nika "*Уважения к ничтожным людям.*"
    nika "*Никому более не аппетитны твои эмоции.*"
    nika "*В чем интерес притворяться хорошим человеком?*"
    nika "*Если внутри тебя без конца разъедает?*"
    nika "*Угодить окружающим?*"
    nika "*Готова поспорить, что они такие же лживые куски дерьма.*"
    nika "*Никогда не догадаешься, что о тебе думает тот или очередной случайный собеседник*"
    nika "*Работодатель или вторая половинка, когда приветливо улыбается тебе в лицо.*"
    sava "(Легко толкает Нику плечом)"
    sava "Ты чего притихла?"
    nika "*Он всегда такой — шумный и раздражающий.*"
    nika "*Общение наше тянется с детства, поэтому он продолжает липнуть ко мне*"
    nika "*Какой бы отстраненной от реального мира я не была.*"
    nika "*Мне все равно на темы, которые мы обсуждаем*"
    nika "*но тут я припоминаю разговор с тетей Алисой.*"
    nika "Я вчера на собеседовании была."
    nika "Этот урод смотрел на меня так, будто я его всю школу гнобила"
    nika "А сейчас пришла устраиваться к нему на работу."
    nika "Ха, да его просто испугали твои синяки под глазами."
    "(Сава оттягивает пальцами кожу под глазами и корчит рожу.)"
    nika "А от тебя его бы отпугнул запах."
    sava "Эй! Так что, он тебя не взял?"
    nika "Догадайся. Намекнул, что с таким лицом я всех посетителей распугаю."
    sava "Ну да, у нас же каждый второй мечтает работать официантом."
    nika "Фырк"
    nika "А сегодня мне тетя позвонила. Сказала, что у её другу помощь нужна."
    nika "Достали меня эти оценивающие встречи. А там я сразу по рекомендации пропишусь."
    sava "Да ладно. Но ты же понимаешь, что это скорее всего огромное количество работы."
    sava "А ты любишь отлынивать."
    nika "*В груди потяжелело от его слов*"
    nika "*Меня раздражают люди тыкающие в мою лень.*"
    nika "*Они пугают меня, злят, ставят в неловкое положение своими эмоциями и тупостью.*"
    nika "*Если бы у меня были математические способности*"
    nika "*Выучилась бы на курсах*"
    nika "*И просиживала в халате за компьютером всю социальную жизнь.*"
    nika "*Учитывая, что нормальную работу я в любом случае не найду.*"
    nika "Меня с универа выгнали за неуспеваемость"
    nika "Мой потолок — сфера обслуживания."
    nika "Хочешь не хочешь, с этими идиотами придется общаться."
    sava "(Вскидывает брови)"
    nika "Тем более, скоро за квартиру платить."
    nika "Родители отсыпали мне пару месяцев назад"
    nika "Но ясно дали понять, что это было в последний раз"
    nika "Хотя, вроде как в этом отеле и живешь, и ешь."
    nika "Так что можно заработать, а потом впасть в спячку."
    sava "Вау! Что, прям в номере жить можно?"
    nika "*Мысль кажется заманчивой.*"
    nika "(Сердце тревожно стучит)"
    nika "*Мне не нравится моя квартира.*"
    nika "*Она находится в районе, где главная достопримечательность бомжи.*"
    nika "*А развлечение — игра «успей добежать до дома, пока к тебе не пристали».*"
    nika "Не знаю."
    nika "Наверное, я вечером напишу начальнику, спрошу, что да как."
    nika "Но честно, идея максимально ублюдская."
    nika "*Силы покидают меня.*"
    nika "*У меня не получится, так что и обнадеживать себя не стоит.*"
    nika "*Как делать других счастливыми, когда сам хочешь лишь удавиться от самого факта своего существования?*"
    nika "Мне кажется, ты прав."
    nika "Я не справлюсь."
    sava "Эй! Странно, конечно, представить тебя в такой обстановке"
    sava "Но всегда нужно пробовать что-то новое."
    sava "Как говорят, не попробуешь не узнаешь!"
    nika "*Я нахожу свое отражение в его лучистых карих глазах.*"
    nika "*Всегда радостных и уверенных.*"
    nika "*Ох, Савелий*"
    nika "*Как бы я хотела тебе поверить.*"
    sava "Пообещай мне, что напишешь ему!"
    nika "Обещаю."
    nika "*Нос начинает щипать*"
    nika "Я чувствую предательскую влагу."
    nika "(Поспешно отвернулась)"
    "Остаток вечера проходит в нескончаемой трели потока сознания"
    "Уже дома"
    "Лежа в кровати"
    nika "*Экран светит мне в лицо так же неестественно и раздражающе*"
    nika "*Как утром.*"
    nika "*Я хочу спать, но внутри волнительно*"
    nika "*Как перед прыжком в ледяную воду*"
    nika "*Мои пальцы подрагивают, когда я нахожу диалог с тетей Алисой*"
    "Непрочитанным сообщением висит номер телефона."
    nika "Я не решаюсь писать."
    nika "Вдруг меня охватывает это ужасное желание развернуться и уйти, как много раз на пирсе."
    nika "*Нет.*"
    nika "Правильно Сава сказал."
    nika "Не попробуешь — не узнаешь."
    author "Конец пролога."
    scene author
    with Dissolve(3)
    author "Снова здравствуй!"
    author "Мы будем выдеться часто"
    author "Ну как тебе пролог?"
    author "Я жду обратной связи"
    author "Телеграмм есть в главном меню, во вкладке об игре"
    author "Ну что?"
    author "Идём дальше?"
    menu prolog_comp:
        "Да":
            jump glava1
        "Нет":
            author "Хорошо, скажи как будешь готов"
            jump prolog_comp
    label glava1:
    author "Окей, идём дальше"
    scene hospital_ward
    with Fade(1, 1, 1)
    show nurse:
        xalign 0.00
        yalign 1.00











    return
