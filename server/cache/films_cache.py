import functools
from collections import OrderedDict

from server.entity.film_model import Film

MAX_CACHE_CAPACITY = 10

film_cache: OrderedDict[int, list[Film]] = OrderedDict()


def add_cache(query: str, value: str, films: list[Film]):
    value_hash = get_hash(query, value)
    if film_cache.get(value_hash) is None:
        film_cache[value_hash] = films
        if len(film_cache) > MAX_CACHE_CAPACITY:
            film_cache.popitem(last=False)


def update_cache(query: str, value: str, films: list[Film]):
    value_hash = get_hash(query, value)
    if film_cache.get(value_hash) is not None:
        film_cache[value_hash] = films


def get_cache(query: str, value: str) -> list[Film] | None:
    value_hash = get_hash(query, value)
    films = {}
    if film_cache.get(value_hash) is not None:
        films = film_cache.pop(value_hash)
        film_cache[value_hash] = films
    return films


def get_hash(query: str, value: str) -> int:
    string = query + value
    length = len(string)
    my_hash = 0
    for i in range(length):
        my_hash += ord(string[i]) * (31 ** length - i + 1)
    return my_hash


def cache(_func=None, *, query: str = ""):
    def decorator_cache(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            values = list(args)
            del values[0]
            value = "".join([str(item) for item in values])
            value += "".join([str(item) for item in kwargs.values()])
            films = get_cache(query, value)
            if films:
                return films
            films = func(*args, **kwargs)
            if films:
                add_cache(query, value, films)
            return films
        return wrapper
    if _func is None:
        return decorator_cache
    else:
        return decorator_cache(_func)
