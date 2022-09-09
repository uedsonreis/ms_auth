from model.entities.user import User


class __UserRepository:

    __users = [
        User(1, 'Uedson Reis', 'uedsonreis', '123456'),
        User(2, 'Guilherme Silva', 'guilherme', '123456'),
        User(3, 'Heitor Andrade', 'andrade', '123456'),
    ]

    __users[0].admin = True

    def find(self):
        return self.__users

    def get(self, id: int):
        if len(self.__users) >= id:
            user = self.__users[id - 1]
            return user
        return None

    def save(self, user: User):
        if user.id is None:
            saved = User(len(self.__users) + 1, user.name, user.username, user.password)
            self.__users.insert(saved.id, saved)
            return saved
        else:
            user_db = self.get(user.id)

            if user_db is None:
                return None
            else:
                if user.name is not None:
                    user_db.name = user.name
                if user.username is not None:
                    user_db.username = user.username
                if user.password is not None:
                    user_db.password = user.password
                if user.admin is not None:
                    user_db.admin = user.admin
            return user_db

    def delete(self, id: int):
        if self.get(id) is None:
            return False
        else:
            self.__users.pop(id-1)
            return True


userRepository = __UserRepository()
