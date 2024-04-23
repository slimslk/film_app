from abc import ABC, abstractmethod

from mysql.connector import Connect


class DatasourceInterface(ABC):

    @classmethod
    @abstractmethod
    def connect_to_db(cls, db_name: str) -> Connect:
        ...
