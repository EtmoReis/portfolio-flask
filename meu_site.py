from flask import Flask, render_template


app = Flask(__name__)


#criar a 1@ Pagina do site 
#route -- etmo.com/route 
#funcao -- oque eu quero exibir  naquela pagina 
#tamplate

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
if __name__ == "__main__":
    app.run(debug=True)

    #servidor do heroku -deploy