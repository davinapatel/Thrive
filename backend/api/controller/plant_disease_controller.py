from api.models.plant_disease import PlantDisease
from flask import request, jsonify
from flask.views import MethodView

# def get_diseases(SessionLocal):
#     def view_func():
#         session = SessionLocal()
#         plant_diseases = session.execute(PlantDisease).all()

#         response = []

#         for disease in plant_diseases:
#             disease_dict = {
#                 "id": disease.id,
#                 "name": disease.name,
#                 "type": disease.type,
#                 "treatment": disease.treatment
#             }

#             response.append(disease_dict)

#         return jsonify(response), 200
    
#     return view_func


# def create_disease(SessionLocal):
#     def view_func():
#         session = SessionLocal()
#         data = request.get_json()
    
#         record = PlantDisease(
#             name = data.get("name"),
#             type = data.get("type"),
#             description = data.get("description"),
#             treatment = data.get("treatment")
#         )

#         session.add(record)
#         session.commit()
#         session.close()

#         return {"message":"Disease created"}, 201
#     return view_func

class DiseaseHandler(MethodView):

    def __init__(self, SessionLocal):
        self.SessionLocal = SessionLocal

    def get(self, name=None):
        session = self.SessionLocal()

        if name != None:
            record = session.query(PlantDisease).filter(PlantDisease.name == name).first()
            try:
                if record:
                    return jsonify({
                    "id": record.id,
                    "name": record.name,
                    "type": record.type,
                    "description": record.description,
                    "treatment": record.treatment

                    }) , 200
                else:
                    return jsonify({"Error": "Record not found"}), 404
            finally:
                session.close()
        else:

            plant_diseases = session.query(PlantDisease).all()

            if len(plant_diseases) == 0:
                response = "No records found"
            else:
                response = []

                for disease in plant_diseases:
                    disease_dict = {
                        "id": disease.id,
                        "name": disease.name,
                        "type": disease.type,
                        "treatment": disease.treatment
                    }
                    response.append(disease_dict)
            session.close()
            return jsonify(response), 200
    
    def post(self):
        try:
            session = self.SessionLocal()

            data = request.get_json()
        
            record = PlantDisease(
                name = data.get("name"),
                type = data.get("type"),
                description = data.get("description"),
                treatment = data.get("treatment")
            )

            session.add(record)
            session.commit()
            return {"message":"Disease created", "id": record.id}, 201
        finally:
            session.close()

        
