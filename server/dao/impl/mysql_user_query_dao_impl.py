from datetime import datetime

from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector import Error as MySqlError

from server.dao.user_query_dao_interface import UserQueryDaoInterface
from server.util.logger import Logger
from server import mysql_queries_constant as queries


class MySqlUserQueryDao(UserQueryDaoInterface):
    __logger = Logger("MySqlUserRequestDao").logger

    def __init__(self, connection: MySQLConnectionAbstract):
        self.__connection = connection

    def get_user_queries(self) -> list[tuple]:
        return self.__execute_read_query(queries.GET_ALL_USER_QUERIES)

    def add_user_query(self, date: datetime, **kwargs):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_query = MySqlUserQueryDao.__user_queries_mapper(**kwargs)
        arg = (user_query, date)
        self.__execute_write_query(queries.ADD_USER_QUERIES, arg)

    def delete_user_query_by_id(self, query_id: int):
        self.__execute_write_query(queries.DELETE_USER_QUERY_BY_ID, (query_id,))

    def get_most_common_queries(self) -> list[tuple]:
        return self.__execute_read_query(queries.GET_MOST_COMMON_USER_QUERIES_BY_DESC_ORDER)

    def __execute_read_query(self, query: str, arg: tuple | list | None = None):
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

    def __execute_write_query(self, query: str, arg: tuple | list | None = None):
        cursor = self.__connection.cursor()
        try:
            cursor.execute(query, arg)
            self.__connection.commit()
        except MySqlError as err:
            self.__logger.error(f"{err}")
            self.__connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def __user_queries_mapper(**kwargs) -> str:
        user_queries = []
        values = []
        for user_query, value in kwargs.items():
            user_queries.append(user_query)
            values.append(value)
        print(user_queries, values)
        return f"{'_'.join(user_queries)}: {', '.join(values)}"
