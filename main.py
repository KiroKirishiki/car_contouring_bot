import telebot
from telebot import apihelper
from image_contouring import *

apihelper.proxy = {'https':'socks5h://68.183.15.160:1080'}
TOKEN = '985690562:AAF3zKYojA2bvbEequZw5KbcIAUK5PCcnHk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую вас')

@bot.message_handler(content_types=['photo'])
def contour_image(message):
    bot.send_message(message.chat.id, "Начинаю обработку изображения, ожидайте")
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", "wb") as new_file:
        new_file.write(downloaded_file)
    # Get image from message
    image = cv2.imread("image.jpg")
    contours = get_contours(image)
    image_contoured = draw_contours(contours, image)
    cv2.imwrite("image.jpg", image_contoured)
    photo = open("image.jpg", 'rb')
    bot.send_photo(message.chat.id, photo)

bot.polling(none_stop=True)