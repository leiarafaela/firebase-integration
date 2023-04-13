
import pyrebase






def SendResetPassword(email):

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    user = auth.send_password_reset_email(email)
    return user





#print(user)