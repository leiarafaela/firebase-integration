
import pyrebase
import requests





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
        user = auth.create_user_with_email_and_password(email, senha)
        return user
    except requests.exceptions.HTTPError as e:
        error_json = e.response
        error_message = error_json['error']['message']
        if error_message == "EMAIL_EXISTS":
            print("O e-mail informado já está em uso.")
        else:
            print("Ocorreu um erro ao criar o usuário:", error_message)
    except Exception as e:
        print("Ocorreu um erro ao criar o usuário:", e)


    return user



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
        error_json = e.response.json()
        error_message = error_json["error"]["message"]
    except Exception as e:
        print("Ocorreu um erro ao criar o usuário:", error_message)


    return user






