from flask import Blueprint
from flask_httpauth import HTTPDigestAuth

from app.models import UserModel
from http import HTTPStatus


bp = Blueprint("bp_admin", __name__, url_prefix="/admin")
auth = HTTPDigestAuth()


@auth.get_password
def verify_password(email) -> None:

    user: UserModel = UserModel.query.filter_by(email=email).first()

    return user.password


@bp.get("/")
@auth.login_required()
def get_user_token():

    email = auth.get_auth()["username"]

    user: UserModel = UserModel.query.filter_by(email=email).first() 

    user_token = user.api_key

    return {"token": user_token}, HTTPStatus.OK