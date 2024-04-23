from client.console_app.console_search_film import ConsoleSearchFilmApp
from server.dao.impl.mysql_film_dao_impl import MySqlFilmDaoImpl
from server.dao.impl.mysql_user_query_dao_impl import MySqlUserQueryDao
from server.mysql_datasource import MySqlDataSource
from server.service.film_search_service import FilmSearchService
from server.service.user_query_service import UserQueryService

datasource = None
connection = None
film_dao = None
film_service = None
user_query_dao = None
user_query_service = None


def init():
    global datasource
    datasource = MySqlDataSource()
    global connection
    connection = datasource.connect_to_db("my_db")
    global user_query_dao
    user_query_dao = MySqlUserQueryDao(connection)
    global user_query_service
    user_query_service = UserQueryService(user_query_dao)
    global film_dao
    film_dao = MySqlFilmDaoImpl(connection)
    global film_service
    film_service = FilmSearchService(film_dao, user_query_service)


def tear_down():
    if connection:
        connection.close()


def main():
    init()

    console_app = ConsoleSearchFilmApp(user_query_service, film_service)
    console_app.main()

    # films, pages = film_service.get_all_films()
    # films, pages = film_service.get_all_films()
    # for film in films:
    #     print(film.title, film.genres, film.cast, film.directors)
    #
    # films, pages = film_service.get_films_by_year(2014)
    # for film in films:
    #     print(film.title, film.genres, film.cast, film.directors)
    # print("-" * 50)
    # user_query_service.insert_user_query(year=2014, rating=3)
    # print("-" * 50)
    # uq = user_query_service.get_most_common_queries()
    # for u_query, count in uq:
    #     print(f"{u_query:^40} | {count}")
    #
    # for i in range(8,20):
    #     user_query_service.delete_user_query_by_id(i)
    # print(f"pages: {pages}")
    # print("-" * 50)
    # films = film_service.get_all_films(1)
    # for film in films:
    #     print(film.title, film.genres, film.cast, film.directors)
    # print("-" * 50)
    # films = film_service.get_all_films(2)
    # for film in films:
    #     print(film.title, film.genres, film.cast, film.directors)
    # films = film_service.get_films_by_keyword("Mountains")
    # for film in films:
    #     print(film.title, film.genres, film.cast, film.directors)

    # print("-" * 50)
    # conditions = {"title": "",
    #               "genre": "Comedy",
    #               "rating": -1,
    #               "cast": "Tom",
    #               "year": 2014,
    #               "keyword": ""}
    # films, pages = film_service.get_films_by_conditions(**conditions)
    # print(f"pages: {pages}")
    # for film in films:
    #     print(film.year, film.title, film.genres, film.cast, film.directors)
    tear_down()


if __name__ == "__main__":
    main()
