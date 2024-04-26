from server.dao.film_dao_interface import FilmDaoInterface
from server.entity.film_model import Film
from server.service.user_query_service import UserQueryService
from server.util.utils import Utils
from server.mysql_queries_constant import MAX_FILMS, GENRES_SET
from math import ceil


class FilmSearchService:

    def __init__(self, film_dao: FilmDaoInterface, user_query_service: UserQueryService):
        self.__film_dao = film_dao
        self.__user_query_service = user_query_service

    def get_all_films(self, offset: int = 0) -> tuple[list[Film], int]:
        film_data = self.__film_dao.get_films(page=offset)
        return FilmSearchService.__get_films_with_pages(film_data)

    def get_film_by_title(self, title: str, offset: int = 0) -> tuple[list[Film], int]:
        film_data = self.__film_dao.get_film_by_title(title, offset)
        if not offset:
            self.__user_query_service.insert_user_query(title=title)
        return FilmSearchService.__get_films_with_pages(film_data)

    def get_films_by_genre(self, genres: str, offset: int = 0) -> tuple[list[Film], int]:
        gnr = self.__get_genres(genres.lower())
        film_data = self.__film_dao.get_films_by_genre(gnr, offset)
        if not offset:
            self.__user_query_service.insert_user_query(genre=gnr)
        return FilmSearchService.__get_films_with_pages(film_data)

    def get_films_by_rating(self, rating: float, offset: int = 0) -> tuple[list[Film], int]:
        film_data = self.__film_dao.get_films_by_rating(rating, offset)
        if not offset:
            self.__user_query_service.insert_user_query(rating=rating)
        return FilmSearchService.__get_films_with_pages(film_data)

    def get_films_by_actor(self, cast: str, offset: int = 0) -> tuple[list[Film], int]:
        film_data = self.__film_dao.get_films_by_actor(cast, offset)
        if not offset:
            self.__user_query_service.insert_user_query(cast=cast)
        return FilmSearchService.__get_films_with_pages(film_data)

    def get_films_by_keyword(self, keyword: str, offset: int = 0) -> tuple[list[Film], int]:
        film_data = self.__film_dao.get_films_by_keyword(keyword, offset)
        if not offset:
            self.__user_query_service.insert_user_query(keyword=keyword.lower())
        return FilmSearchService.__get_films_with_pages(film_data)

    def get_films_by_year(self, year: int, offset: int = 0) -> tuple[list[Film], int]:
        film_data = self.__film_dao.get_films_by_year(year, offset)
        if not offset:
            self.__user_query_service.insert_user_query(year=year)
        return FilmSearchService.__get_films_with_pages(film_data)

    def get_films_by_conditions(self, title: str = "",
                                genres: str = "",
                                rating: float = -1,
                                cast: str = "",
                                year: int = 0,
                                keyword: str = "", offset: int = 0) -> tuple[list[Film], int]:
        """
            The conditions should have the following construction:
            "title": str,
            "genre": str,
            "rating": float,
            "cast": str,
            "year": int,
            "keyword": str
            """
        gnr = self.__get_genres(genres.lower())
        film_data = self.__film_dao.get_films_by_mult_conditions(title, gnr, rating, cast, year, keyword, offset)
        self.__user_query_service.insert_user_query(title=title, genre=gnr, rating=rating,
                                                    cast=cast, year=year, keyword=keyword)
        return FilmSearchService.__get_films_with_pages(film_data)

    @staticmethod
    def __get_genres(genres: str) -> str:
        genre = ",".join(list(filter(lambda item: item in genres, GENRES_SET)))
        if not genre:
            genre = ""
        return genre

    @staticmethod
    def __convert_film_data_to_films_list(film_data: list[tuple]) -> list[Film]:
        return [Utils.film_mapper(film) for film in film_data]

    @staticmethod
    def __count_amount_of_pages(total_films: int) -> int:
        return ceil(total_films / MAX_FILMS)

    @staticmethod
    def __get_films_with_pages(film_data: list[tuple]):
        films_and_pages = ([], 0)
        if film_data:
            pages = FilmSearchService.__count_amount_of_pages(film_data[0][13])
            films = FilmSearchService.__convert_film_data_to_films_list(film_data)
            films_and_pages = (films, pages)
        return films_and_pages
