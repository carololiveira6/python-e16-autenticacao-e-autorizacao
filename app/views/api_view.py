from flask import Blueprint, current_app, jsonify, request

from app.models.user_model import UserModel

from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from http import HTTPStatus

import ipdb


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route('/login', methods=["POST"])
def login():

    data = request.get_json()

    user = UserModel.query.filter_by(email=data['email']).first()

    if not user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND
    
    if user.verify_password(data['password']):
        access_token = create_access_token(identity=user)
        return {"message": access_token}, HTTPStatus.OK
    else:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED


@bp.route("/", methods=["GET"])
@jwt_required()
def return_user():
    
    user = get_jwt_identity()

    return jsonify(user)


@bp.route("/signup", methods=["POST"])
def post_user():
    
    session = current_app.db.session

    data = request.get_json()

    password_to_hash = data.pop("password")

    user = UserModel(**data)

    user.password = password_to_hash

    session.add(user)
    session.commit()

    return jsonify(user), HTTPStatus.CREATED


@bp.route("/", methods=["PUT"])
@jwt_required()
def update_user():

    required_keys = ["name", "last_name", "email"]

    current_user = get_jwt_identity()

    session = current_app.db.session

    data = request.get_json()

    user: UserModel = UserModel.query.get(current_user["id"])

    for key, value in data.items():
        if key in required_keys:
            setattr(user, key, value)
        else:
            return {
                "required_key": required_keys,
                "recived_keys": data.keys(),
            }

    session.add(user)
    session.commit()

    return jsonify(user), HTTPStatus.OK


@bp.route("/", methods=["DELETE"])
@jwt_required()
def delete():

    session = current_app.db.session
    
    current_user = get_jwt_identity()

    user: UserModel = UserModel.query.get(current_user["id"])

    session.delete(user)
    session.commit()

    return " ", HTTPStatus.NO_CONTENT