from fastapi import APIRouter

router = APIRouter()


@router.get("/hello/")
async def hello_world():
    return {"msg": "Hello World"}


@router.get("/model-training/")
async def model_training():
    return {"msg": "New model accuracy: 93%"}


@router.get("/survival-chance-prediction/")
async def measure_survival_probability():
    return {"msg": "You would not survive! I'm sorry."}
