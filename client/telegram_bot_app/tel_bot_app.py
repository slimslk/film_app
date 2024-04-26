from os import getenv
from dotenv import load_dotenv
import telebot

from client.telegram_bot_app.film_search_helper import FilmSearchHelper
from client.telegram_bot_app.my_films_model import UserFilms
from logger import Logger
from server.api.public_api import PublicApi
import client.telegram_bot_app.message_helper as msg_helper
from server.entity.film_model import Film
import client.telegram_bot_app.constants as constants


class TelegramSearchFilm:
    __logger = Logger("TelegramSearchFilm.class", "./logs/telegram_app_error.log").logger

    def __init__(self, public_api: PublicApi):
        self.stop_bot = None
        self.msg_listener = None
        self.callback = None
        self.popular_queries = None
        self.start = None
        try:
            self.__public_api = public_api
            load_dotenv("./client/telegram_bot_app/.env_tgbot")
            bot_token = getenv("BOT_TOKEN")
            self.bot: telebot.TeleBot = telebot.TeleBot(bot_token)
            self.__film_helper = FilmSearchHelper(public_api)
            self._my_films_dict: dict[int, UserFilms] = {}
            self.init_commands()
        except telebot.ExceptionHandler as err:
            self.__logger.error(err)
            exit()

    def start_app(self):
        self.__logger.info("Application started")
        try:
            self.bot.infinity_polling()
        except telebot.ExceptionHandler as err:
            self.__logger.error(err)
            exit()

    def init_commands(self):
        """Initialize methods to represent bot commands"""
        self.start = self.bot.message_handler(commands=["start"])(self.start_command)
        self.popular_queries = self.bot.message_handler(commands=["queries"])(self.send_popular_queries)
        self.callback = self.bot.callback_query_handler(func=lambda callback: True)(self.callback_command)
        self.msg_listener = self.bot.message_handler(func=lambda msg: True)(self.send_films_by_title)

    def start_command(self, message: telebot.types.Message):
        chat_id = message.chat.id
        markup = self.get_menu_buttons()
        films, count = self.__film_helper.get_all_films()
        user_films = UserFilms(user_id=message.chat.id, films=films)
        self._my_films_dict[message.chat.id] = user_films
        back_msg = msg_helper.get_films_simple_message(films)
        self.bot.send_message(chat_id=chat_id, text=back_msg)
        self.bot.send_message(chat_id=chat_id, text=constants.VIEW_FILM_DESCRIPTION_MSG,
                              reply_markup=markup)

    def callback_command(self, callback):
        if callback.data == constants.GET_POPULAR_QUERIES:
            self.send_popular_queries(callback.message)
        if callback.data == constants.MAIN_MENU:
            self.start(callback.message)
        if callback.data == constants.NEXT_FILM:
            user_films = self.__get_user_films_by_user_id(callback.message.chat.id)
            self.show_film_description(user_films.films_desc, callback.message)
        if callback.data == constants.SEARCH_FILM:
            self.show_search_menu(callback.message)
        if callback.data in constants.CONDITION_LIST:
            condition = {callback.data}
            self.__reset_user_films_data_and_take_values(callback.message, condition)
        if callback.data == constants.GENRE_YEAR_CONDITION:
            condition = {constants.GENRE_CONDITION, constants.YEAR_CONDITION}
            self.__reset_user_films_data_and_take_values(callback.message, condition)
        if callback.data in [constants.NEXT_PAGE, constants.LAST_PAGE, constants.PREVIOUS_PAGE, constants.FIRST_PAGE]:
            self.__change_page_number(callback)

    def __reset_user_films_data_and_take_values(self, message: telebot.types.Message, condition):
        user_films = self.__get_user_films_by_user_id(message.chat.id)
        user_films.curr_page = 0
        user_films.last_condition = {}
        self.take_multiple_conditions(message, conditions=condition)

    @staticmethod
    def __is_year(year: str) -> bool:
        return len(year) == 4 and year.isdecimal() and year[0] in ["1", "2"]

    @staticmethod
    def __is_rating(rating: str) -> bool:
        return rating.replace(".", "", 1).isdigit() and 0.0 <= float(rating) <= 10.0

    def take_multiple_conditions(self, message: telebot.types.Message, conditions: set[str]):
        self.bot.clear_step_handler(message)
        user_films = self.__get_user_films_by_user_id(message.chat.id)
        if conditions:
            condition = conditions.pop()
            if condition in constants.CONDITION_LIST:
                if condition == constants.RATING_CONDITION:
                    self.bot.send_message(message.chat.id, text=constants.RATING_FROM_TO_MSG)
                elif condition == constants.YEAR_CONDITION:
                    self.bot.send_message(message.chat.id, constants.ENTER_RELEASE_YEAR_MSG)
                else:
                    self.bot.send_message(message.chat.id, f"Enter \"{condition}\"")
            self.bot.register_next_step_handler(message, self.take_condition_value,
                                                condition=condition,
                                                user_films=user_films,
                                                conditions=conditions)
        else:
            self.bot.clear_step_handler(message)
            self.send_films_by_search_condition(message,
                                                offset=0, user_films=user_films)

    def take_condition_value(self, *args, **kwargs):
        message = args[0]
        condition: str = kwargs["condition"]
        conditions: set[str] = kwargs["conditions"]
        user_films = kwargs["user_films"]
        if condition == constants.YEAR_CONDITION:
            if not self.__is_year(message.text):
                conditions.add(condition)
                self.bot.send_message(message.chat.id, constants.INCORRECT_YEAR_VALUE_MSG)
                self.bot.register_next_step_handler(message, self.take_multiple_conditions, conditions)
        user_films.last_condition[condition] = message.text
        self.take_multiple_conditions(message, conditions)

    def send_films_by_title(self, message: telebot.types.Message):
        title = message.text.lower()
        user_films = self.__get_user_films_by_user_id(message.chat.id)
        if not user_films.films:
            user_films.films = self.__film_helper.get_all_films()[0]
        found_films = self.__film_helper.get_films_by_title(user_films.films, title)
        if not found_films:
            msg = constants.FILM_NOT_FOUND_MSG
            self.bot.send_message(message.chat.id, text=msg)
            self.start(message)
        user_films.films_desc = found_films
        self.show_film_description(user_films.films_desc, message)

    def __change_page_number(self, callback):
        user_films = self.__get_user_films_by_user_id(callback.message.chat.id)
        if callback.data == constants.NEXT_PAGE:
            user_films.curr_page += 1
        elif callback.data == constants.PREVIOUS_PAGE:
            user_films.curr_page -= 1
        elif callback.data == constants.LAST_PAGE:
            user_films.curr_page = user_films.last_page - 1
        elif callback.data == constants.FIRST_PAGE:
            user_films.curr_page = 0
        offset = user_films.curr_page
        self.send_films_by_search_condition(callback.message, offset=offset, user_films=user_films)

    def send_popular_queries(self, message: telebot.types.Message):
        queries = self.__film_helper.get_most_popular_queries()
        msg = msg_helper.get_pretty_queries_message(queries)
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(constants.MAIN_MENU_BUTTON)
        self.bot.send_message(message.chat.id, text=msg, reply_markup=markup)

    def send_films_by_search_condition(self, *arg, **kwargs):
        message = arg[0]
        offset = kwargs["offset"]
        user_films = kwargs["user_films"]
        films, count = self.__get_films(user_films, offset)
        if count > 1:
            markup = self.show_page_buttons(count, user_films.user_id)
            msg = msg_helper.get_films_simple_message(films)
        else:
            msg = constants.FILM_NOT_FOUND_MSG
            if films:
                msg = msg_helper.get_films_simple_message(films)
            markup = self.get_search_buttons()
        self.bot.send_message(message.chat.id, msg, reply_markup=markup)

    def show_page_buttons(self, count: int, user_id) -> telebot.types.InlineKeyboardMarkup:
        user_films = self.__get_user_films_by_user_id(user_id)
        markup = telebot.types.InlineKeyboardMarkup()
        if user_films.curr_page == 0:
            markup.row(constants.NEXT_PAGE_BUTTON, constants.LAST_PAGE_BUTTON)
            markup.row(constants.MAIN_MENU_BUTTON, constants.SEARCH_FILM_BUTTON)
            return markup
        elif user_films.curr_page == count - 1:
            markup.row(constants.FIRS_PAGE_BUTTON, constants.PREVIOUS_PAGE_BUTTON)
            markup.row(constants.MAIN_MENU_BUTTON, constants.SEARCH_FILM_BUTTON)
            return markup
        else:
            markup.row(constants.FIRS_PAGE_BUTTON, constants.PREVIOUS_PAGE_BUTTON,
                       constants.NEXT_PAGE_BUTTON, constants.LAST_PAGE_BUTTON)
            markup.row(constants.MAIN_MENU_BUTTON, constants.SEARCH_FILM_BUTTON)
        return markup

    def show_film_description(self, films: list[Film], message: telebot.types.Message):
        if films:
            if len(films) > 1:
                photo_url, msg = msg_helper.get_film_description_message(films[0])
                films.pop(0)
                markup = self.get_menu_buttons()
                markup.row(constants.NEXT_FILM_BUTTON)
                self.bot.send_photo(message.chat.id, photo_url, caption=msg, reply_markup=markup)
            else:
                markup = self.get_menu_buttons()
                photo_url, msg = msg_helper.get_film_description_message(films[0])
                self.bot.send_photo(message.chat.id, photo_url, caption=msg, reply_markup=markup)

    def show_search_menu(self, message: telebot.types.Message):
        msg = constants.CHOOSE_SEARCH_CONDITION_MSG
        markup = self.get_search_buttons()
        self.bot.send_message(message.chat.id, text=msg, reply_markup=markup)

    @staticmethod
    def get_menu_buttons() -> telebot.types.InlineKeyboardMarkup:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(constants.SEARCH_FILM_BUTTON)
        markup.row(constants.MAIN_MENU_BUTTON)
        return markup

    @staticmethod
    def get_search_buttons() -> telebot.types.InlineKeyboardMarkup:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.row(constants.KEYWORD_BUTTON, constants.GENRE_YEAR_BUTTON)
        markup.row(constants.MAIN_MENU_BUTTON)
        return markup

    def __get_user_films_by_user_id(self, user_id) -> UserFilms:
        if self._my_films_dict.get(user_id) is None:
            user_films = UserFilms(user_id=user_id, films=[])
            self._my_films_dict[user_id] = user_films
            return user_films
        return self._my_films_dict[user_id]

    def __get_films(self, user_films: UserFilms, offset) -> tuple[list[Film], int]:
        length = len(user_films.last_condition)
        if length < 1:
            msg = constants.NO_SEARCH_CONDITIONS_MSG
            markup = self.get_search_buttons()
            self.bot.send_message(user_films.user_id, text=msg, reply_markup=markup)
        if length == 1:
            condition, value = next(iter(user_films.last_condition.items()))
            films, count = self.__film_helper.get_film_by_one_condition(condition, value, offset)
        else:
            films, count = self.__film_helper.get_films_by_conditions(user_films.last_condition, offset)
        user_films.films = films
        user_films.last_page = count
        return films, count
