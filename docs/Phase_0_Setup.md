# Phase 0 – Development Environment & Project Setup

**Project:** Atlas (Personal Student Operating System)
**Phase:** 0 – Development Environment & Project Setup
**Status:** ✅ Completed

---

# Objective

Before writing any actual features, I wanted to set up a clean and professional development environment. The idea was to create a project structure that would be easy to maintain as Atlas grows. By the end of this phase, the backend should be running successfully, PostgreSQL should be connected through Docker, and the project should be stored safely on GitHub.

---

# What I Completed

During this phase, I completed the following tasks:

* Created the Atlas project repository.
* Initialized Git and connected it with GitHub.
* Created the initial folder structure.
* Installed and configured Docker Desktop.
* Ran PostgreSQL inside a Docker container.
* Created the backend project structure.
* Created a Python virtual environment.
* Installed the required Python packages.
* Built the first FastAPI application.
* Successfully ran the backend locally.
* Verified the API using the browser and Swagger documentation.

At this point, the project has a stable foundation and is ready for actual backend development.

---

# Project Structure Created

```text
Atlas/
│
├── assets/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
├── docs/
├── frontend/
│
├── docker-compose.yml
├── README.md
├── LICENSE
└── .gitignore
```

---

# Why These Folders Exist

### backend/

This folder contains the complete backend application.

### app/

This is the main FastAPI application.

### api/

All API routes will be placed here.

### core/

Configuration files, settings, authentication, and reusable utilities will be stored here.

### db/

Everything related to database connections and sessions will be managed here.

### models/

SQLAlchemy database models will be created here.

### schemas/

Pydantic request and response models will be stored here.

### services/

Business logic will be written here instead of directly inside API routes.

### tests/

This folder will contain unit tests and API tests later in the project.

### docs/

Every completed phase will be documented here so that the project's development journey is recorded from beginning to end.

### frontend/

The React frontend will be developed here in later phases.

### assets/

Images, icons, logos, and other project resources will be stored here.

---

# Files Created

## README.md

Contains the project overview, roadmap, technology stack, and current progress.

---

## docker-compose.yml

This file starts PostgreSQL using Docker.

Instead of installing PostgreSQL directly on Windows, I decided to use Docker so the project remains portable. Anyone cloning the repository only needs Docker installed to run the same database setup.

---

## Dockerfile

This file describes how the backend application will run inside a Docker container in later phases.

Right now it is simple, but it will become more useful as the project grows.

---

## requirements.txt

Contains all Python packages used by the backend.

This allows the entire environment to be recreated with a single command:

```bash
pip install -r requirements.txt
```

---

## .env

Stores configuration values such as database credentials and API keys.

Sensitive information should never be hardcoded into the source code.

---

## .gitignore

Prevents unnecessary files like virtual environments, cache files, and temporary files from being uploaded to GitHub.

---

## .gitkeep

Git does not track empty folders.

Adding a `.gitkeep` file allows empty folders to remain in the repository until actual code is added.

---

## **init**.py

These files mark folders as Python packages.

This allows Python to import modules correctly from different directories.

---

## main.py

This is the entry point of the FastAPI application.

Currently it creates the FastAPI app and exposes a simple test endpoint to confirm that the backend is working correctly.

---

# Software and Tools Used

* Visual Studio Code
* Git
* GitHub
* Python 3.14
* FastAPI
* Uvicorn
* PostgreSQL
* Docker Desktop
* Docker Compose

---

# Commands Used

```bash
git init
git add .
git commit -m "Initial project structure"

python -m venv .venv

pip install -r requirements.txt

docker compose up -d

uvicorn app.main:app --reload
```

---

# Problems I Faced

### GitHub Repository

Initially I committed everything locally, but nothing appeared on GitHub.

The issue was that the remote repository had not been connected correctly. After adding the remote and pushing the `main` branch, everything appeared on GitHub.

---

### Python Interpreter

VS Code was showing import errors even after installing FastAPI.

The problem was that VS Code was using the global Python interpreter instead of the virtual environment.

After selecting the `.venv` interpreter, the errors disappeared.

---

### Docker

The PostgreSQL container started successfully, but Docker showed a warning that the `version` field in `docker-compose.yml` is deprecated.

This does not stop the project from running, but the file can be updated later by removing the version field.

---

# What I Learned

This phase was less about writing code and more about setting up a professional development environment.

I learned how Git, GitHub, Docker, PostgreSQL, virtual environments, and FastAPI fit together in a real backend project.

I also understood why a clean folder structure is important before adding features. Spending time on setup now should make future development much easier.

---

# Phase Summary

Phase 0 was all about preparing the project.

The backend is running successfully, PostgreSQL is available through Docker, the repository is connected to GitHub, and the project has a clean structure ready for development.

The next phase will focus on building the actual backend foundation, starting with configuration management, database integration, and user authentication.

---

**Phase Status:** ✅ Completed
