from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base
from datetime import datetime

class UserPrediction(Base):

    __tablename__ = "user_prediction"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    disease_id = Column(Integer, ForeignKey("plant_disease.id"), nullable=False)
    image = Column(String(255), nullable=False)
    prediction = Column(String(255), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)