from fastapi import APIRouter

from core.schemas import TitanicPassenger
from model.model_svc import predict_passenger, train_model

router = APIRouter()


@router.get("/model-training/")
async def model_training():
    response = train_model()
    return {**response}


@router.post("/survival-prediction/")
async def measure_survival_probability(request: TitanicPassenger):
    prediction = predict_passenger(request)
    subtitle = {
        0: "not survive.",
        1: "survive!"
     }
    return {"msg": f"You would {subtitle[prediction]}"}
