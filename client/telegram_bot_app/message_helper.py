from server.entity.film_model import Film


def get_films_simple_message(films: list[Film]) -> str:
    delimiter = "=" * 10
    output = f"\n{delimiter}\n".join([f"{film.title}" for film in films])
    return output


def get_pretty_queries_message(queries: list[tuple[str, int]]) -> str:
    delimiter = "-" * 50
    msg = f"\n{delimiter}\n".join([f"Query name: {data[0]}\nNumber of query: {data[1]}" for data in queries])
    output = f"{delimiter}\n{msg}\n{delimiter}\n"
    return output


def get_film_description_message(film: Film) -> tuple[str, str]:
    return film.poster, film.plot


def get_no_films_found() -> str:
    return f"Found 0 movies. Please try another search condition"


def get_no_search_conditions() -> str:
    return f"No search conditions selected"
