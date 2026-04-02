from fastapi import FastAPI
from routers import cultivos_routers

app = FastAPI()

app.include_router(cultivos_routers.router)

@app.get("/")
def root():
    return {"message": "Recomendación de cultivos con ML"}