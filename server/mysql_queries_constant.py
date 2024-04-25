MAX_FILMS = 10
MAX_QUERIES = 15
ORDER_DIR = "DESC"

DEFAULT_CONDITION = "SELECT *, COUNT(*) OVER () as film_amount FROM movies"
TITLE_CONDITION = "title LIKE %s"
GENRE_CONDITION = "genres LIKE %s"
RATING_CONDITION = "`imdb.rating` = %s"
ACTOR_NAME_CONDITION = "cast LIKE %s"
KEYWORD_CONDITION = """title LIKE %s OR
                                plot LIKE %s OR
                                genres LIKE %s OR
                                directors LIKE %s OR
                                cast LIKE %s"""
YEAR_CONDITION = "year = %s"
LIMIT_CONDITION = f"LIMIT {MAX_FILMS} OFFSET %s;"

ORDER_CONDITION = f"ORDER BY `imdb.rating` {ORDER_DIR}"

GET_FILMS_QUERY = f"{DEFAULT_CONDITION} {ORDER_CONDITION} {LIMIT_CONDITION};"
GET_FILMS_BY_TITLE_QUERY = f"{DEFAULT_CONDITION} WHERE {TITLE_CONDITION} {ORDER_CONDITION} {LIMIT_CONDITION};"
GET_FILMS_BY_GENRE_QUERY = f"{DEFAULT_CONDITION} WHERE {GENRE_CONDITION} {ORDER_CONDITION} {LIMIT_CONDITION};"
GET_FILMS_BY_RATING_QUERY = f"{DEFAULT_CONDITION} WHERE {RATING_CONDITION} {ORDER_CONDITION} {LIMIT_CONDITION};"
GET_FILMS_BY_ACTOR_NAME_QUERY = f"{DEFAULT_CONDITION} WHERE {ACTOR_NAME_CONDITION} {ORDER_CONDITION} {LIMIT_CONDITION};"
GET_FILMS_BY_KEYWORD_QUERY = f"{DEFAULT_CONDITION} WHERE {KEYWORD_CONDITION} {ORDER_CONDITION} {LIMIT_CONDITION};"
GET_FILMS_BY_YEAR_QUERY = f"{DEFAULT_CONDITION} WHERE {YEAR_CONDITION} {ORDER_CONDITION} {LIMIT_CONDITION};"

GET_ALL_USER_QUERIES = "SELECT * FROM movies_info;"
GET_MOST_COMMON_USER_QUERIES_BY_DESC_ORDER = f"""SELECT user_query, COUNT(user_query) AS amount_of_queries
                                                FROM movies_info
                                                GROUP BY user_query
                                                ORDER BY amount_of_queries DESC
                                                LIMIT {MAX_QUERIES};"""
ADD_USER_QUERIES = "INSERT INTO movies_info (user_query, date) VALUES (%s, %s)"
DELETE_USER_QUERY_BY_ID = "DELETE FROM movies_info WHERE id = %s"

GENRES_SET = (
    "drama", "comedy", "thriller", "music", "action", "adventure", "family",
    "romance", "documentary", "mystery", "sci-fi", "biography", "horror",
    "fantasy", "animation", "crime", "sport", "war", "short", "history",
    "news", "western", "musical"
)
