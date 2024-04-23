from server.entity.film_model import Film
from server.entity.user_request_model import UserQuery


class Utils:

    @staticmethod
    def film_mapper(film_data: tuple) -> Film:
        film = Film(
            film_id=film_data[0],
            plot=film_data[1],
            genres=film_data[2],
            runtime=film_data[3],
            cast=film_data[4],
            poster=film_data[5],
            title=film_data[6],
            languages=film_data[7],
            directors=film_data[8],
            awards_text=film_data[9],
            year=film_data[10],
            imdb_rating=film_data[11],
            film_type=film_data[12]
        )
        return film

    @staticmethod
    def user_query_mapper(user_req_data: tuple) -> UserQuery:
        print(user_req_data)
        date = user_req_data[2]
        user_request = UserQuery(req_id=user_req_data[0],
                                 user_request=user_req_data[1],
                                 date=date)
        return user_request
