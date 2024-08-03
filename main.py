import os
import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot import types
from telebot.types import InputMediaPhoto


bot = AsyncTeleBot('6570190161:AAGrM3ot-Nyo9AI5gxv3rMSWYipVjjQdJjA')
file = 'table_plans.xlsx'


@bot.message_handler(commands=['start'])
async def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Учёба")
    btn2 = types.KeyboardButton("Общежитие")
    btn3 = types.KeyboardButton("Немного про деньги")
    btn4 = types.KeyboardButton("Активности")
    btn5 = types.KeyboardButton("Прочее")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    await bot.send_message(message.chat.id,
                           f'Привет, {message.from_user.first_name} ! Поздравляю тебя с поступлением в УУНиТ.'
                           '\n Бот содержит в себе ответы на частые вопросы от абитуриентов и может послужить тебе '
                           'небольшим справочником'
                           '\n\n Если ты не нашел ответа на свой вопрос, то можешь обратиться к админу @Dantekageshad.'
                           '\n\n \U00002757\U00002757\U00002757 Бот является студенческой инициативой и носит '
                           'ознакомительный характер\U00002757\U00002757\U00002757'
                           '\n (СОЗДАНО ДЛЯ СТУДЕНТОВ ГОЛОВНОГО ВУЗА БАКАЛАВРИАТА/СПЕЦИАЛИТЕТА ОЧНОЙ ФОРМЫ ОБУЧЕНИЯ)',
                           reply_markup=markup)


