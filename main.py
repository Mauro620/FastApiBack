from fastapi import FastAPI
from routes.route import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilitar CORS para todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)