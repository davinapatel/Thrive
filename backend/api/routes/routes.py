# Registers all api endpoints in Thrive POC
# The routes include their dedicated handler function/ controller

# def register_routes(app, SessionLocal):
    
#     from api.controller.root_controller import welcome, health_check
#     from api.controller.predict_controller import predict_disease
#     from api.controller.plant_disease_controller import create_disease, get_diseases

#     routes = [
#         ("/", welcome, ["GET"]),
#         ("/health", health_check, ["GET"]),
#         ("/predict", predict_disease, ["POST"]),
#         ("/disease", create_disease(SessionLocal), ["POST"]),
#         ("/disease", get_diseases(SessionLocal), ["GET"])
#     ]
#     for endpoint, view_func, methods in routes:
#         app.add_url_rule(endpoint, view_func.__name__, view_func, methods = methods)

from api.controller.root_controller import welcome, health_check
from api.controller.predict_controller import PredictionHandler
from api.controller.plant_disease_controller import DiseaseHandler
from api.controller.user_controller import UserHandler
from api.controller.user_prediction_controller import UserPredictionHandler

def register_routes(app, SessionLocal):
    
    app.add_url_rule("/", "welcome", welcome, methods=["GET"])
    app.add_url_rule("/health", "health_check", health_check, methods=["GET"])

    prediction_handler = PredictionHandler.as_view("prediction_handler", SessionLocal=SessionLocal)
    app.add_url_rule("/predict", view_func=prediction_handler, methods=["POST"])

    disease_handler = DiseaseHandler.as_view("disease_handler", SessionLocal=SessionLocal)
    app.add_url_rule("/disease", view_func=disease_handler, methods=["GET","POST"])
    app.add_url_rule("/disease/<string:name>", view_func=disease_handler, methods=["GET"])

    user_handler = UserHandler.as_view("user_handler", SessionLocal=SessionLocal)
    app.add_url_rule("/user", view_func=user_handler, methods=["GET","POST"])

    user_prediction_handler = UserPredictionHandler.as_view("user_prediction_handler", SessionLocal=SessionLocal)
    app.add_url_rule("/userpredictions", view_func=user_prediction_handler, methods=["POST"])
    app.add_url_rule("/userpredictions/<int:user_id>", view_func=user_prediction_handler, methods=["GET"])