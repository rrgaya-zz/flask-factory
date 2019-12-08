from flask import jsonify, render_template


def configure(app):

    @app.route("/")
    def index():
        nomes = ["Ricardo", "Maria", "José"]
        return render_template("index.html", title="Apresentação para Nação", nomes=nomes)
        
    @app.route("/api")
    def api():
        return jsonify({"nome": "Ricardo"})
