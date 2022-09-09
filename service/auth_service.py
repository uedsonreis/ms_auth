from service.user_service import userService


class __AuthService:

    def get_user_service(self):
        return userService

    def login(self, username: str, password: str):
        user = self.get_user_service().get_by_username(username)
        if user.password == password:
            return "ABC123"
        else:
            return None


authService = __AuthService()
