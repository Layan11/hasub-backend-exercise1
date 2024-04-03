from fastapi import APIRouter
from models.auth_model import auth_model
import utils.auth_funcs as auth_fns
import utils.db_funcs as db_fns

router = APIRouter()


@router.post('/auth/sign_up')
def sign_up(body: auth_model):
    updated_db = auth_fns.create_new_user(body.password, body.username, body.role)
    db_fns.update_db(updated_db)
    auth_token = auth_fns.generate_jwt({"user role": "guest"})
    return {"msg": "user created", "token": auth_token}


@router.post('/auth/sign_in')
def sign_in(body: auth_model):
    try:
        stored_user = db_fns.find_user(body.username)
        if stored_user:
            stored_pass = stored_user["password"]
            if auth_fns.verify_password(stored_pass, body.password):
                auth_token = auth_fns.generate_jwt({"user role": body.role})
                return {"msg": "user sign in successfully", "token": auth_token}
            else:
                return {"msg": "invalid credentials"}
    except Exception as e:
        print(e)
        return {"msg": "no such username"}
