from fastapi import APIRouter
from schemas.cultivos_schemas import cultivoInput
from services.cultivos_services import predict_RF, predict_SVM

router = APIRouter()

@router.post("/predict/rf")
def predict_random_forest(data: cultivoInput):
    prediction = predict_RF(data)
    return {"modelo": "RandomForest", "predicción": prediction}

@router.post("/predict/svm")
def predict_svm_model(data: cultivoInput):
    prediction = predict_SVM(data)
    return {"modelo": "SVM", "predicción": prediction}