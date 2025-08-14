from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.messages import router as messages_router
from routes.events import router as events_router
from logger import get_logs

# Initialize FastAPI application
app = FastAPI()

# Configure CORS to allow frontend (localhost:3000) to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ✅ List allowed frontend origin explicitly
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the message-related routes with the application
app.include_router(messages_router)
app.include_router(events_router)

# Root endpoint to verify server is running
@app.get("/")
def root():
    return {"message": "Welcome to the API server!"}
    
@app.get("/logs")  # ✅ Serve logs at this endpoint
def show_logs():
    return get_logs()