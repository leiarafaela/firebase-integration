from flask import Flask, session, render_template, request, redirect, make_response
from auth import SendResetPassword, CreateUserFirebase, SignFirebase, EmailExiste, SenhaErrada
import requests
from dotenv import load_dotenv
import os
from db.database import Produto

load_dotenv()

app = Flask(__name__)

@app.route('/reset', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        try:
            resetPass = SendResetPassword(email)
        except:
            return 'Erro ao redefinir'
    return render_template('reset-password.html')


@app.route('/home', methods=['GET'])
def show_index():
    produtos = Produto.getAll()
    return render_template('home.html', produtos=produtos)

@app.route('/home', methods=['POST'])
def post_index():
    
    return render_template('home.html')


@app.route('/detalhes', methods=['GET'])
def detalhes_produto():
    return render_template('detalhe-produto.html')

@app.route('/cadastro', methods=['GET'])
def get_casdastro():
    errors = {}
    return render_template('cadastro.html', errors=errors)


@app.route('/cadastro', methods=['POST'])
def create_user_login():
    errors = {}
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        recaptcha_response = request.form['g-recaptcha-response']

        if senha == "":
            return "Senha invalida"
        if email == "":
            return "Email invalido"
        

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': os.getenv('SECRETRECAPTCHA'),
                'response': recaptcha_response
            }
        ).json()

        if not recaptcha_request.get('success'):
            errors['recaptcha'] = True


        if errors:
            return render_template('cadastro.html', errors=errors)




        try:
            user = CreateUserFirebase(email, senha)
            print(f"User ===> {user}")
            if user['idToken'] != "":
                return make_response(redirect('/login'))
            return "Problema com token", 400
        except EmailExiste as e:
            return "Já tem o e-mail.", 400
        except Exception as e:
            return str(e), 400
        

  
    return render_template('home.html', errors=errors)


@app.route('/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if senha == "":
            return "Senha invalida", 400
        if email == "":
            return "Email invalido", 400
        try:
            user = SignFirebase(email, senha)
            return render_template('home.html')
        except SenhaErrada as e:
            return "Senha ou Email errados", 400
        except Exception as e:
            return str(e), 400
        
    return render_template("login.html")

if __name__ == '__main__':
    app.run(port=8000, debug=True)
