from flask import Blueprint, request, jsonify
from api.v1.dependencies import get_db
from schemas.auth import UserCreate, UserLogin
from services.auth import create_user, authenticate_user

user_router = Blueprint("users", __name__)

@user_router.route("/register", methods=["POST"])
def register_user():
    db = next(get_db())
    user_data = request.json
    user = UserCreate(**user_data)
    response = create_user(db=db, user=user)
    return jsonify(response)

@user_router.route("/login", methods=["POST"])
def login_user():
    db = next(get_db())
    user_data = request.json
    user = UserLogin(**user_data)
    response = authenticate_user(db=db, user=user)
    return jsonify(response)
