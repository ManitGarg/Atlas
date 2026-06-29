# Atlas

# Phase 0 — Project Setup & Development Environment

**Project Version:** Atlas v1.0

**Documentation Version:** 1.0

**Author:** Manit Garg

**Phase Status:** ✅ Completed

---

# Purpose of this Document

This document records every step performed during **Phase 0** of the Atlas project.

Instead of only documenting *what* was done, this document also explains **why every decision was made**, **why each tool was selected**, **why every folder and file exists**, and **what concepts were learned**.

The goal is that months or even years later, anyone reading this document—including the project author—can understand the complete setup process without relying on memory.

This document also serves as a learning guide. Every important technology introduced during this phase is explained with its purpose in the overall architecture of Atlas.

---

# About Atlas

Atlas is a Personal Student Operating System (PSOS) designed to centralize every aspect of a student's academic and personal productivity into a single intelligent platform.

Rather than being a simple task manager or note-taking application, Atlas aims to function as a complete operating system for students by integrating productivity tools, AI assistance, document management, planning, and personal knowledge management into one unified ecosystem.

Atlas is being developed using modern software engineering practices with an emphasis on scalability, maintainability, clean architecture, and professional development workflows.

---

# Objective of Phase 0

Phase 0 focuses entirely on preparing the development environment before any real application development begins.

No major features are implemented during this phase.

Instead, this phase establishes the technical foundation that every future phase will depend upon.

The objectives of Phase 0 are:

- Initialize the project repository.
- Configure Git and GitHub for version control.
- Design the initial project directory structure.
- Configure Docker for containerized development.
- Set up PostgreSQL using Docker Compose.
- Prepare the Python backend environment.
- Install backend dependencies.
- Create the initial FastAPI application.
- Verify that the backend server runs successfully.
- Establish a professional project architecture.

At the completion of Phase 0, Atlas has a fully functional backend development environment that is ready for feature implementation in Phase 1.

---

# Expected Outcome of Phase 0

After successfully completing this phase, the project should have:

- A professional folder structure.
- A Git repository connected to GitHub.
- Docker installed and configured.
- PostgreSQL running inside Docker.
- A Python virtual environment.
- Backend dependencies installed.
- A working FastAPI server.
- Documentation describing every setup step.

Phase 0 is considered complete only after the FastAPI application successfully responds to requests in the browser.
---

# Section 2 — Software & Tools Used

Before writing any code, a professional development environment must be prepared. During Phase 0, several software tools and technologies were installed and configured. Each of these serves a specific purpose in the Atlas project.

---

## 2.1 Visual Studio Code (VS Code)

### What is VS Code?

Visual Studio Code is a lightweight yet powerful source code editor developed by Microsoft. It supports hundreds of programming languages and provides built-in support for debugging, Git integration, extensions, and terminal access.

### Why was it chosen?

VS Code is one of the most widely used code editors in the software industry because it is:

- Lightweight
- Fast
- Highly customizable
- Cross-platform
- Rich in extensions
- Excellent for Python and web development

### Why Atlas needs VS Code

VS Code serves as the primary development environment for the Atlas project.

Throughout the project, it will be used for:

- Writing Python code
- Building the backend
- Developing the frontend
- Managing Git
- Running Docker
- Debugging applications
- Managing project files
- Running terminal commands

---

## 2.2 Git

### What is Git?

Git is a Distributed Version Control System (DVCS).

Instead of saving only the latest version of a project, Git keeps the complete history of every change made to the project.

This allows developers to:

- Track changes
- Restore previous versions
- Work safely on new features
- Collaborate with other developers

### Why was Git installed?

Atlas is intended to be developed as a professional software project.

Without Git:

- Code history would be lost.
- Mistakes would be difficult to undo.
- Collaboration would become challenging.
- Professional software development practices could not be followed.

### How Atlas uses Git

Git records every meaningful milestone of the project through commits.

Examples include:

- Initial project setup
- Docker configuration
- Database integration
- Authentication system
- AI modules
- Frontend development

Each commit creates a snapshot of the project at that point in time.

---

## 2.3 GitHub

### What is GitHub?

GitHub is a cloud-based platform that hosts Git repositories.

It allows developers to store code online, collaborate with others, and maintain backups of their projects.

### Why Atlas uses GitHub

The Atlas repository is hosted on GitHub so that:

- Source code is safely backed up.
- Progress is available from any computer.
- Every commit is stored online.
- The project can later be shared with recruiters or collaborators.
- Development history is preserved.

GitHub acts as the remote repository, while Git manages the local repository.

---

## 2.4 Python

### What is Python?

Python is a high-level, interpreted programming language known for its readability, simplicity, and extensive ecosystem.

