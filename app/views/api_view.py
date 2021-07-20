from flask import Blueprint, current_app, jsonify, request

from app.models.user_model import UserModel

from flask_httpauth import HTTPTokenAuth

import secrets

from http import HTTPStatus


bp = Blueprint("api", __name__, url_prefix="/api")

auth = HTTPTokenAuth(scheme="bearer")

@auth.verify_token
def verify_token(token):

    user_token = UserModel.query.filter_by(api_key=token).first()

    return user_token


@bp.route("/", methods=["GET"])
@auth.login_required()
def return_user():
    
    user = auth.current_user()

    return jsonify(user)


@bp.route("/signup", methods=["POST"])
def post_user():
    
    session = current_app.db.session

    data = request.get_json()

    # password_to_hash = data.pop("password")

    user = UserModel(**data)

    user.api_key = secrets.token_hex(32)

    # user.password = password_to_hash

    session.add(user)
    session.commit()

    return jsonify(user), HTTPStatus.CREATED


@bp.route("/", methods=["PUT"])
@auth.login_required()
def update_user():

    session = current_app.db.session

    data = request.get_json()

    user = auth.current_user()

    for key, value in data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()

    return jsonify(user), HTTPStatus.OK


@bp.route("/", methods=["DELETE"])
@auth.login_required()
def delete_user():
    
    session = current_app.db.session

    user = auth.current_user()

    session.delete(user)
    session.commit()

    return " ", HTTPStatus.NO_CONTENT
    