@bot.message_handler(content_types=['text'])
async def func(message):
    if message.text == "Немного про деньги":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Академ стипендия")
        btn2 = types.KeyboardButton("Социальная стипендия")
        btn4 = types.KeyboardButton("Мат помощь")
        btn5 = types.KeyboardButton("Назад")
        markup.add(btn1, btn2, btn4, btn5)

        await bot.send_photo(message.chat.id, photo=open('money.jpg', 'rb'),
                             caption='<b>Стипендия</b> - любимое слово каждого студента. Получают '
                                     'ее 25 числа каджого месяца, а если дата приходится на выходные, то раньше. '
                                     '\nПри неудачной сдаче сессии(у вас есть тройки/двойки или незачёты,'
                                     'задолженности) можете забыть о ней до следующего семестра, если, конечно, '
                                     'вы хорошо закроете сессию.'
                                     '\nСуществует несколько видов стипендий,посмотрим с чем их едят, а также '
                                     'немного про материальную помощь', reply_markup=markup, parse_mode='html')

    elif message.text == "Академ стипендия":
        photos = ['гас.jpg', 'пгас.jpg']
        media = []
        for photo_path in photos:
            if os.path.exists(photo_path):
                media.append(InputMediaPhoto(open(photo_path, 'rb')))
            else:
                await bot.send_message(chat_id=message.chat.id, text=f"Файл {photo_path} не найден.")
        if media:
            await bot.send_media_group(chat_id=message.chat.id, media=media)

        await bot.send_message(message.chat.id, 'В первом семестре ГАС выплачивается в зависимости от среднего балла ,'
                                                ' с которым вы поступили без учёта индивидуальных достижений ('
                                                'фиксированно вы получаетет около 4500, информация не точная).'
                                                '\n \nТак надбавка со средним баллом 80 - 84.99 будет 3000'
                                                '\n \nДля 85 - 89.99 плюс 5000'
                                                '\n \nИ если вы очень умный и средний балл от 90, то надбавка 10000'
                                                '\n \nЕсли вы ещё умнее и поступили по олимпиале, то надбавка будет '
                                                '50000/80000')

    elif message.text == "Социальная стипендия":
        photos = ['гсс.jpg', 'пгсс.jpg']
        media = []
        for photo_path in photos:
            if os.path.exists(photo_path):
                media.append(InputMediaPhoto(open(photo_path, 'rb')))
            else:
                await bot.send_message(chat_id=message.chat.id, text=f"Файл {photo_path} не найден.")
        if media:
            await bot.send_media_group(chat_id=message.chat.id, media=media)

        await bot.send_message(message.chat.id, 'Если вы учитесь на бюджете, проживаете в общежитие и вам от 18 до '
                                                '23 , '
                                                'у вас есть возможность оформить социальную стипендию и получать больше'
                                                ' денег'
                                                '\n\nКак это сделать?'
                                                '\n\nЧитаем гайды для самых умных и тех, кто не умеет '
                                                'пользоваться госуслугами. (я серьёзно, читай оба файла и решай на чьей'
                                                ' стороне ты')
        await bot.send_document(message.chat.id, document=open('Как оформить социалку.pdf', 'rb'))
        await bot.send_document(message.chat.id, document=open('Как оформить социалку, не выходя из комнаты.pdf', 'rb'))

    elif message.text == "Мат помощь":
        await bot.send_photo(message.chat.id, photo=open('матпомощь.jpg', 'rb'),
                             caption='Материальная помощь — это единовременная выплата, по различным социальным '
                                     'причинам. '
                                     '\n\nПолучать её могут и бюджетники, и платники, если они состоят в Профсоюзе. '
                                     'Для этого следует лишь собрать документы и принести их в профком (не забудьте '
                                     'профсоюзный билет) не позднее 28 числа каждого месяца (может быть раньше в связи'
                                     ' с праздниками/выходными), сама выплата приходит в следующем месяце'
                                     '\n\nСписок причин и документов для оформления приведён ниже')
        await bot.send_document(message.chat.id, document=open('Причины матпомощи.pdf', 'rb'))

    elif message.text == "Учёба":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Расписание')
        btn2 = types.KeyboardButton('Учебный план')
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        await bot.send_photo(message.chat.id, photo=open('невдупленыш.jpg', 'rb'),
                             caption='Немного слов'
                                     '\n  <b>Экзамен</b> - приходишь, решаешь задачки или отвечаешь письменно '
                                     'на вопросы, потом бубнишь перед преподом защиту, получаешь оценку. Также '
                                     'на многих предметах можно получить автомат по экзамену - скипнуть заучивание'
                                     ' материала, решение билета и защиту. Автомат можно получить по разным п'
                                     'ричинам, но чаще всего за успехи в учебе во время семестра.'
                                     '\n\n  <b>Зачёт</b> - надо просто все вовремя сдать и получить зачёт или '
                                     'незачёт. У некоторых преподавателей на некоторых дисциплинах надо сдать '
                                     'зачетную работу, чтобы получить этот самый.'
                                     '\n\n  <b>Диф зачет</b> aka <b>зачет с оценкой</b> aka <b>дифференцированный '
                                     'зачет</b> - то же самое, что зачет, но он может поднасрать тебе в стипуху, '
                                     'если получишь «удовл.» (троечка).'
                                     '\n\n  <b>Проект</b> aka <b>курсач</b> - массивная чапалаха, которую ты '
                                     'делаешь в последнюю неделю, чтобы закрыть предмет, хотя у тебя был целый '
                                     'семестр для этого.'
                                     '\n\n  <b>Семестр</b> - учебное полугодие', reply_markup=markup, parse_mode='html')

    elif message.text == "Расписание":
        markup = types.InlineKeyboardMarkup(row_width=1)
        b1 = types.InlineKeyboardButton("Приложение для Андроид",
                                        url='https://play.google.com/store/apps/details?id=ru.uust')
        b2 = types.InlineKeyboardButton("Приложение для IOS", url='https://apps.apple.com/app/id6447134234')
        b3 = types.InlineKeyboardButton("Сайт", url='https://uust-time.ru/')
        markup.add(b1, b2, b3)
        await bot.send_photo(message.chat.id, photo=open('пары.jpg', 'rb'),
                             caption='Лекции, практики, лабы, а что зачем ? '
                                     '\n \n Лекция - пара, когда несколько групп собирают в одной большой душной '
                                     'аудитории и читают им материал. Стоит ли ходить? 50/50 Если хотите всё знать и '
                                     'уметь, то смело вставайте к первой паре. Если вы верите в себя и одногрупника, '
                                     'который ходил и всё записывал, то можете продлить свой сон. (Некоторые преподы '
                                     'отмечают на лекциях и могут проводить контрольные, узнайте об этом заранее)'
                                     '\n\n Практика - приходим, решаем задачки, вопросы решаем, ничего интересного. '
                                     'Ходить стоит, но если вы сверхчеловек, который сам всё может изучить, то '
                                     'появляйтесь хотя бы изредка'
                                     '\n\n Лабы - две пары подряд вы сидите и занимаетесь чем-то, прогуливать не стоит,'
                                     ' потому что придётся отрабатывать. Защитить лабу - это показать, что вы'
                                     ' разбираетесь в своей работе, а не списали её у друга за 10 минут до конца'
                                     '\n\n Приложения и сайт с расписанием смотреть ниже ( для поступивших в бывший БГУ'
                                     ' может не работать)', reply_markup=markup)

    elif message.text == "Учебный план":
        await bot.send_photo(message.chat.id, photo=open('me.jpg', 'rb'),
                             caption='Самый частый вопрос: "А что мы будем изучать???"'
                                     '\n\n Так вот. Учебный план - это непонятный файл с тем, что вы будете изучать, '
                                     'когда и в каком объёме. В файле ниже вы можете найти план для своего профиля '
                                     'специальности')
        await bot.send_document(message.chat.id, document=open('plans.xlsx', 'rb'))
        await bot.send_document(message.chat.id, document=open('Как читать учебные планы.pdf', 'rb'))

    elif message.text == "Прочее":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("МФСО")
        btn2 = types.KeyboardButton("ИСУ")
        btn3 = types.KeyboardButton("Контактная информация")
        btn4 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3, btn4)
        await bot.send_photo(message.chat.id, photo=open('Мем с котом.jpg', 'rb'), reply_markup=markup)

    elif message.text == "Контактная информация":
        await bot.send_photo(message.chat.id, photo=open('callc.jpg', 'rb'),
                             caption='Сall-центр +7(917)379-07-00'
                                     '\n\nОтдел сопровождения '
                                     'платного обучения +7(917)756-55-05'
                                     '\n\nМФСО (Многофункциональный студенческий офис) +7-908-350-50-29'
                                     '\n\nБухгалтерия +7-908-350-49-45'
                                     '\n\nУправление по социальной работе +7-(908)-350-49-09')

    elif message.text == "ИСУ":
        await bot.send_photo(message.chat.id, photo=open('загруженное.jpg', 'rb'),
                             caption='ИСУ? ШТА?'
                                     '\n\nЗнакомтесь, это ИСУ, типа местные госуслуги, можно заказать  справочки, '
                                     'посмотреть свои оценки кинуть заявку на общагу и прочие мелочи жизни'
                                     '\n\nА как получить туда доступ, смотрите ниже. https://isu.uust.ru/ (новая '
                                     'ссылка на сайт)')
        await bot.send_document(message.chat.id, document=open('Как получить доступ в ИСУ.pdf', 'rb'))

    elif message.text == "МФСО":
        await bot.send_photo(message.chat.id, photo=open('загруженное (1).jpg', 'rb'),
                             caption='МФСО, аля местное МФЦ, консультуруют по вашим вопросам и хранят ваши справочки.'
                                     ' https://vk.com/mfso_uust '
                                     '\n\nА как заказать эти ваши справки? Читаем ниже ')
        await bot.send_document(message.chat.id, document=open('Гайд по справкам.pdf', 'rb'))

    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Учёба")
        btn2 = types.KeyboardButton("Общежитие")
        btn3 = types.KeyboardButton("Немного про деньги")
        btn4 = types.KeyboardButton("Активности")
        btn5 = types.KeyboardButton("Прочее")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        await bot.send_message(message.chat.id, 'Вы вернулись в главное меню'.format(message.from_user),
                               reply_markup=markup)

    elif message.text == "Общежитие":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заселение")
        btn2 = types.KeyboardButton("Как вы тут живёте?")
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        await bot.send_photo(message.chat.id, photo=open('hostel.jpg', 'rb'),
                             caption='Если вы ткнули сюда, то вас ждут увлекательные 4-5 лет жизни в общаге. '
                                     '\n\n А пока смотрим как заселиться и подружиться с тараканами ',
                             reply_markup=markup)

    elif message.text == "Заселение":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Шаг 1")
        btn2 = types.KeyboardButton("Шаг 2")
        btn3 = types.KeyboardButton("Шаг 3")
        btn4 = types.KeyboardButton("Шаг 4")
        btn5 = types.KeyboardButton("Шаг 5")
        btn6 = types.KeyboardButton("Вернуться")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        await bot.send_message(message.chat.id, 'Пошаговая инструкция как заселиться в общагу ', reply_markup=markup)

    elif message.text == "Шаг 1":
        await bot.send_photo(message.chat.id, photo=open('plasw.jpg', 'rb'),
                             caption='Шаг 1. Подать заявление на предоставление койко-места до 15.08')
        await bot.send_document(message.chat.id, document=open('zayavl-zaseleniye.docx', 'rb'))

    elif message.text == "Шаг 2":
        await bot.send_document(message.chat.id,
                                document=open('Инструкция для подачи заявления на общежитие.pdf', 'rb'),
                                caption='Шаг 2. Подаём заявление в ИСУ(если вам предоставили место) до 23.08'
                                        '\n\nКак получить доступ в ИСУ? Смотреть во вкладке Прочее')

    elif message.text == "Шаг 3":
        photos = ['prepare.jpg', 'step1.jpg', 'step2.jpg', 'step3.jpg', 'step4.jpg']
        media = []
        for photo_path in photos:
            if os.path.exists(photo_path):
                media.append(InputMediaPhoto(open(photo_path, 'rb')))
        if media:
            await bot.send_media_group(message.chat.id, media=media)
        await bot.send_message(message.chat.id,
                               'Шаг 3. Собираем бумаги и идём в нужный день в нужный час в нужное место')

    elif message.text == "Шаг 4":
        photos = ['pay1.jpg', 'pay2.jpg', 'pay3.jpg', 'pay4.jpg', 'pay5.jpg', 'pay6.jpg', 'pay7.jpg']
        media = []
        for photo_path in photos:
            if os.path.exists(photo_path):
                media.append(InputMediaPhoto(open(photo_path, 'rb')))
        if media:
            await bot.send_media_group(message.chat.id, media=media)
        await bot.send_message(message.chat.id, 'Шаг 4. Оплачиваем нашу жизнь ')

    elif message.text == "Шаг 5":
        photos = ['doc1.jpg', 'doc2.jpg', 'doc3.jpg', 'doc4.jpg', 'doc5.jpg', 'doc6.jpg', 'doc7.jpg']
        media = []
        for photo_path in photos:
            if os.path.exists(photo_path):
                media.append(InputMediaPhoto(open(photo_path, 'rb')))
        if media:
            await bot.send_media_group(message.chat.id, media=media)
        await bot.send_message(message.chat.id, 'Шаг 5. Закрепляем чеки до 15.09, показывая что мы честные люди, '
                                                'сами чеки относим коменданту (если требуется) ')

    elif message.text == "Вернуться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Заселение")
        btn2 = types.KeyboardButton("Как вы тут живёте?")
        btn3 = types.KeyboardButton('Назад')
        markup.add(btn1, btn2, btn3)
        await bot.send_photo(message.chat.id, photo=open('hostel.jpg', 'rb'),
                             caption='Если вы ткнули сюда, то вас ждут увлекательные 4-5 лет жизни в общаге.'
                                     '\n\n А пока смотрим как заселиться и подружиться с тараканами ',
                             reply_markup=markup)

    elif message.text == 'Как вы тут живёте?':
        await bot.send_photo(message.chat.id, photo=open('how.jpg', 'rb'),
                             caption='Пару слов туда-сюда'
                                     '\n\n 1. да тараканы есть, в разных количествах и не везде, вам придётся '
                                     'смириться с этим. Главное - убирайтесь и травите их'
                                     '\n\n2. Никаких электронагревательных приборов. А если честно, то можно всё, '
                                     'главное не спалиться перед проверками. Если стучат в дверь, а вы никого не ждали,'
                                     ' прячьте всё '
                                     '\n\n3. Дружим со студсоветом. Повезёт - вам и комнату поменяют на хорошую, и '
                                     'мебель новую подгонят и просто вашу жопу прикроют')

    elif message.text == 'Активности':
        await bot.send_photo(message.chat.id, photo=open('act.jpg', 'rb'),
                             caption='Студенческие активности: спортивные и творческие'
                                     '\n\nhttps://vk.com/uust_youth - в группе Управления по молодёжной политике вы '
                                     'найдёте информацию о мероприятиях, форумах, грантовых конкурсах, также проводятся'
                                     ' розыгрыши билетов на культурные мероприятия. '
                                     'В контактах группы можете найти множество студенческих объединений разной '
                                     'направленности'
                                     '\n\n Чтобы узнать больше про мероприятия в университете и о Профкоме, рекомендуем'
                                     ' к ознакомлению документ ниже ')
        await bot.send_document(message.chat.id, document=open('Gid_pervokursnika_Profkoma.pdf', 'rb'))
        await bot.send_photo(message.chat.id, photo=open('спорт.jpg', 'rb'),
                             caption='https://vk.com/sportusatu - группа кафедры физического воспитания. '
                                     'Освещаюстя спортивные события, наборы в сборные и секции '
                                     '\n\nhttps://vk.com/uustesports - сектор киберспорта'
                                     '\nУведомления о наборах в сборные/секции будут опубликованы в группах, следите за'
                                     ' обновлениями')


asyncio.run(bot.polling(none_stop=True))
