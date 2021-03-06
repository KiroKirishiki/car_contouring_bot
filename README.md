# Car contouring bot
Тестовая версия бота для телеграма. Функционал бота: пользователь кидает картинку боту, бот перерисовывает картинку в раскраску черного цвета на белом фоне.

# Установка
Для установки проекта необходимо скачать оба файла в одну папку
* image_contouring.py - отвечает за обработку изображения
* main.py - "мейн" код самого бота
# Используемые модули
Для запуска проекта потребуются следующие модули
```
* pyTelegramBotAPI
* opencv (cv2)
* numpy
```

Также для корректной работы бота могут потребоваться последнии версии следующих модулей `gunicorn, PySocks, requests, urllib3`.

# Запуск проекта
Для создания собственного бота необходимо получить токен (в программном коде `TOKEN`) бота от `@botfather` - "*отец*" всех ботов телеграмма.
Токен своего бота необходимо будет вставить здесь:
```
TOKEN = 'ваш токен'
bot = telebot.TeleBot(TOKEN)
```
От `@botfather` вы также получите ссылку в телеграмм чат вашего бота, с которым и будете работать далее.

В виду того, что бот не задеплоен, нужно будет сначала запускать `main.py`, для того чтобы бот работал.  
Работать с ботом очень просто:  
Вы заходите в чат с ботом, присылаете ему картинку и ждёте обработку картинки ботом. Как только бот обработает картинку, бот вышлет вам результат.
