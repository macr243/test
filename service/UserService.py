import json


class UserService:

    @staticmethod
    def save_user(user):
        print(user)
        return json.dumps({"success": True}), 201

    @staticmethod
    def get_user(id):
        return json.dumps({"id": id, "name": "Miguel", "email":"macr243@gmail.com"})

    @staticmethod
    def update_user(id):
        return json.dumps({"id": id, "name": "Miguel", "email":"macr243@gmail.com"})

    @staticmethod
    def delete_user(id):
        return json.dumps(''), 204