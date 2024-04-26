from mysql.connector import connect, Error as MySqlError
from mysql.connector.abstracts import MySQLConnectionAbstract

from server.dao.datasource_abstract import DatasourceInterface
from logger import Logger


class MySqlDataSource(DatasourceInterface):
    __logger = Logger("MySqlDatasource.class", "./logs/server_app_error.log").logger

    def __init__(self, user: str, password: str, host: str, port: str):
        self.__dbconfig = {"user": user, "password": password, "host": host, "port": port}

    def connect_to_db(self, db_name: str) -> MySQLConnectionAbstract:
        try:
            self.__dbconfig["database"] = db_name
            connection = connect(**self.__dbconfig)
            self.__logger.info(f"Connection to the {db_name} is established")
        except MySqlError as err:
            self.__logger.error(f"Unable to create a connection to the database.\n {err}")
            raise MySqlError()
        return connection
