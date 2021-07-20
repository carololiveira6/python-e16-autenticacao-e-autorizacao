from flask import Blueprint
from flask_httpauth import HTTPBasicAuth

from app.models import UserModel
from http import HTTPStatus


bp = Blueprint("bp_admin", __name__, url_prefix="/admin")
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email, password) -> None:

    user: UserModel = UserModel.query.filter_by(email=email).first()

    if user and user.verify_password(password):
        return user

    return None


@bp.get("/")
@auth.login_required()
def get_user_token():

    user_token = auth.current_user().api_key

    return {"token": user_token}, HTTPStatus.OK