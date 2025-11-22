from sqlalchemy import Column, Integer, String
from database import Base

# Created Plant Disease model used to create the Plant Disease table in DB
# Table holds information about all the Plant Diseases that can be identified

class PlantDisease(Base):

    __tablename__ = "plant_disease"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False, unique=True)
    type = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    treatment = Column(String(200))

    # Create a representation string
    def __repr__(self):
        return '<Name %r>' % self.name