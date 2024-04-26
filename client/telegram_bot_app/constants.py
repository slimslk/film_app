from telebot.types import InlineKeyboardButton

MAIN_MENU = "main_menu"
NEXT_PAGE = "next_page"
LAST_PAGE = "last_page"
PREVIOUS_PAGE = "prev_page"
FIRST_PAGE = "first_page"
NEXT_FILM = "next_film"
SEARCH_FILM = "search"
GET_POPULAR_QUERIES = "get_common_queries"

TITLE_CONDITION = "title"
GENRE_CONDITION = "genre"
YEAR_CONDITION = "year"
CAST_CONDITION = "cast"
RATING_CONDITION = "rating"
KEYWORD_CONDITION = "keyword"
GENRE_YEAR_CONDITION = "genre_year"


CONDITION_LIST = [KEYWORD_CONDITION, YEAR_CONDITION, GENRE_CONDITION, RATING_CONDITION, CAST_CONDITION]

MAIN_MENU_BUTTON = InlineKeyboardButton(text="Main menu", callback_data=MAIN_MENU)
NEXT_PAGE_BUTTON = InlineKeyboardButton(text="Next page", callback_data=NEXT_PAGE)
LAST_PAGE_BUTTON = InlineKeyboardButton(text="Last page", callback_data=LAST_PAGE)
PREVIOUS_PAGE_BUTTON = InlineKeyboardButton(text="Previous page", callback_data=PREVIOUS_PAGE)
FIRS_PAGE_BUTTON = InlineKeyboardButton(text="First page", callback_data=FIRST_PAGE)
NEXT_FILM_BUTTON = InlineKeyboardButton(text="Next film", callback_data=NEXT_FILM)
# COMMON_QUERIES_BUTTON = InlineKeyboardButton(text="Most common queries",
#                                              callback_data="get_common_queries")
SEARCH_FILM_BUTTON = InlineKeyboardButton(text="Search film", callback_data="search")
TITLE_BUTTON = InlineKeyboardButton(text="Title", callback_data=TITLE_CONDITION)
YEAR_BUTTON = InlineKeyboardButton(text="Year", callback_data=YEAR_CONDITION)
GENRE_BUTTON = InlineKeyboardButton(text="Genre", callback_data=GENRE_CONDITION)
CAST_BUTTON = InlineKeyboardButton(text="Cast", callback_data=CAST_CONDITION)
RATING_BUTTON = InlineKeyboardButton(text="Rating", callback_data=RATING_CONDITION)
KEYWORD_BUTTON = InlineKeyboardButton(text="Keyword", callback_data=KEYWORD_CONDITION)
GENRE_YEAR_BUTTON = InlineKeyboardButton(text="Genres and Year", callback_data=GENRE_YEAR_CONDITION)

FILM_NOT_FOUND_MSG = "Found 0 movies. Please try another search condition"
NO_SEARCH_CONDITIONS_MSG = "No search conditions selected"
CHOOSE_SEARCH_CONDITION_MSG = "Please choose a search conditions"
INCORRECT_YEAR_VALUE_MSG = "Incorrect year value"
RATING_FROM_TO_MSG = "Enter rating value from 0.0 to 10.0"
ENTER_RELEASE_YEAR_MSG = "Enter release year"
VIEW_FILM_DESCRIPTION_MSG = "Enter name of the film to view the movie description"
