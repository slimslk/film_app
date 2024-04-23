from datetime import datetime

from server.entity.user_request_model import UserQuery
from server.util.utils import Utils
from server.dao.user_query_dao_interface import UserQueryDaoInterface


class UserQueryService:

    def __init__(self, user_query_dao: UserQueryDaoInterface):
        self.__user_query_dao = user_query_dao

    def get_user_queries(self) -> list[UserQuery]:
        user_query_data = self.__user_query_dao.get_user_queries()
        return UserQueryService.__convert_user_query_data_to_user_query(user_query_data)

    def get_most_common_queries(self) -> list[tuple[str, int]]:
        return self.__user_query_dao.get_most_common_queries()

    def insert_user_query(self, title: str = "",
                          genre: str = "",
                          rating: float = -1,
                          cast: str = "",
                          year: int = 0,
                          keyword: str = ""):
        cur_date = datetime.now()
        query_dict = UserQueryService.__prepare_queries(title=title,
                                                        genre=genre,
                                                        rating=rating,
                                                        cast=cast,
                                                        year=year,
                                                        keyword=keyword)
        self.__user_query_dao.add_user_query(cur_date, **query_dict)

    def delete_user_query_by_id(self, user_query_id: int):
        self.__user_query_dao.delete_user_query_by_id(user_query_id)

    @staticmethod
    def __convert_user_query_data_to_user_query(user_queries_data: list[tuple]) -> list[UserQuery]:
        return [Utils.user_query_mapper(uq_data) for uq_data in user_queries_data]

    @staticmethod
    def __prepare_queries(**kwargs) -> dict:
        result = {}
        for key, value in kwargs.items():
            if key == "rating" and value <= 0:
                continue
            elif value:
                result[key] = str(value).lower()
        return result
