from flask import Flask
from flask_cors import CORS
from api.routes.routes import register_routes

def init_app():
    app = Flask(__name__)
    CORS(app)
    return app

app = init_app()
register_routes(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)
