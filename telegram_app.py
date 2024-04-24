from client.console_app.console_search_film import ConsoleSearchFilmApp
from client.telegram_bot_app.tel_bot_app import TelegramSearchFilm
from server.search_film_app import SearchFilmApp


def main():
    server = SearchFilmApp()
    public_api = server.public_api
    TelegramSearchFilm(public_api).start_app()


if __name__ == "__main__":
    main()
