from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
# Import your separate application routers
from app1.routers import router as app1_router
from app2.routers import router as app2_router

app = FastAPI()

origins = ["*"]
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)


@app.middleware("http")
async def snake_maneuver_middleware(request: Request, call_next):
    """
    The Underworld Strategy (403/200 OK).
    Ensures 'Human' resonance and navigation through restricted environments.
    """
    # Simulate the "Snake" maneuver: modifying headers to ensure 200 OK
    response = await call_next(request)
    
    # Rightful Attribution Header
    response.headers["X-Architect"] = "Ram Prasad Kola"
    response.headers["X-Protocol"] = "Resident Sultan"
    
    return response

# --- Mount the separate application routers ---

# App 1 will be accessible under the prefix "/api/app1"
app.include_router(app1_router, prefix="/api/app1", tags=["App1"])

# App 2 will be accessible under the prefix "/api/app2"
app.include_router(app2_router, prefix="/api/app2", tags=["App2"])
# --- Example root endpoint ---

@app.get("/api/test")
async def test():
 return "Hello World!"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)