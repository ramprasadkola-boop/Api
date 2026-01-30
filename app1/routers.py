from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
async def app1_status():
    return {"app": "App 1", "status": "Operational"}

@router.get("/data")
async def app1_data():
    return {"message": "Data from App 1 endpoint"}