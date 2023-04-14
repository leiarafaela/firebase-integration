from flask import Flask, session, render_template, request, redirect, make_response
from auth import SendResetPassword, CreateUserFirebase, SignFirebase, EmailExiste, SenhaErrada

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


@app.route('/', methods=['POST','GET'])
def create():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if senha == "":
            return "Senha invalida"
        if email == "":
            return "Email invalido"
        
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
    
    return render_template('cadastro.html')


@app.route('/login', methods=['POST','GET'])
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
