from fastapi import FastAPI
from routers import cultivos_routers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# SOLUCIÓN CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # puedes restringir luego
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cultivos_routers.router)

@app.get("/")
def root():
    return {"message": "Recomendación de cultivos con ML"}