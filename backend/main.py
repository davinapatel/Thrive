from flask import Flask
from flask_cors import CORS
from api.routes.routes import register_routes
from database import Base, engine, SessionLocal
from api.models.plant_disease import PlantDisease
from api.models.user import User

def init_app():
    app = Flask(__name__, static_folder='api/static')
    CORS(app)
    return app

app = init_app()

# Creates all tables in database - sqlite db
Base.metadata.create_all(bind=engine)

# Registers api endpoints and passes SessionLocal for routes that require calls to DB
register_routes(app, SessionLocal)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)
