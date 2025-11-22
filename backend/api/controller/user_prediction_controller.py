from api.models.user_prediction import UserPrediction
from flask import request, jsonify
from flask.views import MethodView
from database import DB_IMAGE_UPLOAD_PATH
from werkzeug.utils import secure_filename
import os

class UserPredictionHandler(MethodView):

    def __init__(self, SessionLocal):
        self.SessionLocal = SessionLocal

    def post(self):
        session = self.SessionLocal()

        try:

            data = request.form

            file = request.files.get("image")
            filename = secure_filename(file.filename)
            imagePath = os.path.join(DB_IMAGE_UPLOAD_PATH, filename)
            file.save(imagePath)

            record = UserPrediction(
                user_id = data.get("user_id"),
                disease_id = data.get("disease_id"),
                image = imagePath,
                prediction = data.get("prediction")
            )

            session.add(record)
            session.commit()

            return {"message": "User Prediction Record added", "id": record.id}, 201
        finally:
            session.close()
    
    def get(self, user_id):
        # Retrieves all records for a particular user_id
        session = self.SessionLocal()

        try:

            records = session.query(UserPrediction).filter(UserPrediction.user_id == user_id).all()

            if len(records) == 0:
                return jsonify({"Records": "No records found"}),200

            response = []
            for r in records:
                row = {
                    "id": r.id,
                    "user_id": r.user_id,
                    "disease_id": r.disease_id,
                    "image": r.image,
                    "prediction": r.prediction,
                    "date": r.date
                }
                response.append(row)

            return jsonify({"Records": response}), 200
        finally:
            session.close()
       

