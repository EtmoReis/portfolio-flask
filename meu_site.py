from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/projetos")
def projetos():
    lista_projetos = [
        {
            "nome": "Sistema com Flask",
            "descricao": "Aplicação web com rotas dinâmicas, templates e estrutura MVC.",
            "tecnologias": "Python, Flask, HTML, CSS",
            "link": "https://github.com/EtmoReis/Sistema-Flask"
        },
        {
            "nome": "API em Python",
            "descricao": "API REST para manipulação de dados com endpoints dinâmicos.",
            "tecnologias": "Python, Flask",
            "link": "https://github.com/EtmoReis/API-Python"
        }
    ]
    return render_template("projetos.html", projetos=lista_projetos)

# Configuração para Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)