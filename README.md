# Atlas v1.0

> **Personal Student Operating System**

Atlas is an open-source Personal Student Operating System designed to bring every essential part of a student's academic life into one organized platform.

Instead of switching between multiple apps for notes, assignments, finances, schedules, and AI tools, Atlas aims to provide a single workspace where everything is connected.

---

# Why Atlas?

Most students use different applications for:

- Notes
- Assignments
- Expenses
- Study Planning
- Exam Tracking
- AI Assistance

Atlas combines all of them into one unified system.

---

# 🚀 Current Status

**Version:** v1.0

Current Development Phase:

✅ Phase 0 — Project Initialization

✅ Phase 1 — Backend Foundation

⏳ Phase 2 — Academic Module

⏳ Phase 3 — Finance Module

⏳ Phase 4 — Dashboard & AI Integration

---

# ✨ Features (Current)

### Backend

- FastAPI
- PostgreSQL
- SQLAlchemy ORM
- Docker Database
- REST API

### User Management

- Create User
- Get All Users
- Get User by ID
- Update User
- Delete User

### Architecture

- Layered Architecture
- Service Layer
- Dependency Injection
- Pydantic Validation
- Automatic Table Creation

### Documentation

- Swagger UI
- OpenAPI Specification

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

## Database

- PostgreSQL

## Containerization

- Docker
- Docker Compose

## Tools

- VS Code
- Git
- GitHub

---

# 🏗 Project Architecture

```
Client
   │
   ▼
FastAPI Routes
   │
   ▼
Services
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL
```

---

# 📁 Project Structure

```
Atlas/
│
├── assets/
│
├── backend/
│   ├── app/
│   │
│   ├── api/
│   │   ├── routes/
│   │   │   ├── health.py
│   │   │   └── user.py
│   │   └── router.py
│   │
│   ├── core/
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── dependencies.py
│   │   ├── init_db.py
│   │   └── session.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── schemas/
│   │   └── user.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   ├── tests/
│   │
│   └── main.py
│
├── docs/
│
├── frontend/
│
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

# 📖 API Documentation

After starting the backend, open:

```
http://127.0.0.1:8000/docs
```

Swagger UI provides interactive documentation for all API endpoints.

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/ManitGarg/Atlas.git
```

Move into the project

```bash
cd Atlas
```

---

## Backend Setup

```bash
cd backend
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Database

Start PostgreSQL

```bash
docker compose up -d
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 📌 Current API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Health Check |
| POST | /users | Create User |
| GET | /users | Get All Users |
| GET | /users/{id} | Get User |
| PUT | /users/{id} | Update User |
| DELETE | /users/{id} | Delete User |

---

# 🗺 Roadmap

## ✅ Phase 0

- Project Setup
- Docker
- PostgreSQL
- GitHub Repository

---

## ✅ Phase 1

- SQLAlchemy
- User Model
- CRUD APIs
- Swagger Documentation
- Layered Architecture

---

## ⏳ Phase 2

Academic Module

- Subjects
- Notes
- Assignments
- Exams
- Attendance

---

## ⏳ Phase 3

Finance Module

- Expense Tracking
- Pocket Money
- Monthly Reports
- Savings Goals

---

## ⏳ Phase 4

Dashboard

- Student Dashboard
- Analytics
- AI Features
- Productivity Insights

---

# 🌟 Future Plans

- Authentication & Authorization
- JWT Login
- Study Planner
- Notes Management
- Finance Tracking
- AI Assistant
- Dashboard Analytics
- Notifications
- Mobile Responsive Frontend

---

# 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

If you'd like to improve Atlas, feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Manit Garg**

Electrical & Computer Engineering Student

Building Atlas — Personal Student Operating System