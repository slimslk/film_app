from telebot.types import InlineKeyboardButton

KEYWORD_CONDITION = "keyword"
GENRE_CONDITION = "genre"
YEAR_CONDITION = "year"
RATING_CONDITION = "rating"
GENRE_YEAR_CONDITION = "genre_year"


CONDITION_LIST = [KEYWORD_CONDITION, YEAR_CONDITION, GENRE_CONDITION, RATING_CONDITION]

MAIN_MENU_BUTTON = InlineKeyboardButton(text="Main menu", callback_data="main_menu")
NEXT_PAGE_BUTTON = InlineKeyboardButton(text="Next page", callback_data="next_page")
LAST_PAGE_BUTTON = InlineKeyboardButton(text="Last page", callback_data="last_page")
PREVIOUS_PAGE_BUTTON = InlineKeyboardButton(text="Previous page", callback_data="prev_page")
FIRS_PAGE_BUTTON = InlineKeyboardButton(text="First page", callback_data="first_page")
NEXT_FILM_BUTTON = InlineKeyboardButton(text="Next film", callback_data="next_film")
# COMMON_QUERIES_BUTTON = InlineKeyboardButton(text="Most common queries",
#                                              callback_data="get_common_queries")
SEARCH_FILM_BUTTON = InlineKeyboardButton(text="Search film", callback_data="search")
TITLE_BUTTON = InlineKeyboardButton(text="Title", callback_data="title")
YEAR_BUTTON = InlineKeyboardButton(text="Year", callback_data="year")
GENRE_BUTTON = InlineKeyboardButton(text="Genre", callback_data="genre")
CAST_BUTTON = InlineKeyboardButton(text="Cast", callback_data="cast")
RATING_BUTTON = InlineKeyboardButton(text="Rating", callback_data="rating")
KEYWORD_BUTTON = InlineKeyboardButton(text="Keyword", callback_data=KEYWORD_CONDITION)
GENRE_YEAR_BUTTON = InlineKeyboardButton(text="Genres and Year", callback_data=GENRE_YEAR_CONDITION)
PAGE_NUMBER_BUTTON = InlineKeyboardButton(text="Hello", callback_data="None")
