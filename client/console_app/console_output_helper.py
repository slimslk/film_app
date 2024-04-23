from server.entity.film_model import Film
import client.console_app.messages_constant as messages


def print_film_list(films: list[Film]):
    print(messages.LINE_DELIMITER)
    for film in films:
        print(f"{film.title[:60]:<60} | {str(film.genres):^50} | {film.year:^ 8} | {film.imdb_rating:^5} | {film.cast}")
    print(messages.LINE_DELIMITER)


def print_common_queries(queries: list[tuple]):
    print(messages.HASH_DELIMITER)
    for query, amount in queries:
        print(f"{messages.PURPLE}{query:^40}{messages.RESET}|{messages.PURPLE}{amount:^10}{messages.RESET}")
    print(messages.HASH_DELIMITER)
    input(messages.PRESS_ENTER_TO_MAIN_MENU_MESSAGE)
