import client.console_app.console_output_helper as output_helper
import client.console_app.messages_constant as messages
from server.entity.film_model import Film


def search_film_by_title(films: list[Film], film_title) -> list[Film]:
    found_films = []
    for film in films:
        if film_title and film_title in film.title.lower():
            found_films.append(film)
    return found_films


def input_search_film(films: list[Film], title: str) -> list[Film]:
    found_films = search_film_by_title(films, title)
    if found_films:
        print(messages.FIND_FILMS_MESSAGE.format(len=len(found_films),
                                                 inp=title,
                                                 color=messages.GREEN,
                                                 color_2=messages.BLUE,
                                                 reset=messages.RESET))
        return found_films
    print(messages.FIND_FILMS_MESSAGE.format(len=len(found_films),
                                             inp=title,
                                             color=messages.RED,
                                             color_2=messages.BLUE,
                                             reset=messages.RESET))


def input_film_title(films: list[Film], title: str) -> str:
    if not films:
        print(messages.HASH_DELIMITER)
        print(messages.FIND_FILMS_MESSAGE.format(len=len(films),
                                                 inp=title,
                                                 color=messages.RED,
                                                 color_2=messages.BLUE,
                                                 reset=messages.RESET))
        return messages.MAIN_MENU_COMMAND
    length = len(films)
    if length > 1:
        for i in range(length - 1):
            print_film_description(films[i])
            command = input(
                f"Press \"{messages.BLUE}Enter{messages.RESET}\" to show next film description or"
                f" enter \"{messages.BLUE}quit{messages.RESET}\" to exit film description: ")
            if command.lower() == "quit":
                return messages.MAIN_MENU_COMMAND
        else:
            print_film_description(films[length - 1])
        input(f"Press {messages.BLUE}Enter{messages.RESET} to to exit film description.")
        return messages.MAIN_MENU_COMMAND
    else:
        print_film_description(films[0])
        input(f"Press {messages.BLUE}Enter{messages.RESET} to to exit film description.")
        return messages.MAIN_MENU_COMMAND


def input_search_condition(search_con_list: list[str]) -> dict[str: str]:
    while True:
        print(messages.HASH_DELIMITER)
        print(messages.SELECT_SEARCH_CONDITION_MESSAGE)
        print(messages.SEARCH_CONDITION_LIST_FULL)
        condition = input("Enter condition: ").lower()
        if condition.lower() == "main menu":
            return {}
        if condition in search_con_list:
            return inp_cond_search(condition)
        if condition == "all":
            return {condition: -1}
        if condition == "multi":
            multi_condition = {}
            print(f"Choose conditions from the list: ")
            while True:
                print(messages.SEARCH_CONDITION_LIST)
                condition = input("Enter the condition from the list or press enter to exit: ")
                if not condition:
                    return multi_condition
                cond = inp_cond_search(condition)
                multi_condition = multi_condition | cond
                if not multi_condition:
                    print(f"Conditions: {messages.YELLOW}None{messages.RESET}")
                    continue
                print(f"Conditions:", end=" ")
                for key, value in multi_condition.items():
                    print(f"{messages.YELLOW}{key.capitalize()} = {value}{messages.RESET}", end=" ")
                print(f"\n{messages.LINE_DELIMITER}")


def inp_cond_search(condition: str) -> dict[str: str]:
    while True:
        condition = condition.lower()
        if condition in ["title", "genre", "actor", "cast", "keyword"]:
            value = input("Enter the condition value: ")
            return {condition: value}
        elif condition == "rating":
            while True:
                rating = input(f"Enter rating value from {messages.YELLOW}0.0{messages.RESET}"
                               f" to {messages.YELLOW}10.0{messages.RESET}: ")
                if is_correct_rating(rating):
                    return {condition: float(rating)}
                print("Incorrect rating value. Try again.")
        elif condition == "year":
            while True:
                year = input("Enter release year: ")
                if is_correct_year(year):
                    return {condition: int(year)}
                print("Incorrect year value. Try again.")
        else:
            print(messages.LINE_DELIMITER)
            print(f"{messages.YELLOW}{condition}{messages.RESET} - Incorrect condition name! Try again.")
            return {}


def input_film_page_or_film_title(films: list[Film], count, page_number) -> int:
    print(count)
    while True:
        print(messages.HASH_DELIMITER)
        output_helper.print_film_list(films)
        page_msg = f"{messages.BLUE}{page_number + 1}/{count}{messages.RESET}"
        if page_number == 0:
            page_msg = f"{page_msg}  {messages.CURRENT_PAGE_RIGHT}"
        elif page_number == count - 1:
            page_msg = f"{messages.CURRENT_PAGE_LEFT}  {page_msg}"
        else:
            page_msg = f"{messages.CURRENT_PAGE_LEFT}  {page_msg}  {messages.CURRENT_PAGE_RIGHT:}"
        print(f"{page_msg}")
        print(f"{messages.FILMS_FOUND_MENU_MESSAGE}")
        command = input(f"Enter {messages.BLUE}\"<<\"{messages.RESET}, {messages.BLUE}\"<\"{messages.RESET},"
                        f" {messages.BLUE}\">\"{messages.RESET}, {messages.BLUE}\">>\"{messages.RESET},"
                        f" number between {messages.BLUE}1{messages.RESET} and {messages.BLUE}{count}{messages.RESET}"
                        f" or select command from menu above: ").lower()
        if not command:
            continue
        elif command == "search":
            return -1
        elif command == "main menu":
            return -2
        elif command == "<<":
            if page_number == 0:
                continue
            return 0
        elif command == "<":
            if page_number == 0:
                continue
            return page_number - 1
        elif command == ">>":
            if page_number == count - 1:
                continue
            return count - 1
        elif command == ">":
            if page_number == count - 1:
                continue
            return page_number + 1
        elif command.isdecimal():
            if not int(command) in range(1, count + 1):
                continue
            return int(command) - 1
        elif command:
            found_films = search_film_by_title(films, command)
            input_film_title(found_films, command)


def is_correct_year(year: str) -> bool:
    return len(year) == 4 and year.isdecimal() and year[0] in ["1", "2"]


def is_correct_rating(rating: str) -> bool:
    return rating.replace(".", "", 1).isdigit() and 0.0 <= float(rating) <= 10.0


def print_film_description(film: Film):
    print(messages.HASH_DELIMITER)
    print(f"{film.title:<50}, runtime: {film.runtime:^6}, {film.genres}")
    print(messages.LINE_DELIMITER)
    print(f"Description: {film.plot}")
    print(messages.LINE_DELIMITER)
    print(f"cast: {film.cast:<50}, directors: {film.directors}")
    print(messages.HASH_DELIMITER)
