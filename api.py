from flask import Flask, request, make_response
from flask_cors import CORS
from model import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///foo.db')
Base.metadata.create_all(engine)

app = Flask(__name__)
CORS(app)

@app.route('/register', methods = ['POST'])
def register():
    """
    {
        "name": "asdf",
        "password": "sdafafds"
    }
    """
    username = request.get_json()["username"]
    raw_password = request.get_json()["password"]
    new_user = User(username, raw_password)

    with Session(engine) as session:
        try: 
            session.add(new_user)
            session.commit()
            return make_response({"status":"new user created"},200)
        except IntegrityError as e:
            session.rollback()
            return make_response({"error": "Username is already taken"}, 403)

        
@app.route('/login', methods = ['POST'])
def login():
    """
    {
        "username": "asfd",
        "password": "asdf"
    }
    """
    username = request.get_json()['username']
    password = request.get_json()['password']
    





if __name__ == "__main__":
    app.run(host='0.0.0.0')

