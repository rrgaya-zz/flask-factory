from flask import Blueprint, render_template, request, abort, current_app

bp = Blueprint("contact", __name__, url_prefix="/contact")


@bp.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    
    # Processar Data
    name = request.form.get("name")
    message = request.form.get("message")
    
    # Validar
    if not name or not message:
        abort(400, "Mensagem invalida")
    
    # Banco de dados
    current_app.db.message.insert_one({"name": name, "message": message})

    print(request.form)
    return "Enviado!"

def configure(app):
    app.register_blueprint(bp)