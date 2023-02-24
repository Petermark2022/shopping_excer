from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLA1chemy
from os import environ

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URL")
db = SQLA1chemy(app)

class User(db.mode):
    __tableame__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    userame = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    
    def json(self):
        return {"id" : id, "username" : self.username, "email" : self.email}
    
db.create_all()

#create a test route
@app.route("/test", methods=["GET"])
def test():
    return make_response(jsonify({"message": "tesr route"}, 200))

#create a user
@app.toute("/users", methods=["POSt"])
def create_user():
    try:
         data = request.get_json()
         new_user = User(username=data["username"], email=data["email"])
         db.session.add(new_user)
         db.session.commit()
         return make_response(jsonify({"message" : "user created"}), 201)
    except e:
        return make_response(jsonify({"message": "error creating user"}), 500)
    
#get all users
@app.route("/user", methods =["GET"])
def get_user():
    try:
        users = User.query.all()
        return make_response(jsonify({"users": [user.json() for user in users]}), 200)
    except e:
        return make_response(jsonify({"message": "error getting users"}), 500)
    
#get a user by id
@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
             return make_response(jsonify({"user": user.json()}), 500)
    except e:
        return make_response(jsonify({"message": "error getting user"}), 500)

#update a user
@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    try:
        data = request.get_json()
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.username = data["useername"]
            user.email = data["email"]
            db.session.commit()
            return make_response(jsonify({"message": "user updated"}), 200)
        return make_response(jsonify({"message": "user not found"}), 404)
    except e:
        return make_response(jsonify({"message": "error updating user"}), 500)
    
#delete a user
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({"mesage": "user deleted"}), 200)
        return make_response(jsonify({"message": "user not found"}), 404)
    except e:
        return make_response(jsonify({"message": "error deleting user"}), 500)