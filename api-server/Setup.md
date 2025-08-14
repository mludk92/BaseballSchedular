# 🚀 Setup Instructions

## 1. Clone and Open the Repository

```bash
git clone https://github.com/mludk92/software-engineer-2-assessment.git
cd software-engineer-2-assessment
```

---

# 🚀 Running the Application

## 1. Frontend Server (React)

```bash
cd frontend-server
npm install        # Install required dependencies
npm start          # Start the frontend server
```

- Frontend will be available at: `http://localhost:3000`
- _(Note: If you are on Windows and cannot access `localhost`, you may need to edit your hosts file to map `127.0.0.1` to `localhost`.)_

---

## 2. Backend Server (FastAPI)

```bash
cd api-server
python -m venv venv
# Activate virtual environment
source venv/Scripts/activate    # Windows
# or
source venv/bin/activate        # Mac/Linux

# Install backend dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

- Backend API will be available at: `http://127.0.0.1:8000`
- API documentation (Swagger UI) will be available at: `http://127.0.0.1:8000/docs`

---


# 📦 Libraries and Technologies Used

## Frontend (React + Vite + TypeScript)
- **React** — JavaScript library for building user interfaces.
- **Vite** — Frontend build tool for rapid development and hot reloading.
- **TypeScript** — Strong typing for React components and state management.
- **CSS Modules** — Component-scoped styles (`App.css`).

## Backend (FastAPI + Python)
- **FastAPI** — High-performance Python web framework for APIs.
- **Uvicorn** — ASGI server for running FastAPI applications.
- **SQLAlchemy** — ORM (Object Relational Mapper) for interacting with SQLite database easily.
- **Pydantic** — Data validation and parsing using Python type hints.

## Database
- **SQLite3** — Lightweight file-based database, easy to set up locally without separate server installation.

---

# 📋 Quick Summary

| Component | Command | URL |
|:----------|:--------|:----|
| Frontend | `npm start` | [http://localhost:3000](http://localhost:3000) |
| Backend | `uvicorn app:app --reload` | [http://127.0.0.1:8000](http://127.0.0.1:8000) |
| API Docs | (auto) | [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) |

---

# 🙏 Thank You