### Why was Python selected?

Atlas uses Python because:

- It integrates well with AI libraries.
- FastAPI is built using Python.
- It has excellent database support.
- Development speed is very high.
- It is one of the most popular backend languages.

### How Atlas uses Python

Python powers the complete backend of Atlas.

Future responsibilities include:

- REST APIs
- AI integration
- Database operations
- Authentication
- Business logic
- Automation tasks

---

## 2.5 FastAPI

### What is FastAPI?

FastAPI is a modern Python framework for building APIs.

It automatically generates API documentation, provides excellent performance, and supports asynchronous programming.

### Why was FastAPI selected?

FastAPI was chosen over traditional frameworks because it offers:

- High performance
- Automatic API documentation
- Type safety
- Easy validation
- Modern architecture
- Scalability

### How Atlas uses FastAPI

FastAPI serves as the backend framework of Atlas.

Every feature developed in Atlas will eventually be exposed through FastAPI endpoints.

Examples include:

- User authentication
- Task management
- Notes management
- AI services
- Calendar integration
- Analytics

---

## 2.6 Docker

### What is Docker?

Docker is a containerization platform.

Instead of installing software directly on the operating system, Docker packages applications and their dependencies into isolated containers.

This ensures that applications behave consistently across different computers.

### Why was Docker installed?

Docker solves the common problem of "it works on my machine."

Every developer uses the same environment, regardless of their operating system.

### How Atlas uses Docker

Atlas currently uses Docker to run PostgreSQL inside a container.

In future phases, Docker may also be used for:

- Backend deployment
- Frontend deployment
- Redis
- Background workers
- Production environments

---

## 2.7 Docker Compose

### What is Docker Compose?

Docker Compose is a tool used to manage multiple Docker containers through a single configuration file.

Instead of manually creating containers one by one, Docker Compose starts every required service with a single command.

### Why Atlas uses Docker Compose

The project currently uses Docker Compose to start PostgreSQL.

As Atlas grows, Docker Compose will also manage additional services such as:

- Backend container
- Frontend container
- Redis
- AI services

---

## 2.8 PostgreSQL

### What is PostgreSQL?

PostgreSQL is a powerful open-source relational database management system (RDBMS).

It stores structured data using tables, relationships, and SQL.

### Why PostgreSQL was selected

PostgreSQL is widely used in production applications because it is:

- Reliable
- Secure
- Scalable
- ACID compliant
- Highly optimized

### How Atlas uses PostgreSQL

All persistent application data will eventually be stored in PostgreSQL.

Examples include:

- User accounts
- Tasks
- Notes
- AI conversations
- Calendar events
- Project data
- Analytics

---

## Summary

By the end of this section, the complete development environment required for Atlas had been established.

These tools together provide:

- A professional code editor
- Version control
- Cloud-based code hosting
- Backend programming language
- API framework
- Database
- Containerized development environment

This setup forms the technological foundation upon which every future phase of Atlas will be built.
---

# Section 3 — Project Folder Structure

A clean and organized project structure is one of the foundations of professional software engineering.

Rather than placing every file in a single directory, Atlas follows a modular folder structure where each folder has a clearly defined responsibility.

This approach improves:

- Readability
- Scalability
- Maintainability
- Team collaboration
- Debugging
- Future expansion

The structure created during Phase 0 acts as the skeleton of the Atlas project. Future phases will gradually populate these folders with implementation code while keeping the architecture clean and organized.

---

# 3.1 Root Directory

```
Atlas/
```

The root directory is the main project folder that contains every component of the Atlas project.

Everything related to Atlas—including the backend, frontend, documentation, assets, Docker configuration, and Git repository—is stored inside this directory.

---

# 3.2 Backend Folder

```
backend/
```

The backend folder contains all server-side code.

The backend is responsible for:

- Business logic
- Database communication
- Authentication
- API development
- AI integration
- Request handling
- Data processing

Atlas uses **FastAPI** as its backend framework, and all backend development takes place inside this folder.

---

# 3.3 Frontend Folder

```
frontend/
```

The frontend folder will contain the complete user interface of Atlas.

Although it is currently empty, future phases will use this folder to develop the web application that users interact with.

Future responsibilities include:

- Dashboard
- Login page
- Notes interface
- Calendar
- Task management
- AI assistant interface
- Settings pages

Keeping the frontend separate from the backend allows both parts of the application to evolve independently.

---

# 3.4 Documentation Folder

```
docs/
```

The docs folder stores all project documentation.

Unlike many personal projects where documentation is created only at the end, Atlas follows a documentation-first approach.

Each phase will have its own document describing:

- Objectives
- Architecture
- Decisions
- Commands used
- Concepts learned
- Problems encountered
- Solutions implemented

