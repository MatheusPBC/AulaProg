from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import os 
from modelo import Time
 
app = Flask(__name__) 
caminho = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(caminho, "times.db") 
app.config["SQLpALCHEMY_DATABASE_URI"] = "sqlite:///"+arquivobd 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  
db = SQLAlchemy(app)


@app.route("/")
def padrao():
    return "Bem vindo ao backend"


@app.route("/listar_times")
def listar_times():
    db.session.query(Time).all()
    return times

app.run(debug=True)
