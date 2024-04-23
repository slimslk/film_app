class Film:
    def __init__(self, film_id, plot, genres, runtime, cast,
                 poster, title, languages, directors, awards_text,
                 year, imdb_rating, film_type):
        self.__film_type = film_type
        self.__imdb_rating = imdb_rating
        self.__year = year
        self.__awards_text = awards_text
        self.__directors = directors
        self.__languages = languages
        self.__title = title
        self.__poster = poster
        self.__cast = cast
        self.__runtime = runtime
        self.__genres = genres
        self.__plot = plot
        self.__film_id = film_id

    def __hash__(self):
        return hash((self.__plot, self.__title, self.directors, self.__cast, self.year, self.genres))

    def __eq__(self, other):
        if (other is None or
                self.__film_id != other.film_id or
                self.__imdb_rating != other.imdb_rating or
                self.__year != other.year or
                self.__awards_text != other.awards_text or
                self.__directors != other.directors or
                self.__languages != other.languages or
                self.__title != other.title or
                self.__poster != other.poster or
                self.__cast != other.cast or
                self.__runtime != other.runtime or
                self.__genres != other.genres or
                self.__plot != other.plot or
                self.__film_type != other.film_type):
            return False
        else:
            return True

    def __str__(self):
        ...

    @property
    def film_type(self):
        return self.__film_type

    @property
    def imdb_rating(self):
        return self.__imdb_rating

    @property
    def year(self):
        return self.__year

    @property
    def awards_text(self):
        return self.__awards_text

    @property
    def directors(self):
        return self.__directors

    @property
    def languages(self):
        return self.__languages

    @property
    def title(self):
        return self.__title

    @property
    def poster(self):
        return self.__poster

    @property
    def cast(self):
        return self.__cast

    @property
    def runtime(self):
        return self.__runtime

    @property
    def genres(self):
        return self.__genres

    @property
    def plot(self):
        return self.__plot

    @property
    def film_id(self):
        return self.__film_id

    @film_type.setter
    def film_type(self, film_type):
        self.__film_type = film_type

    @imdb_rating.setter
    def imdb_rating(self, imdb_rating):
        self.__imdb_rating = imdb_rating

    @year.setter
    def year(self, year):
        self.__year = year

    @awards_text.setter
    def awards_text(self, awards_text):
        self.__awards_text = awards_text

    @directors.setter
    def directors(self, directors):
        self.__directors = directors.split(", ")

    @languages.setter
    def languages(self, languages):
        self.__languages = languages.split(", ")

    @title.setter
    def title(self, title):
        self.__title = title

    @poster.setter
    def poster(self, poster):
        self.__poster = poster

    @cast.setter
    def cast(self, cast):
        self.__cast = cast.split(", ")

    @runtime.setter
    def runtime(self, runtime):
        self.__runtime = runtime

    @genres.setter
    def genres(self, genres):
        self.__genres = genres.split(",")

    @plot.setter
    def plot(self, plot):
        self.__plot = plot

    @film_id.setter
    def film_id(self, film_id):
        self.__film_id = film_id

    def append_cast(self, cast: str):
        self.__cast = self.__cast + cast.split(", ")

    def append_genres(self, genres: str):
        self.__genres = self.__genres + genres.split(",")

    def append_directors(self, directors: str):
        self.__directors = self.__directors + directors.split(", ")

    def append_languages(self, languages: str):
        self.languages = self.__languages + languages.split(", ")
