import bcrypt
import utils.db_funcs as fns
import jwt
import json
from base64 import b64decode as decode

secret = "some secret text"


def hash_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def verify_password(stored_pass, user_pass):
    return bcrypt.checkpw(user_pass.encode('utf-8'), stored_pass.encode('utf-8'))


def create_new_user(password, username, role):
    hashed_password = hash_password(password)
    current_db = fns.load_db()
    current_db[username] = {
        "username": username,
        "password": hashed_password,
        "role": role
    }
    return current_db


def generate_jwt(payload):
    SECRET_KEY = "your-secret-key"
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    print('encoded_jwt: ', encoded_jwt)
    return encoded_jwt


def verify_jwt(user_jwt):
    try:
        SECRET_KEY = "your-secret-key"
        data = jwt.decode(user_jwt, SECRET_KEY, algorithms="HS256")
        return data["user role"]
    except Exception as e:
        print('e: ', e)
        print("bad token")
        return False


def check_token(request):
    auth_header = request.headers.get('authorization')
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        try:
            if verify_jwt(token):
                return request
        except Exception as e:
            raise e
    return


def check_admin(request):
    role = request.headers.get('role')
    if role == 'admin':
        return True
    return False
