from abc import ABC, abstractmethod
from datetime import datetime


class UserQueryDaoInterface(ABC):

    @abstractmethod
    def get_user_queries(self) -> list[tuple]:
        ...

    @abstractmethod
    def add_user_query(self, date: datetime, **kwargs):
        ...

    @abstractmethod
    def delete_user_query_by_id(self, query_id: int):
        ...

    @abstractmethod
    def get_most_common_queries(self) -> list[tuple[str, int]]:
        ...
