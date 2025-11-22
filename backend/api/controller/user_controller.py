from api.models.user import User
from flask import request, jsonify
from flask.views import MethodView

class UserHandler(MethodView):

    def __init__(self, SessionLocal):
        self.SessionLocal = SessionLocal

    def post(self):
        session = self.SessionLocal()
        try:

            data = request.get_json()

            record = User(
                username = data.get("username"),
                password = data.get("password")
            )
            session.add(record)
            session.commit()

            return {"message":"User successfully created", "id":record.id}, 201
        
        finally:
            session.close()

        
    
    def get(self):
        session = self.SessionLocal()
        try:
            users = session.query(User).all()

            if len(users) == 0:
                response = "No users found"
            else:
                response = []
                for user in users:
                    user_dict = {
                        "id": user.id,
                        "username": user.username
                    }

                    response.append(user_dict)
            return jsonify(response), 200
        finally:
            session.close()
        