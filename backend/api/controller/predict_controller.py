from flask import request, jsonify
from api.models.classifier import Classifier
from api.models.config import CLASS_NAMES

def predict_disease():
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    # Get image from request
    
    file = request.files['file']

    # Save the file temp
    file_path = "temp_image.jpg"
    file.save(file_path)

    # Create instance of Classifier Model
    model = Classifier(CLASS_NAMES)

    # Make prediction from uploaded image
    prediction = model.Predict(file_path)

    # Return the prediction as a JSON Response
    return jsonify({'prediction': prediction})