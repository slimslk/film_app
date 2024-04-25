from client.telegram_bot_app import constants
from server.api.public_api import PublicApi
from server.entity.film_model import Film


class FilmSearchHelper:

    def __init__(self, public_api: PublicApi):
        self.__public_api: PublicApi = public_api

    def get_film_by_one_condition(self, condition: str,
                                  value: str | float | int, offset: int = 0) -> tuple[list[Film], int]:
        if condition == constants.KEYWORD_CONDITION:
            return self.get_films_by_keyword(value, offset)
        if condition == constants.RATING_CONDITION:
            return self.get_films_by_rating(value, offset)
        if condition == constants.YEAR_CONDITION:
            return self.get_films_by_year(value, offset)

    def get_most_popular_queries(self) -> list[tuple[str, int]]:
        return self.__public_api.get_most_common_queries()

    def get_all_films(self) -> tuple[list[Film], int]:
        return self.__public_api.get_all_films()

    def get_films_by_keyword(self, keyword: str, offset: int = 0) -> tuple[list[Film], int]:
        return self.__public_api.get_films_by_keyword(keyword, offset)

    def get_films_by_rating(self, rating: float, offset: int = 0) -> tuple[list[Film], int]:
        return self.__public_api.get_films_by_rating(rating, offset)

    def get_films_by_year(self, year: int, offset: int = 0) -> tuple[list[Film], int]:
        return self.__public_api.get_films_by_year(year, offset)

    def get_films_by_conditions(self, conditions: dict[str: str | float | int],
                                offset: int = 0) -> tuple[list[Film], int]:
        conditions = dict(filter(lambda condition: condition[0] in constants.CONDITION_LIST, conditions.items()))
        return self.__public_api.get_films_by_conditions(**conditions, offset=offset)

    @staticmethod
    def get_films_by_title(films: list[Film], title) -> list[Film]:
        found_films = []
        for film in films:
            if title and title in film.title.lower():
                found_films.append(film)
        return found_films
