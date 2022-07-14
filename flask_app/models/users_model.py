from flask_app.config.mysqlconnect import connectToMySQL


class User:
    def __init__(self,data):
        self.id = data["id"]
        self.f_name = data["f_name"]
        self.l_name = data["l_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]


    @classmethod
    def get_all(cls):
        query = "select* from users;"
        result = connectToMySQL("user_db").query_db(query)
        # print(result)
        list_users =[]
        for user in result:
            list_users.append(cls(user))
        print(list_users)
        return list_users


    @classmethod
    def create_user(cls,data):
        query = "insert into users (f_name,l_name,email) values (%(f_name)s,%(l_name)s,%(email)s);"
        result = connectToMySQL("user_db").query_db(query,data)
        print(result)
        return result