GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
PURPLE = "\033[035m"

TITLE = "title"
GENRE = "genre"
RATING = "rating"
CAST = "cast"
YEAR = "year"
KEYWORD = "keyword"
ALL = "all"
MULTI = "multi"
MAIN_MENU = "main menu"

MAIN_MENU_COMMAND = "main menu"
HASH_DELIMITER = "#" * 200
LINE_DELIMITER = "-" * 200

GREETING_MESSAGE = "Welcome to film recommendation"
SEARCH_OR_DESCRIPTION_MESSAGE = (f"To view a list of the {BLUE}10{RESET} most popular queries,"
                                 f" enter \"{YELLOW}/queries{RESET}\" or \"{YELLOW}/exit{RESET}\" to "
                                 f"to exit our application\n"
                                 f"Enter \"{BLUE}/search{RESET}\" to start film searching or enter "
                                 f"{BLUE}THE TITLE OF A MOVIE{RESET} from the list to display the movie description: ")
FIND_FILMS_MESSAGE = "Found {color}{len}{reset} films with a similar {color_2}\"{inp}\"{reset} in the title"
SELECT_SEARCH_CONDITION_MESSAGE = f"Please select a search condition from the list below"
SEARCH_CONDITION_LIST = (f"{BLUE}{TITLE.upper():^10}{RESET}|{BLUE}{GENRE.upper():^10}{RESET}|"
                         f"{BLUE}{RATING.upper():^10}{RESET}|"f"{BLUE}{CAST.upper():^10}{RESET}|"
                         f"{BLUE}{YEAR.upper():^10}{RESET}|{BLUE}{KEYWORD.upper():^11}{RESET}|"
                         )
SEARCH_CONDITION_LIST_FULL = (f"{SEARCH_CONDITION_LIST}{BLUE}{ALL.upper():^10}{RESET}|{BLUE}{MULTI.upper():^11}{RESET}|"
                              f"{BLUE}{MAIN_MENU.upper():^11}{RESET}")
BYE_BYE_MESSAGE = f"{GREEN}Thank you for using our movie search app!{RESET}"

CURRENT_PAGE_LEFT = f"{YELLOW}<<{RESET}  {GREEN}<{RESET}"
CURRENT_PAGE_RIGHT = f"{GREEN}>{RESET}  {YELLOW}>>{RESET}"
FILMS_FOUND_MENU_MESSAGE = (f"{BLUE}{MAIN_MENU.upper()}{RESET}  |  {BLUE}SEARCH{RESET}  |"
                            f"  \"{BLUE}FILM TITLE{RESET}\"")
PRESS_ENTER_TO_MAIN_MENU_MESSAGE = f"Press {BLUE}Enter{RESET} to return to Main Menu"