This creates a permanent engineering journal for the project.

Examples include:

- Phase_0_Setup.md
- Phase_1_Backend_Foundation.md
- Phase_2_Database.md

---

# 3.5 Assets Folder

```
assets/
```

The assets folder stores static resources used throughout the project.

Examples include:

- Images
- Logos
- Icons
- Diagrams
- Screenshots
- Design files

Keeping assets in one dedicated location prevents unnecessary clutter in the project.

---

# 3.6 Backend Application Folder

```
backend/
└── app/
```

The app folder is the heart of the backend.

Everything related to the FastAPI application is organized inside this directory.

This modular organization makes the project easier to understand and maintain.

---

# 3.7 API Folder

```
app/api/
```

This folder contains all API endpoints.

Whenever a client sends an HTTP request, the corresponding endpoint will be defined here.

Examples include:

- Login API
- Register API
- Task API
- Notes API
- AI API
- Calendar API

Separating endpoints from business logic keeps the project clean and maintainable.

---

# 3.8 Database Folder

```
app/db/
```

The db folder contains all database-related functionality.

Future responsibilities include:

- Database connection
- Session management
- Database initialization
- SQLAlchemy configuration

Instead of scattering database code throughout the project, everything related to PostgreSQL is centralized here.

---

# 3.9 Models Folder

```
app/models/
```

This folder contains SQLAlchemy models.

A model represents the structure of a database table.

For example:

- User
- Task
- Note
- Event
- Project

Each model defines the columns, relationships, and constraints of its corresponding database table.

---

# 3.10 Schemas Folder

```
app/schemas/
```

Schemas define how data enters and leaves the API.

Atlas uses **Pydantic** schemas for:

- Request validation
- Response formatting
- Data serialization

This ensures that only valid data is accepted by the backend.

---

# 3.11 Services Folder

```
app/services/
```

The services folder contains the business logic of the application.

Instead of placing complex logic inside API endpoints, the endpoints call functions from the services layer.

Examples include:

- Creating users
- Authenticating users
- Managing tasks
- AI processing
- File handling

This separation makes the application easier to test and maintain.

---

# 3.12 Core Folder

```
app/core/
```

The core folder stores shared configuration and common utilities used across the backend.

Examples include:

- Application settings
- Environment configuration
- Security utilities
- Authentication helpers
- Constants
- Global configurations

Although this folder is mostly empty during Phase 0, it will become increasingly important as Atlas grows.

---

# 3.13 Tests Folder

```
backend/tests/
```

The tests folder contains automated tests for the backend.

Testing ensures that new features do not accidentally break existing functionality.

Future tests will include:

- API testing
- Authentication testing
- Database testing
- Unit tests
- Integration tests

Professional software projects maintain a dedicated testing directory from the beginning of development.

---

# 3.14 Python Cache Folder

```
__pycache__/
```

This folder is automatically created by Python.

It stores compiled bytecode files (.pyc) to improve execution speed.

These files are generated automatically and should never be edited manually.

Since they can always be regenerated, they are excluded from Git using `.gitignore`.

---

# 3.15 __init__.py Files

```
__init__.py
```

Almost every package inside the backend contains an `__init__.py` file.

This file tells Python that the directory should be treated as a package.

Benefits include:

- Enables module imports
- Organizes project structure
- Supports package initialization
- Improves code modularity

Most `__init__.py` files remain empty during the early stages of development, but they are essential for Python's package system.

---

# Section Summary

By the end of Phase 0, Atlas has a clean and scalable directory structure that follows modern backend development practices.

Every folder has a clearly defined responsibility, ensuring that future development remains organized as the project grows in complexity.

This architecture minimizes confusion, improves maintainability, and provides a solid foundation for all future phases of Atlas.
---

# Section 4 — Project Files Explained

In addition to creating a well-organized folder structure, several important files were created during Phase 0.

Each file serves a specific purpose within the Atlas project. Some files help developers manage the project, while others are required by Python, Docker, Git, or FastAPI.

Understanding the role of every file is essential before moving into feature development.

---

# 4.1 README.md

```
README.md
```

### Purpose

The README file is the first document that visitors see when they open the GitHub repository.

It provides an overview of the project and helps developers understand:

- What the project is
- Why it exists
- Technologies used
- How to set up the project
- How to run the application
- Future roadmap

### Why Atlas needs README.md

A well-written README makes the project easier to understand for:

- Recruiters
- Interviewers
- Contributors
- Future developers
- The project author

As Atlas grows, this file will be continuously updated to reflect new features and setup instructions.

---

# 4.2 LICENSE

```
LICENSE
```

### Purpose

