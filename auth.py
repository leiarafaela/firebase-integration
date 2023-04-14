
import pyrebase
import requests
import json




def SendResetPassword(email):

    config = {
    'apiKey': "AIzaSyDMAChNn_jeQKdiqwPQWOLNPiB3GX_PAtM",
    'authDomain': "ibooks-1fa58.firebaseapp.com",
    'projectId': "ibooks-1fa58",
    'storageBucket': "ibooks-1fa58.appspot.com",
    'messagingSenderId': "516281803999",
    'appId': "1:516281803999:web:31b0d833009469f4c1b56a",
    'measurementId': "G-V8JNJ11FDL",
    'databaseURL': ""
    }

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    user = auth.send_password_reset_email(email)
    return user

class EmailExiste(Exception):
    pass
class SenhaErrada(Exception):
    pass

def CreateUserFirebase(email, senha):

    config = {
    'apiKey': "AIzaSyDMAChNn_jeQKdiqwPQWOLNPiB3GX_PAtM",
    'authDomain': "ibooks-1fa58.firebaseapp.com",
    'projectId': "ibooks-1fa58",
    'storageBucket': "ibooks-1fa58.appspot.com",
    'messagingSenderId': "516281803999",
    'appId': "1:516281803999:web:31b0d833009469f4c1b56a",
    'measurementId': "G-V8JNJ11FDL",
    'databaseURL': ""
    }

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    try:
        return auth.create_user_with_email_and_password(email, senha)
    except requests.exceptions.HTTPError as e:
        print(e.__class__.__name__)
        if "EMAIL_EXISTS" in str(e):
            raise EmailExiste()
        else:
            raise e
    except Exception as e:
        print("Ocorreu um erro ao criar o usuário:", e)
        raise e



def SignFirebase(email,senha):

    config = {
    'apiKey': "AIzaSyDMAChNn_jeQKdiqwPQWOLNPiB3GX_PAtM",
    'authDomain': "ibooks-1fa58.firebaseapp.com",
    'projectId': "ibooks-1fa58",
    'storageBucket': "ibooks-1fa58.appspot.com",
    'messagingSenderId': "516281803999",
    'appId': "1:516281803999:web:31b0d833009469f4c1b56a",
    'measurementId': "G-V8JNJ11FDL",
    'databaseURL': ""
    }

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    try:
        user = auth.sign_in_with_email_and_password(email, senha)
    except requests.exceptions.HTTPError as e:
        print(e.__class__.__name__)
        if "INVALID_PASSWORD" in str(e) or "EMAIL_NOT_FOUND" in str(e):
            raise SenhaErrada()
        else:
            raise e
    except Exception as e:
        print("Ocorreu um erro ao logar o usuário:", e)
        raise e









