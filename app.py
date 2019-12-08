import views
import contact
import db
import admin
from flask import Flask


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="frontend")

    # Extensions
    db.configure(app)
    views.configure(app)

    admin.configure(app)

    # Blueprint app example
    contact.configure(app)

    # Configurar variaveis
    app.config["SECRET_KEY"] = "skdalksdjsalkjdlkajsdlkajlks"

    return app
 

