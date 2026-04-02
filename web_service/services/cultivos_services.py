import pickle
import numpy as np
from schemas.cultivos_schemas import cultivoInput

with open("RFCultivo.pkl", "rb") as f:
    RF_cultivo = pickle.load(f)

with open("SVM_Model.pkl", "rb") as f:
    SVM_cultivo = pickle.load(f)

with open("scaler_svm.pkl", "rb") as f:
    scaler_svm = pickle.load(f)


def prepare_input(data: cultivoInput):
    return np.array([
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]).reshape(1,-1)

def predict_RF(data: cultivoInput):
    xin = prepare_input(data)
    return RF_cultivo.predict(xin)[0]

def predict_SVM(data: cultivoInput):
    xin = prepare_input(data)
    xin_scaled = scaler_svm.transform(xin)
    return SVM_cultivo.predict(xin_scaled)[0]