import client.console_app.console_input_helper as helper
import client.console_app.messages_constant as messages
import client.console_app.console_output_helper as output_helper
from client.console_app.console_app_logger import Logger
from server.entity.film_model import Film
from server.service.film_search_service import FilmSearchService
from server.service.user_query_service import UserQueryService
from enum import Enum


class Query(Enum):
    _order_ = "TITLE GENRE RATING CAST YEAR KEYWORD"
    TITLE = "title"
    GENRE = "genre"
    RATING = "rating"
    CAST = "cast"
    YEAR = "year"
    KEYWORD = "keyword"


class ConsoleSearchFilmApp:
    __logger = Logger("ConsoleSearchFilmApp").logger

    def __init__(self, user_query_service: UserQueryService, film_search_service: FilmSearchService):
        self.__film_search_service = film_search_service
        self.__user_query_service = user_query_service

    def main(self):
        while True:
            films = self.__greeting()
            if not self.__is_film_not_found(films):
                exit()
            command = input(f"{messages.SEARCH_OR_DESCRIPTION_MESSAGE}").lower()
            if command in ["\\quit", "\\exit", "\\stop"]:
                print(messages.BYE_BYE_MESSAGE)
                exit()
            if command == "\\queries":
                queries = self.__user_query_service.get_most_common_queries()
                output_helper.print_common_queries(queries)
                continue
            elif command == "\\search":
                self.__search_film()
                continue
            else:
                usr_input = helper.input_search_film(films, command)
                if type(usr_input) is list:
                    command = helper.input_film_title(usr_input)
                    if command == "main menu":
                        continue

    def __search_film(self):
        page_number = 0
        while True:
            if page_number == -2:
                return
            page_number = 0
            search_con_list = [e.value for e in Query]
            cur_search_con = helper.input_search_condition(search_con_list)
            if not cur_search_con:
                break
            films, count = self.__get_films_by_query(cur_search_con, page_number)
            if not self.__is_film_not_found(films):
                continue
            if count > 1:
                while True:
                    page_number = helper.input_film_page_or_film_title(films, count, page_number)
                    if page_number in [-1, -2]:
                        break
                    films, count = self.__get_films_by_query(cur_search_con, page_number)

    def __get_films_by_query(self, queries: dict[str: str | int | float] = None, page: int = 0) -> tuple[list[Film], int]:
        if len(queries) == 1:
            query, value = list(queries.items())[0]
            if query == "all":
                films, count = self.__film_search_service.get_all_films()
                return films, count
            elif query == Query.TITLE.value:
                films, count = self.__film_search_service.get_film_by_title(value, page)
                return films, count
            elif query == Query.GENRE.value:
                films, count = self.__film_search_service.get_films_by_genre(value, page)
                return films, count
            elif query == Query.RATING.value:
                films, count = self.__film_search_service.get_films_by_rating(value, page)
                return films, count
            elif query == Query.CAST.value:
                films, count = self.__film_search_service.get_films_by_actor(value, page)
                return films, count
            elif query == Query.KEYWORD.value:
                films, count = self.__film_search_service.get_films_by_keyword(value, page)
                return films, count
            elif query == Query.YEAR.value:
                films, count = self.__film_search_service.get_films_by_year(value, page)
                return films, count
        if len(queries) > 1:
            # conditions = {}
            # for key, value in queries.items():
            #     if key in [e.value for e in Query]:
            #         conditions[key] = value
            film, count = self.__film_search_service.get_films_by_conditions(**queries, offset=page)
            return film, count

    def __greeting(self) -> list[Film]:
        print(f"{messages.GREETING_MESSAGE:^150}")
        films, count = self.__get_films_by_query({"all": -1})
        self.__print_film_list(films)
        return films

    @staticmethod
    def __print_film_list(films: list[Film]):
        print(messages.LINE_DELIMITER)
        for film in films:
            print(f"{film.title[:60]:<60} | {str(film.genres):^50} | {film.year:^ 8} | {film.imdb_rating:^5} | {film.cast}")
        print(messages.LINE_DELIMITER)

    @staticmethod
    def __is_film_not_found(films: list[Film]) -> bool:
        if not films:
            print(f"{messages.RED}Films not found!{messages.RESET}. Try another query!")
            return False
        return True


