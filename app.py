from flask import Flask, session, render_template, request, redirect
from auth import SendResetPassword

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        try:
            resetPass = SendResetPassword(email)
        except:
            return 'Erro ao redefinir'
    return render_template('reset-password.html')


@app.route('/logout')
def logout():
    pass


if __name__ == '__main__':
    app.run(port=8000, debug=True)
