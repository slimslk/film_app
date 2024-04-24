from os import getenv
from dotenv import load_dotenv

from server.api.public_api import PublicApi
from server.dao.impl.mysql_film_dao_impl import MySqlFilmDaoImpl
from server.dao.impl.mysql_user_query_dao_impl import MySqlUserQueryDao
from server.dao.impl.mysql_datasource import MySqlDataSource
from server.service.film_search_service import FilmSearchService
from server.service.user_query_service import UserQueryService
from server.util.logger import Logger


class SearchFilmApp:
    __logger = Logger("MySqlDaoImpl").logger

    def __init__(self):
        self.__datasource = None
        self.__connection = None
        self.__user_query_dao = None
        self.__user_query_service = None
        self.__film_dao = None
        self.__film_service = None
        self.__public_api = None
        self.__init_app()

    def __init_app(self):
        load_dotenv()
        film_host = getenv("FILM_DB_HOST")
        film_port = getenv("FILM_DB_PORT")
        film_username = getenv("FILM_DB_USERNAME")
        film_password = getenv("FILM_DB_PASSWORD")
        film_database = getenv("FILM_DB_DATABASE")

        query_host = getenv("QUERY_DB_HOST")
        query_port = getenv("QUERY_DB_PORT")
        query_username = getenv("QUERY_DB_USERNAME")
        query_password = getenv("QUERY_DB_PASSWORD")
        query_database = getenv("QUERY_DB_DATABASE")

        self.__film_datasource = MySqlDataSource(host=film_host, port=film_port,
                                                 user=film_username, password=film_password)
        self.__query_datasource = MySqlDataSource(host=query_host, port=query_port,
                                                  user=query_username, password=query_password)

        self.__connection = {"film_db": self.__film_datasource.connect_to_db(film_database),
                             "query_db": self.__query_datasource.connect_to_db(query_database)}

        self.__user_query_dao = MySqlUserQueryDao(self.__connection["query_db"])
        self.__user_query_service = UserQueryService(self.__user_query_dao)

        self.__film_dao = MySqlFilmDaoImpl(self.__connection["film_db"])
        self.__film_service = FilmSearchService(self.__film_dao, self.__user_query_service)

        self.__public_api = PublicApi(self.__film_service, self.__user_query_service)

    @property
    def public_api(self):
        return self.__public_api

    def __del__(self):
        for key, db_connection in self.__connection.items():
            self.__logger.error(f"{key} connection close")
            if db_connection.is_connected():
                db_connection.close()

