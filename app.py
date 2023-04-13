from flask import Flask, session, render_template, request, redirect, make_response
from auth import SendResetPassword, CreateUserFirebase, SignFirebase

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
        
        user = CreateUserFirebase(email, senha)
        print(f"User ===> {user}")
        if user['idToken'] != "":
            return make_response(redirect('/login'))

               
    
    return render_template('cadastro.html')


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if senha == "":
            return "Senha invalida"
        if email == "":
            return "Email invalido"
        try:
            user = SignFirebase(email, senha)
        except:
            return make_response(redirect(login), error=user['error']['message'])
    return render_template("login.html")

if __name__ == '__main__':
    app.run(port=8000, debug=True)
