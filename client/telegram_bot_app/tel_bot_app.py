from os import getenv
from dotenv import load_dotenv
import telebot

from server.service.film_search_service import FilmSearchService
from server.service.user_query_service import UserQueryService




class TelegramSearchFilm:
    # __logger = Logger("ConsoleSearchFilmApp").logger

    # def __init__(self, user_query_service: UserQueryService, film_search_service: FilmSearchService):
    #     self.__film_search_service = film_search_service
    #     self.__user_query_service = user_query_service

    def __init__(self):
        load_dotenv()
        self.bot: telebot.TeleBot = telebot.TeleBot("7064056325:AAFxjyT4jesAOrAsckY94hOAc_xk1P-LVQ0")
        self.init_commands()

    def start(self):
        self.bot.infinity_polling()

    def init_commands(self):
        """Initialize methods to represent bot commands"""
        self.help = self.bot.message_handler(commands=['help'])(self.help_command)
        self.test = self.bot.message_handler(commands=['test'])(self.test_command)
        self.stat = self.bot.message_handler(commands=["start"])(self.start_command)
        self.callback = self.bot.callback_query_handler(func=lambda callback: True)(self.callback_command)

    def callback_command(self, callback):
        if callback.data == "print_msg":
            self.bot.send_photo(callback.message.chat.id, "https://m.media-amazon.com/images/M/MV5BNDMyODU3ODk3Ml5BMl5BanBnXkFtZTgwNDc1ODkwNjE@._V1_SY1000_SX677_AL_.jpg")

    def help_command(self, message: telebot.types.Message):
        markup = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Press me!", callback_data="print_msg")
        button2 = telebot.types.InlineKeyboardButton(text="Don'tPress me!", callback_data="print_msg")
        button3 = telebot.types.InlineKeyboardButton(text="One more time press me!!", callback_data="print_msg")
        markup.row(button1, button2)
        markup.row(button3)
        self.bot.send_message(chat_id=message.chat.id, text="Help!", reply_markup=markup)

    def test_command(self, message: telebot.types.Message):
        self.bot.send_message(chat_id=message.chat.id, text=message.text)

    def start_command(self, message: telebot.types.Message):
        markup = telebot.types.ReplyKeyboardMarkup()
        button1 = telebot.types.KeyboardButton(text="help")
        button2 = telebot.types.KeyboardButton(text="Don'tPress me!")
        button3 = telebot.types.KeyboardButton(text="One more time press me!!")
        markup.row(button1, button2)
        markup.row(button3)
        msg = "Hello there! How are you?"
        self.bot.send_message(chat_id=message.chat.id, text=msg, reply_markup=markup)
        self.bot.register_next_step_handler(message, callback=self.on_click)

    def on_click(self, message):
        self.bot.send_message(message.chat.id, f"/{message.text}")


TelegramSearchFilm().start()


# class TestBot:
#
#     def __init__(self) -> None:
#         self.bot: telebot.TeleBot = telebot.TeleBot("7064056325:AAFxjyT4jesAOrAsckY94hOAc_xk1P-LVQ0")
#         self.init_commands()  # this method initialize my commands
#
#     def start(self):
#         self.bot.infinity_polling()
#
#     def init_commands(self):
#         """Initialize methods to represent bot commands"""
#         self.help = self.bot.message_handler(commands=['help'])(self.help_command)
#         self.test = self.bot.message_handler(commands=['test'])(self.test_command)
#
#     # Commands bellow
#     def help_command(self, message: telebot.types.Message):
#         self.bot.send_message(chat_id=message.chat.id, text="Help!")
#
#     def test_command(self, message: telebot.types.Message):
#         self.bot.send_message(chat_id=message.chat.id, text=message.text)
#
#
# TestBot().start()
