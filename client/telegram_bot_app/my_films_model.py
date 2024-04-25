from server.entity.film_model import Film


class UserFilms:
    def __init__(self, user_id: int = 0, films: list[Film] = None, films_desc: list[Film] = None, curr_page: int = 0,
                 last_page: int = 0, last_condition: dict[str: str | float | int] = None):
        self.last_condition = {} if last_condition is None else last_condition
        self.__user_id = user_id
        self.__films = [] if films is None else films
        self.__films_desc = [] if films_desc is None else films_desc
        self.__curr_page = curr_page
        self.__last_page = last_page
        self.__last_condition = last_condition

    @property
    def user_id(self):
        return self.__user_id

    @property
    def films(self):
        return self.__films

    @property
    def films_desc(self):
        return self.__films_desc

    @property
    def curr_page(self):
        return self.__curr_page

    @property
    def last_page(self):
        return self.__last_page

    @property
    def last_condition(self):
        return self.__last_condition

    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @films.setter
    def films(self, films: list[Film]):
        self.__films = films

    @films_desc.setter
    def films_desc(self, films_desc: list[Film]):
        self.__films_desc = films_desc

    @curr_page.setter
    def curr_page(self, curr_page: int):
        self.__curr_page = curr_page

    @last_page.setter
    def last_page(self, last_page: int):
        self.__last_page = last_page

    @last_condition.setter
    def last_condition(self, last_condition: dict[str: str | float | int]) -> dict[str: str | float | int]:
        self.__last_condition = last_condition
