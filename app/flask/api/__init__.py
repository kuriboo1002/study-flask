from flask import Flask
from flask_cors import CORS
from api.database import db
from .views.user import user


def create_app():

    app = Flask(__name__)
    CORS(app)
    app.config["JSON_AS_ASCII"] = False

    # DB設定を読み込む
    app.config.from_object('config.Config')
    db.init_app(app)

    app.register_blueprint(user)

    return app


app = create_app()
