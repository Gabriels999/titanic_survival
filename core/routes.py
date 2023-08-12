from fastapi import APIRouter

from model.model_svc import train_model

router = APIRouter()


@router.get("/model-training/")
async def model_training():
    response = train_model()
    return {**response}


@router.get("/survival-chance-prediction/")
async def measure_survival_probability():
    return {"msg": "You would not survive! I'm sorry."}
