from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return 'Hello, World! UEA - Computação em Nuvem'