from api.controller.user_controller import *
from api.controller.auth_controller import *
from settings import db

# db.drop_all()
db.create_all()

app.run(port=5000)