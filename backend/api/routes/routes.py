from api.controller.root_controller import welcome, health_check
from api.controller.predict_controller import predict_disease

routes = [
    ("/", welcome, ["GET"]),
    ("/health", health_check, ["GET"]),
    ("/predict", predict_disease, ["POST"])
]
def register_routes(app):
    for endpoint, view_func, methods in routes:
        app.add_url_rule(endpoint, view_func.__name__, view_func, methods = methods)