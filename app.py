from flask import Flask, render_template

app = Flask(__name__)

# POSTS MOCK
posts = [
     {
         "titulo": "Post1",
         "texto": "Meu primeiro Post"
     },
     {
          "titulo": "Post2",
         "texto": "olha eu aqui de novo"    
     }
]

@app.route("/")
def exibir_entradas():
       return render_template("exibir_entradas.html", entradas=posts)

@app.route("/pudim")
def pudim():
     return "<h1>eu gosto de pudim</h1>"
