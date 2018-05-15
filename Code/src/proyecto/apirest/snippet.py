from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="claraTFG2",
    password="123456clara",
    hostname="claraTFG2.mysql.pythonanywhere-services.com",
    databasename="claraTFG2$prueba",
)
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    ids = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), unique=True)

    def __init__(self, username, email,password,ids=None ):
        self.username = username
        self.email = email
        self.password = password
        self.ids = ids

    def jsonUser(self):
        return self.username + self.email +self.password


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('ids','username', 'email','password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    
    
    try:
        new_user = User(username, email,password)
        db.session.add(new_user)
        db.session.commit()
        return "True"
    except:
        return "False"

# endpoint to show all users
@app.route("/prueba", methods=["GET"])
def get_prueba():
    
    return jsonify("helloworld")
    
# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)

# endpoint to delete all users
@app.route("/user/deleteall", methods=["DELETE"])
def Deleteall_user():
    users = User.query.all()
    number=0
    for i in users:        
        db.session.delete(i)
        db.session.commit()
        number+=1

   
    return jsonify(number)


# endpoint to get user detail by id
@app.route("/user/<ids>", methods=["GET"])
def user_detail(ids):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<ids>", methods=["PUT"])
def user_update(ids):
    user = User.query.get(id)
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    user.email = email
    user.username = username
    user.password = password

    db.session.commit()
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/user/<ids>", methods=["DELETE"])
def user_delete(ids):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)