import uvicorn

from src.server import app
from src.settings import settings

print(app)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        log_level="info"
    )