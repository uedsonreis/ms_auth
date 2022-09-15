from api.controller.role_controller import *
from api.controller.user_controller import *
from api.controller.user_role_controller import UserRoleController
from api.controller.auth_controller import *
from settings import db


# db.drop_all()
db.create_all()


if __name__ == "__main__":
    app.run(port=5000)
