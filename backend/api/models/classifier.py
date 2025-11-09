import tensorflow as tf
from PIL import Image
import numpy as np
import os

# Model representation of ML Model
class Classifier:

    def __init__(self, class_names):
        self.model = self.load_model()
        self.class_names = class_names

    def load_model(self):
        # Loading the ML Model from .keras file so it can be used to make predictions
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, "plant-disease-identifier.keras")

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at: {model_path}")

        model = tf.keras.models.load_model(model_path)
        return model
    
    def preproccess_image(self, image_path):
        # Load Image
        image = Image.open(image_path).convert("RGB")

        # Convert image into an array
        image_array = tf.keras.preprocessing.image.img_to_array(image)
        image_array = tf.expand_dims(image_array, 0)

        return image_array
    
    def Predict(self, image_path):
        # Convert image path to an image array to be inputted into the model
        image_array = self.preproccess_image(image_path)

        # Model makes its prediction on image
        model_predictions = self.model.predict(image_array)


        # Extracted predicted class from model
        predicted_class = self.class_names[np.argmax(model_predictions[0])]

        return predicted_class