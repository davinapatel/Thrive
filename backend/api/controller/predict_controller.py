from flask import request, jsonify
from api.models.classifier import Classifier
from api.models.config import CLASS_NAMES
from flask.views import MethodView
import os

class PredictionHandler(MethodView):

    def __init__(self, SessionLocal):
        self.session = SessionLocal

    def post(self):
        # Check the API Request includes an image file
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        # Get image from request
        file = request.files['file']

        # Save image file temporarily
        file_path = "api/images/temp_image.jpg"
        file.save(file_path)

        # Create instance of Classifier Model
        model = Classifier(CLASS_NAMES)

        # Make prediction from uploaded image
        prediction = model.Predict(file_path)

        # Need to save prediction to UserPrediction table
        

        # Return the prediction as a JSON Response

        if os.path.exists(file_path):
            os.remove(file_path)

        return jsonify({'prediction': prediction})