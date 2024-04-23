from abc import ABC, abstractmethod


class FilmDaoInterface(ABC):

    @abstractmethod
    def get_films(self, page: int) -> list[tuple]:
        ...

    @abstractmethod
    def get_film_by_title(self, title: str, page: int = 0) -> list[tuple]:
        ...

    @abstractmethod
    def get_films_by_genre(self, genre: str, page: int = 0) -> list[tuple]:
        ...

    @abstractmethod
    def get_films_by_rating(self, rating: float, page: int = 0) -> list[tuple]:
        ...

    @abstractmethod
    def get_films_by_actor(self, actor_name: str, page: int = 0) -> list[tuple]:
        ...

    @abstractmethod
    def get_films_by_keyword(self, keyword: str, page: int = 0) -> list[tuple]:
        ...

    @abstractmethod
    def get_films_by_year(self, year: int, page: int = 0) -> list[tuple]:
        ...

    @abstractmethod
    def get_films_by_mult_conditions(self, title: str = "",
                                     genre: str = "",
                                     rating: float = -1,
                                     cast: str = "",
                                     year: int = 0,
                                     keyword: str = "", page: int = 0):
        ...
