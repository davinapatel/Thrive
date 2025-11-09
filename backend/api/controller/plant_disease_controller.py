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
        self.session = SessionLocal

    def get(self):
        session = self.session()  
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
        session = self.session()

        data = request.get_json()
    
        record = PlantDisease(
            name = data.get("name"),
            type = data.get("type"),
            description = data.get("description"),
            treatment = data.get("treatment")
        )

        session.add(record)
        session.commit()
        session.close()

        return {"message":"Disease created", "id": record.id}, 201
