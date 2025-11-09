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
from api.controller.predict_controller import predict_disease
from api.controller.plant_disease_controller import DiseaseHandler

def register_routes(app, SessionLocal):
    
    app.add_url_rule("/", "welcome", welcome, methods=["GET"])
    app.add_url_rule("/health", "health_check", health_check, methods=["GET"])
    app.add_url_rule("/predict", "predict_disease", predict_disease, methods=["POST"])

    disease_handler = DiseaseHandler.as_view("disease_handler", SessionLocal=SessionLocal)
    app.add_url_rule("/disease", view_func=disease_handler, methods=["GET","POST"])