The LICENSE file defines the legal permissions for using, modifying, and distributing the project.

### Why Atlas has a LICENSE

Although Atlas is currently a personal resume project, adding a license is considered a professional software engineering practice.

It clearly communicates:

- Ownership
- Usage rights
- Distribution permissions

During Phase 0, the MIT License was selected because it is simple and widely used in open-source projects.

---

# 4.3 .gitignore

```
.gitignore
```

### Purpose

The `.gitignore` file tells Git which files and folders should **not** be tracked.

Many files are automatically generated during development and should never be uploaded to GitHub.

Examples include:

- Python cache files
- Virtual environments
- IDE settings
- Environment variables
- Build files

### Why Atlas uses .gitignore

Without `.gitignore`, unnecessary files would be committed into the repository, making it:

- Larger
- Harder to maintain
- Less secure

The `.gitignore` file keeps the repository clean and professional.

---

# 4.4 .gitkeep

```
.gitkeep
```

### Purpose

Git does not track empty folders.

If a folder contains no files, Git simply ignores it.

The `.gitkeep` file is a commonly used convention that allows empty directories to remain part of the repository.

### Why Atlas uses .gitkeep

During Phase 0, many folders were intentionally created before they contained any source code.

Adding `.gitkeep` ensured that these folders appeared correctly in GitHub and preserved the intended project structure.

---

# 4.5 docker-compose.yml

```
docker-compose.yml
```

### Purpose

This file defines the Docker services required by Atlas.

Instead of manually creating containers every time, Docker Compose reads this file and automatically starts the required services.

### Current responsibilities

During Phase 0, it starts:

- PostgreSQL container
- Database volume
- Database credentials
- Network configuration

### Why Atlas uses Docker Compose

Without Docker Compose, every developer would need to manually configure PostgreSQL.

Docker Compose automates this process and ensures every development environment is identical.

---

# 4.6 Dockerfile

```
backend/Dockerfile
```

### Purpose

The Dockerfile contains instructions for building the backend Docker image.

It tells Docker:

- Which operating system image to use
- Which Python version to install
- Which dependencies to install
- Which command starts the application

### Why Atlas needs a Dockerfile

Although the backend currently runs locally, future phases will use this file to containerize the FastAPI application for deployment and production environments.

---

# 4.7 requirements.txt

```
backend/requirements.txt
```

### Purpose

This file lists every Python package required by the backend.

Examples include:

- FastAPI
- Uvicorn
- SQLAlchemy
- psycopg2
- Pydantic
- python-dotenv

### Why Atlas uses requirements.txt

Instead of manually installing packages one by one, a developer only needs to run:

```bash
pip install -r requirements.txt
```

This guarantees that everyone working on Atlas installs the same package versions.

---

# 4.8 .env

```
backend/.env
```

### Purpose

The `.env` file stores configuration values and sensitive information.

Examples include:

- Database URL
- JWT Secret Key
- Gemini API Key
- Environment variables

### Why Atlas uses .env

Sensitive information should never be hardcoded into source code.

Keeping secrets inside `.env` improves:

- Security
- Maintainability
- Portability

The `.env` file is also excluded from Git using `.gitignore`.

---

# 4.9 main.py

```
backend/app/main.py
```

### Purpose

This is the entry point of the FastAPI backend.

Whenever the application starts, execution begins from this file.

### Current responsibilities

During Phase 0, `main.py`:

- Creates the FastAPI application
- Configures project metadata
- Defines the first API endpoint
- Verifies that the backend is running successfully

As development continues, this file will also register routers, middleware, and startup events.

---

# 4.10 __init__.py

```
__init__.py
```

### Purpose

The `__init__.py` file tells Python that a directory should be treated as a package.

### Why Atlas uses __init__.py

These files enable Python to:

- Import modules correctly
- Organize backend code into packages
- Support scalable application architecture

Most of these files remain empty during the early stages of development because their primary purpose is package initialization.

---

# 4.11 .venv (Virtual Environment)

```
backend/.venv/
```

### Purpose

The `.venv` directory contains the project's isolated Python environment.

It stores:

- Python interpreter
- Installed packages
- Executable scripts

### Why Atlas uses a Virtual Environment

Using a virtual environment prevents conflicts between different Python projects on the same computer.

Each project can have its own package versions without affecting other projects.

This is considered a standard practice in professional Python development.

---

# Section Summary

By the end of Phase 0, every essential project file had been created and configured.

Together, these files provide:

- Project documentation
- Version control configuration
- Dependency management
- Container configuration
- Environment configuration
- Backend initialization
- Python package organization

Although many of these files contain only a small amount of content during Phase 0, they form the foundation that every future phase of Atlas will build upon.