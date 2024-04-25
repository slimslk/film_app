from server.entity.film_model import Film
from server.service.film_search_service import FilmSearchService
from server.service.user_query_service import UserQueryService


class PublicApi:
    def __init__(self, search_film_service: FilmSearchService, user_query_service: UserQueryService):
        self.__user_query_service = user_query_service
        self.__search_film_service = search_film_service

    def get_all_films(self, offset: int = 0) -> tuple[list[Film], int]:
        return self.__search_film_service.get_all_films(offset)

    def get_film_by_title(self, title: str, offset: int = 0) -> tuple[list[Film], int]:
        return self.__search_film_service.get_film_by_title(title, offset)

    def get_films_by_genre(self, genre: str, offset: int = 0) -> tuple[list[Film], int]:
        return self.__search_film_service.get_films_by_genre(genre, offset)

    def get_films_by_rating(self, rating: float, offset: int = 0) -> tuple[list[Film], int]:
        return self.__search_film_service.get_films_by_rating(rating, offset)

    def get_films_by_actor(self, cast: str, offset: int = 0) -> tuple[list[Film], int]:
        return self.__search_film_service.get_films_by_actor(cast, offset)

    def get_films_by_keyword(self, keyword: str, offset: int = 0) -> tuple[list[Film], int]:
        return self.__search_film_service.get_films_by_keyword(keyword, offset)

    def get_films_by_year(self, year: int, offset: int = 0) -> tuple[list[Film], int]:
        return self.__search_film_service.get_films_by_year(year, offset)

    def get_films_by_conditions(self, title: str = "",
                                genre: str = "",
                                rating: float = -1,
                                cast: str = "",
                                year: int = 0,
                                keyword: str = "", offset: int = 0) -> tuple[list[Film], int]:
        return self.__search_film_service.get_films_by_conditions(title=title,
                                                                  genres=genre,
                                                                  rating=rating,
                                                                  cast=cast,
                                                                  year=year,
                                                                  keyword=keyword, offset=offset)

    def get_most_common_queries(self) -> list[tuple[str, int]]:
        return self.__user_query_service.get_most_common_queries()
