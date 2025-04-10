from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Initialisation FastAPI
app = FastAPI(title="Amazing - API de segmentation")

# Chargement des modèles
with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
with open("models/pca.pkl", "rb") as f:
    pca = pickle.load(f)
with open("models/kmeans.pkl", "rb") as f:
    kmeans = pickle.load(f)

# Format attendu de l'entrée
class UserFeatures(BaseModel):
    features: list[float]

# Endpoint de prédiction
@app.post("/predict_cluster/")
def predict_cluster(data: UserFeatures):
    try:
        scaled = scaler.transform([data.features])
        reduced = pca.transform(scaled)
        cluster = kmeans.predict(reduced)[0]
        return {"cluster": int(cluster)}
    except Exception as e:
        return {"error": str(e)}