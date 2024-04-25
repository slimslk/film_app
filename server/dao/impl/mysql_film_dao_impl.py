from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector import Error as MySqlError

from server import mysql_queries_constant as queries
from server.dao.film_dao_interface import FilmDaoInterface
from logger import Logger


class MySqlFilmDaoImpl(FilmDaoInterface):
    __logger = Logger("MySqlFilmDaoImpl.class", "./logs/server_app_error.log").logger

    def __init__(self, connection: MySQLConnectionAbstract):
        self.__connection = connection

    def get_films(self, page: int = 0) -> list[tuple]:
        return self.__execute_query(queries.GET_FILMS_QUERY, (page * queries.MAX_FILMS,))

    def get_film_by_title(self, title: str, page: int = 0) -> list[tuple]:
        return self.__execute_query(queries.GET_FILMS_BY_TITLE_QUERY, (f"%{title}%", page * queries.MAX_FILMS))

    def get_films_by_genre(self, genre: str, page: int = 0) -> list[tuple]:
        return self.__execute_query(queries.GET_FILMS_BY_GENRE_QUERY, (f"%{genre}%", page * queries.MAX_FILMS))

    def get_films_by_rating(self, rating: float, page: int = 0) -> list[tuple]:
        return self.__execute_query(queries.GET_FILMS_BY_RATING_QUERY, (rating, page * queries.MAX_FILMS))

    def get_films_by_actor(self, actor_name: str, page: int = 0) -> list[tuple]:
        return self.__execute_query(queries.GET_FILMS_BY_ACTOR_NAME_QUERY,
                                    (f"%{actor_name}%", page * queries.MAX_FILMS))

    def get_films_by_keyword(self, keyword: str, page: int = 0) -> list[tuple]:
        keyword = f"%{keyword}%"
        keywords = (keyword, keyword, keyword, keyword, keyword, page * queries.MAX_FILMS)
        return self.__execute_query(queries.GET_FILMS_BY_KEYWORD_QUERY, keywords)

    def get_films_by_year(self, year: int, page: int = 0) -> list[tuple]:
        return self.__execute_query(queries.GET_FILMS_BY_YEAR_QUERY, (year, page * queries.MAX_FILMS))

    def get_films_by_mult_conditions(self,
                                     title: str = "",
                                     genre: str = "",
                                     rating: float = -1,
                                     cast: str = "",
                                     year: int = 0,
                                     keyword: str = "", page: int = 0) -> list[tuple]:
        conditions = {"title": title,
                      "genre": genre,
                      "rating": rating,
                      "cast": cast,
                      "year": year,
                      "keyword": keyword}
        query, args = MySqlFilmDaoImpl.__create_mult_query(conditions)
        args.append(page * queries.MAX_FILMS)
        return self.__execute_query(query, args)

    @staticmethod
    def __create_mult_query(conditions: dict) -> tuple[str, list]:
        args = []
        conditions_list = []
        for condition_type, value in conditions.items():
            if condition_type == "title" and value:
                conditions_list.append(queries.TITLE_CONDITION)
                args.append(f"%{value}%")
                continue
            if condition_type == "genre" and value:
                conditions_list.append(queries.GENRE_CONDITION)
                args.append(f"%{value}%")
                continue
            if condition_type == "rating" and value >= 0:
                conditions_list.append(queries.RATING_CONDITION)
                args.append(value)
                continue
            if condition_type == "cast" and value:
                conditions_list.append(queries.ACTOR_NAME_CONDITION)
                args.append(f"%{value}%")
                continue
            if condition_type == "year" and value:
                conditions_list.append(queries.YEAR_CONDITION)
                args.append(value)
                continue
            if condition_type == "keyword" and value:
                conditions_list.append(f"({queries.KEYWORD_CONDITION})")
                word = f"%{value}%"
                words = [word, word, word, word, word]
                args += words

        condition = " AND ".join(conditions_list)
        query = f"{queries.DEFAULT_CONDITION} WHERE {condition} {queries.LIMIT_CONDITION}"
        return query, args

    def __execute_query(self, query: str, arg: tuple | list | None = None) -> list:
        cursor = self.__connection.cursor()
        result = []
        try:
            cursor.execute(query, arg)
            result = cursor.fetchall()
        except MySqlError as err:
            self.__logger.error(f"{err}")
        finally:
            cursor.close()
        return result
