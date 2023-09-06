from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

router = APIRouter()

cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

class Item(BaseModel):
    temperature: int

@router.get("/")
def get_temperatures():
    users_ref = db.collection("temperatures")
    docs = users_ref.stream()

    temperatures_list = []

    for doc in docs:
        temperature_data = doc.to_dict()
        temperatures_list.append({doc.id: temperature_data})
    
    json_compatible_item_data = jsonable_encoder(temperatures_list)
    
    return JSONResponse(content=json_compatible_item_data, status_code=200)

@router.post("/")
def add_temperature(item: Item):
    temperature = item.temperature
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    data_for_cloud = {"temperature": temperature, "date": date}
           
    temperatures_ref = db.collection("temperatures")
    new_temperatures_ref = temperatures_ref.add(data_for_cloud)
    
    document_id = new_temperatures_ref[1].id
    response = {"message": "Temperature added successfully!", "document_id": document_id}
    json_compatible_item_data = jsonable_encoder(response)
    
    return JSONResponse(content=json_compatible_item_data, status_code=201)