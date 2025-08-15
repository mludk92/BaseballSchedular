from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.messages import router as messages_router
from routes.events import router as events_router
from logger import get_logs
from database import init_db

# Ensure database tables are created on startup
init_db()


# Initialize FastAPI application
app = FastAPI()

# Configure CORS to allow frontend (localhost:3000) to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Replace with your deployed frontend URL for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi.staticfiles import StaticFiles
import os

# Register the message-related routes with the application
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")
app.include_router(messages_router)
app.include_router(events_router)


# Catch-all route for frontend (serves index.html for all non-API routes)


from fastapi.responses import FileResponse
from fastapi import Request

@app.get("/{full_path:path}")
async def serve_frontend(full_path: str, request: Request):
    # Serve static files and assets directly
    asset_path = os.path.join(static_dir, full_path)
    if (
        full_path.startswith("assets/")
        or full_path.startswith("static/")
        or full_path.startswith("api/")
        or full_path.endswith(".js")
        or full_path.endswith(".css")
        or full_path.endswith(".svg")
    ):
        if os.path.exists(asset_path):
            return FileResponse(asset_path)
        return {"error": "Not found"}
    # Otherwise, serve index.html for SPA routing
    index_path = os.path.join(static_dir, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "Welcome to the API server!"}
    
@app.get("/logs")  # ✅ Serve logs at this endpoint
def show_logs():
    return get_logs()