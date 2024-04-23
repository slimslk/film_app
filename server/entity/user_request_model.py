class UserQuery:
    def __init__(self, req_id, user_request, date):
        self.__req_id = req_id
        self.__user_request = user_request
        self.__date = date

    def __hash__(self):
        return hash((self.__req_id, self.__user_request, self.__date))

    def __eq__(self, other):
        if (other is None or
                self.__req_id != other.req_id or
                self.__user_request != other.user_request or
                self.__date != other.date):
            return False
        else:
            return True

    def __str__(self):
        ...

    @property
    def req_id(self):
        return self.req_id

    @property
    def user_request(self):
        return self.__user_request

    @property
    def date(self):
        return self.__date

    @req_id.setter
    def req_id(self, req_id):
        self.__req_id = req_id

    @user_request.setter
    def user_request(self, user_request):
        self.__user_request = user_request

    @date.setter
    def date(self, date):
        self.__date = date
