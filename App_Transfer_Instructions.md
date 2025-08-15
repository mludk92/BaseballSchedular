# BaseballSchedular App Transfer Instructions

## App Summary & Technology Overview

**BaseballSchedular** is a web application for scheduling baseball games and events. It features a calendar interface for adding, viewing, and editing events. The app consists of:

- **Frontend:** React (TypeScript, Vite)
  - Provides the interactive calendar UI and event form.
  - Built with Vite for fast development and production builds.
  - Communicates with the backend via REST API calls.
- **Backend:** FastAPI (Python)
  - Serves API endpoints for event CRUD operations.
  - Serves static files for the frontend build.
  - Handles database operations.
- **Database:** PostgreSQL (Heroku Postgres)
  - Stores all event data persistently.
  - Managed by SQLAlchemy ORM in the backend.
- **Deployment:** Heroku
  - Hosts both backend and frontend as a single app.
  - Uses Heroku Postgres for persistent storage.

## How the Technologies Work Together
- The React frontend sends HTTP requests to FastAPI endpoints to create, read, update, and delete events.
- FastAPI processes these requests, interacts with the PostgreSQL database using SQLAlchemy, and returns data to the frontend.
- The frontend is built and its static files are served by FastAPI.
- Heroku runs the backend and serves the built frontend, with the database managed by Heroku Postgres.

---

## Step-by-Step Transfer Instructions

### 1. GitHub Setup
1. **Create a GitHub Account**
   - Go to [github.com](https://github.com/) and sign up.
2. **Fork the Repository**
   - Visit: `https://github.com/mludk92/BaseballSchedular`
   - Click "Fork" to copy the repo to your account.
3. **Clone the Forked Repo**
   - Install [Git](https://git-scm.com/downloads).
   - Run:
     ```bash
     git clone https://github.com/<your-username>/BaseballSchedular.git
     cd BaseballSchedular
     ```

### 2. Heroku Setup
1. **Create a Heroku Account**
   - Go to [heroku.com](https://signup.heroku.com/) and sign up.
2. **Install Heroku CLI**
   - Download: [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. **Log in to Heroku**
   - Run:
     ```bash
     heroku login
     ```
4. **Create a New Heroku App**
   - Run:
     ```bash
     heroku create
     ```
5. **Add Heroku Postgres**
   - Run:
     ```bash
     heroku addons:create heroku-postgresql:essential-0
     ```
6. **Deploy the App**
   - Run:
     ```bash
     git push heroku main
     ```

### 3. Transfer Heroku App Ownership
1. Go to [dashboard.heroku.com](https://dashboard.heroku.com/), log in, and select the app.
2. Click the "Settings" tab.
3. Scroll to "Transfer Ownership" and enter the new owner's Heroku email address.

---

## Making Code Changes & Redeploying

1. **Edit the Code**
   - Make changes in your local repo (frontend or backend).
2. **Build the Frontend (if changed):**
   ```bash
   cd frontend-server
   npm install
   npm run build
   cp -r dist/* ../static/
   cd ..
   git add static/
   git commit -m "Update static assets"
   ```
3. **Commit & Push Changes**
   ```bash
   git add .
   git commit -m "Describe your changes"
   git push heroku main
   ```
4. **Verify on Heroku**
   - Visit your Heroku app URL to confirm changes are live.

---

## Additional Notes
- **Environment Variables:** If you add secrets or config, set them in Heroku via `heroku config:set`.
- **Database:** All event data is stored in Heroku Postgres and persists across deploys.
- **Support:** For help, see the README or contact the original author.

---

**End of Instructions**
