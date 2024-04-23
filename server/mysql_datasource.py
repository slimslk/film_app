from os import getenv

from mysql.connector import connect, Error as MySqlError
from mysql.connector.abstracts import MySQLConnectionAbstract
from dotenv import load_dotenv

from server.datasource_abstract import DatasourceInterface
from server.util.logger import Logger


class MySqlDataSource(DatasourceInterface):
    __logger = Logger("MySqlDatasource.class").logger
    __instance = None
    __dbconfig = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MySqlDataSource, cls).__new__(cls)
        load_dotenv()
        cls.__dbconfig = {
            "user": getenv("MYSQL_USERNAME"),
            "password": getenv("MYSQL_PASSWORD"),
            "host": getenv("MYSQL_HOST"),
            "port": getenv("MYSQL_PORT")
        }
        return cls.__instance

    @classmethod
    def connect_to_db(cls, db_name: str) -> MySQLConnectionAbstract:
        connection = None
        try:
            cls.__dbconfig["database"] = db_name
            connection = connect(**cls.__dbconfig)
            cls.__logger.info("Connection complete")
        except MySqlError as err:
            cls.__logger.error(f"Unable to create a connection to the database.\n {err}")
        return connection
