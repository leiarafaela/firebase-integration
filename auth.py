
import pyrebase
import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()


def SendResetPassword(email):


    config = {
    'apiKey': os.getenv('APIKEY'),
    'authDomain': os.getenv('AUTHDOMAIN'),
    'projectId': os.getenv('PROJECTID'),
    'storageBucket': os.getenv('STORAGEBUCKET'),
    'messagingSenderId': os.getenv('MESSAGINGSENDERID'),
    'appId': os.getenv('APPID'),
    'measurementId': os.getenv('MEASUREMENTID'),
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
    'apiKey': os.getenv('APIKEY'),
    'authDomain': os.getenv('AUTHDOMAIN'),
    'projectId': os.getenv('PROJECTID'),
    'storageBucket': os.getenv('STORAGEBUCKET'),
    'messagingSenderId': os.getenv('MESSAGINGSENDERID'),
    'appId': os.getenv('APPID'),
    'measurementId': os.getenv('MEASUREMENTID'),
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
    'apiKey': os.getenv('APIKEY'),
    'authDomain': os.getenv('AUTHDOMAIN'),
    'projectId': os.getenv('PROJECTID'),
    'storageBucket': os.getenv('STORAGEBUCKET'),
    'messagingSenderId': os.getenv('MESSAGINGSENDERID'),
    'appId': os.getenv('APPID'),
    'measurementId': os.getenv('MEASUREMENTID'),
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









