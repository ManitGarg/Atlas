1. Phase Overview
Phase 1 focused on building the complete backend foundation for Atlas v1.0. The objective of this phase was to create a scalable and maintainable backend architecture that would support all future modules of the project. Instead of directly implementing features, this phase concentrated on establishing the core infrastructure required for backend development.

During this phase, the FastAPI project was configured, PostgreSQL was connected as the primary database, SQLAlchemy ORM was integrated for database operations, and the project structure was organized using a layered architecture. The backend was divided into separate components such as API routes, database configuration, models, schemas, services, and dependency management to improve maintainability and scalability.

The first database model (User) was created, followed by the implementation of complete CRUD (Create, Read, Update, Delete) operations. Every API endpoint was tested using Swagger UI to verify correct request handling, response generation, and database interaction. Throughout the phase, multiple debugging sessions were carried out to resolve configuration issues, dependency errors, import problems, and database constraints.

By the end of Phase 1, Atlas had a fully functional backend capable of handling REST API requests, communicating with PostgreSQL, validating incoming data, and performing database operations using a clean and production-inspired architecture. This backend foundation will serve as the base for all future modules developed in later phases of the project.

2. Objectives

The primary objective of Phase 1 was to establish a strong backend foundation for Atlas that could support future development without requiring major architectural changes. Rather than focusing on advanced features, this phase concentrated on building a clean, organized, and scalable backend structure following industry-standard practices.

The specific objectives achieved during this phase were:

Set up the FastAPI backend application with a modular project structure.
Configure environment variables for secure and centralized project configuration.
Establish a successful connection between the application and the PostgreSQL database.
Integrate SQLAlchemy ORM to simplify database operations and object-relational mapping.
Create the base database configuration and session management system.
Design and implement the first database model (User).
Create Pydantic schemas for request validation and response serialization.
Implement dependency injection for efficient database session management.
Build a service layer to separate business logic from API endpoints.
Develop a complete RESTful CRUD API for the User module.
Organize API routes using a centralized routing system.
Verify all backend functionality using Swagger UI.
Test Create, Read, Update, and Delete operations against the PostgreSQL database.
Ensure the project follows a clean and maintainable layered architecture that can be extended easily in future phases.

By completing these objectives, Atlas now has a reliable backend foundation capable of supporting larger modules such as Academic Management, Finance Tracking, Dashboard, and AI-powered features in the upcoming phases.

3. Technologies and Tools Used

During Phase 1, several technologies and development tools were used to build the backend foundation of Atlas. Each technology was selected based on its suitability for modern backend development, scalability, ease of maintenance, and community support.

Python

Python was used as the primary programming language for backend development. It provides clean syntax, extensive library support, and excellent compatibility with modern web development frameworks.

Purpose:

Backend programming
Database interaction
API development
Business logic implementation
FastAPI

FastAPI served as the backend web framework for Atlas. It was chosen because of its high performance, automatic API documentation, built-in request validation, and excellent developer experience.

Purpose:

Building REST APIs
Handling HTTP requests and responses
Automatic Swagger/OpenAPI documentation
Request and response validation
PostgreSQL

PostgreSQL was selected as the primary relational database for storing application data. It is reliable, scalable, and widely used in production applications.

Purpose:

Store user information
Manage relational data
Provide persistent storage for future Atlas modules
SQLAlchemy

SQLAlchemy was used as the Object Relational Mapper (ORM). Instead of writing raw SQL queries, SQLAlchemy allows interaction with the database using Python classes and objects.

Purpose:

Database abstraction
Table creation
CRUD operations
Object-relational mapping
Pydantic

Pydantic was used for request validation and response serialization. It ensures that incoming API data matches the expected format before being processed.

Purpose:

Validate user input
Serialize API responses
Improve API reliability
Prevent invalid data from entering the application
Uvicorn

Uvicorn was used as the ASGI server to run the FastAPI application during development.

Purpose:

Run the backend server
Handle incoming HTTP requests
Enable hot reloading during development
Docker

Docker was used to containerize the PostgreSQL database, ensuring that the development environment remains consistent across different systems.

Purpose:

Run PostgreSQL inside a container
Simplify database setup
Avoid manual database installation
Maintain consistent development environments
Docker Compose

Docker Compose was used to define and manage the PostgreSQL container using a configuration file.

Purpose:

Start and stop database services easily
Store database configuration in code
Simplify project setup
Git

Git was used as the version control system throughout the development process.

Purpose:

Track code changes
Maintain project history
Manage development milestones
GitHub

GitHub was used to host the Atlas repository and maintain backups of every completed phase.

Purpose:

Remote repository hosting
Version history
Project documentation
Code backup
Visual Studio Code

Visual Studio Code was used as the primary code editor during development.

Purpose:

Writing and editing code
Integrated terminal
Git integration
Extension support for Python and FastAPI
Swagger UI

Swagger UI was automatically generated by FastAPI and used extensively to test every API endpoint without requiring external API testing tools.

Purpose:

Interactive API documentation
CRUD endpoint testing
Request and response verification
Summary

The combination of these technologies provided a modern backend development environment that emphasizes clean architecture, scalability, maintainability, and ease of development. Together, they form the technical foundation upon which all future Atlas modules will be developed.

Folder Structure Before and After Phase 1

One of the major goals of Phase 1 was not only to write backend code but also to organize the project using a clean and scalable folder structure. A well-structured project makes development easier, improves readability, and allows new features to be added without creating unnecessary complexity.

Before beginning Phase 1, the backend contained only the basic project setup completed during Phase 0. During Phase 1, additional folders and files were created to separate different responsibilities such as routing, database management, models, schemas, and business logic.

Folder Structure Before Phase 1
Atlas/
│
├── assets/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   └── health.py
│   │   │   └── router.py
│   │   │
│   │   ├── core/
│   │   │   └── config.py
│   │   │
│   │   ├── db/
│   │   │   └── session.py
│   │   │
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── tests/
│   ├── .env
│   ├── requirements.txt
│   └── Dockerfile
│
├── docs/
├── frontend/
├── docker-compose.yml
├── README.md
└── LICENSE

At this stage, the project had only the basic backend setup. The API could start successfully, and the database connection was configured, but no database models, schemas, or CRUD functionality had been implemented.

Folder Structure After Phase 1
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
│   │   └── config.py
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
│   ├── __init__.py
│   └── main.py
│
├── tests/
├── .env
├── requirements.txt
├── Dockerfile
│
├── docs/
├── frontend/
├── docker-compose.yml
├── README.md
└── LICENSE
New Components Added During Phase 1
api/routes/user.py

Contains all User-related API endpoints, including Create, Read, Update, and Delete operations.

db/base.py

Defines the SQLAlchemy Declarative Base that serves as the parent class for all database models.

db/dependencies.py

Provides database sessions to API endpoints using FastAPI's dependency injection system.

db/init_db.py

Initializes the database by creating tables based on the defined SQLAlchemy models.

models/user.py

Defines the User database model and maps it to the users table in PostgreSQL.

schemas/user.py

Contains Pydantic schemas used for validating incoming requests and formatting API responses.

services/user_service.py

Implements the business logic for all User-related database operations. This keeps API routes clean by separating request handling from database logic.

Why This Structure?

The backend follows a layered architecture, where each folder has a single responsibility.

API Layer handles HTTP requests and responses.
Service Layer contains business logic.
Schema Layer validates request and response data.
Model Layer represents database tables.
Database Layer manages database connections, sessions, and initialization.

This separation improves code readability, reduces duplication, simplifies debugging, and makes the project easier to maintain as Atlas grows in future phases.

5. Files Created and Modified

During Phase 1, several new files were created to implement the backend architecture and the User CRUD module. Existing files from Phase 0 were also modified to integrate the new components. Each file was created with a specific responsibility, following the principle of separation of concerns.

5.1 Newly Created Files
1. app/api/routes/user.py

Purpose

This file contains all API endpoints related to the User module. It receives HTTP requests from the client, validates incoming data using Pydantic schemas, and delegates the actual database operations to the service layer.

Why it was created

Instead of writing all endpoints inside main.py, a dedicated route file keeps the project modular and makes it easier to manage multiple modules in the future.

2. app/db/base.py

Purpose

Defines the SQLAlchemy Declarative Base class.

Why it was created

Every SQLAlchemy model must inherit from a common base class. This file centralizes that base so all models share the same metadata.

3. app/db/dependencies.py

Purpose

Provides database sessions using FastAPI's dependency injection mechanism.

Why it was created

Instead of manually creating and closing database sessions inside every endpoint, this file automatically manages database connections for each request.

4. app/db/init_db.py

Purpose

Initializes the database by creating all tables defined in the SQLAlchemy models.

Why it was created

To automate database initialization during application startup, eliminating the need to manually create tables using SQL commands.

5. app/models/user.py

Purpose

Defines the structure of the users table in PostgreSQL.

Why it was created

This model acts as the bridge between Python objects and database records using SQLAlchemy ORM.

6. app/schemas/user.py

Purpose

Contains Pydantic schemas used for request validation and API responses.

Why it was created

Database models and API schemas have different responsibilities. Keeping them separate improves maintainability and prevents exposing internal database structures.

7. app/services/user_service.py

Purpose

Contains all business logic related to User operations.

Why it was created

Rather than writing SQLAlchemy queries directly inside API routes, all database-related operations are centralized in one location, making the code reusable and easier to maintain.

5.2 Modified Files
1. app/main.py
Changes Made
Registered the central API router.
Added database initialization during application startup.
Connected all backend modules together.
Reason

This file became the central entry point responsible for starting the FastAPI application and initializing the backend.

2. app/api/router.py
Changes Made
Registered the Health router.
Registered the User router.
Reason

Instead of importing every route directly into main.py, a central router improves organization and scalability.

3. app/db/session.py
Changes Made
Configured SQLAlchemy Engine.
Configured Session Factory.
Reason

Provides a centralized database connection used throughout the application.

4. requirements.txt
Changes Made

Added all backend dependencies, including:

FastAPI
SQLAlchemy
PostgreSQL Driver (psycopg2-binary)
Pydantic
Pydantic Settings
Uvicorn
Python Dotenv
Email Validator
Reason

Ensures every developer can recreate the exact backend environment using a single installation command.

5.3 Files Used During Phase 1

Although these files were created during Phase 0, they played an important role during Phase 1.

.env

Used to securely store environment variables such as the PostgreSQL connection string.

docker-compose.yml

Used to start and manage the PostgreSQL Docker container.

README.md

Updated to reflect the completion of Phase 1 and document the current project status.

6. Detailed File Explanation

This section explains every major file created or modified during Phase 1. Each file is discussed individually, including its purpose, responsibilities, important code, and how it interacts with the rest of the backend. Understanding these files is essential because together they form the complete backend architecture of Atlas.

6.1 app/main.py
Purpose

main.py is the entry point of the FastAPI application. Whenever the backend server starts using Uvicorn, execution begins from this file.

It is responsible for creating the FastAPI application, initializing the database, and registering all API routes.

Responsibilities
Create the FastAPI application.
Configure application metadata.
Initialize the database during startup.
Register all API routes.
Start the backend application.
Important Code
app = FastAPI(
    title="Atlas API",
    description="Backend API for Atlas - Personal Student Operating System",
    version="1.0.0",
)
Explanation

This creates the FastAPI application object.

The metadata provided here is automatically used to generate Swagger UI and OpenAPI documentation.

title → Name displayed in Swagger UI.
description → Brief description of the project.
version → Current API version.
@app.on_event("startup")
def startup():
    init_db()
Explanation

This function executes automatically every time the backend starts.

Its responsibility is to initialize the database by creating all tables defined in the SQLAlchemy models if they do not already exist.

This eliminates the need to manually create tables using SQL commands.

app.include_router(api_router)
Explanation

Instead of defining every API endpoint inside main.py, FastAPI allows routers to be registered.

This statement imports every route defined inside api/router.py.

As Atlas grows, new modules can simply be registered inside the router without modifying main.py.

Why this approach?

Keeping main.py small makes the project easier to maintain.

Instead of containing hundreds of API endpoints, it acts only as the application's entry point and configuration file.

6.2 app/core/config.py
Purpose

This file manages all application configuration.

Instead of hardcoding values like database URLs inside the source code, they are loaded from environment variables.

Responsibilities
Read values from .env
Store project configuration
Make configuration available throughout the application
Why use environment variables?

Hardcoding database passwords inside source code is insecure.

Environment variables allow configuration to change without modifying the source code.

This also prevents sensitive information from being uploaded to GitHub.

Why Pydantic Settings?

Pydantic automatically validates configuration values and converts them into Python objects.

This reduces configuration errors and centralizes all settings in one location.

6.3 app/db/session.py
Purpose

This file creates the connection between FastAPI and PostgreSQL.

Every database operation performed anywhere in the project depends on the objects defined here.

Responsibilities
Create SQLAlchemy Engine
Create Session Factory
Configure database communication
Important Code
engine = create_engine(settings.DATABASE_URL)
Explanation

The Engine represents the application's connection to PostgreSQL.

It does not execute queries directly.

Instead, it manages communication between SQLAlchemy and the database.

SessionLocal = sessionmaker(...)
Explanation

A Session represents one conversation with the database.

Every API request receives its own Session.

This prevents different requests from interfering with each other.

Engine vs Session

Many beginners confuse these two concepts.

Engine

Permanent database connection manager.

Session

Temporary workspace used to perform database operations.

Think of the Engine as the road connecting your application to PostgreSQL, while a Session is the vehicle traveling on that road.

6.4 app/db/base.py
Purpose

Defines the parent class for every SQLAlchemy model.

Responsibilities
Create Declarative Base
Store metadata of every database model
Why is Base needed?

Every SQLAlchemy model inherits from this Base class.

Without it, SQLAlchemy would not know which classes represent database tables.

It also stores metadata that is later used by create_all() to automatically generate database tables.

6.5 app/db/init_db.py
Purpose

Automatically create database tables during application startup.

Responsibilities
Load all models
Register metadata
Create tables
Important Code
Base.metadata.create_all(bind=engine)
Explanation

This command checks every registered SQLAlchemy model.

If the corresponding table does not exist inside PostgreSQL, SQLAlchemy creates it automatically.

Existing tables remain unchanged.

Why use this?

During development, developers do not need to manually create tables using SQL.

Starting the application is enough.
6.6 app/db/dependencies.py
Purpose

This file provides database sessions to API endpoints using FastAPI's Dependency Injection system.

Instead of manually creating and closing a database session inside every route, FastAPI automatically manages the session lifecycle through this dependency.

This makes the code cleaner, reduces duplication, and ensures database connections are always closed properly after every request.

Responsibilities
Create a database session for each request.
Provide the session to API routes.
Automatically close the session after the request is completed.
Prevent connection leaks.
Important Code
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
Code Explanation
db = SessionLocal()

Creates a new database session.

This session acts as a temporary workspace where SQLAlchemy performs all database operations for the current request.

yield db

Instead of returning the session, FastAPI uses yield.

When the API endpoint starts executing, FastAPI pauses the function at yield and sends the database session to the endpoint.

After the endpoint finishes executing, FastAPI automatically returns to this function and executes everything written inside the finally block.

db.close()

Closes the database session.

Closing the session releases the database connection back to SQLAlchemy's connection pool, preventing unnecessary resource usage.

Why use Dependency Injection?

Without dependency injection, every API endpoint would need to create and close its own database session.

Example:

db = SessionLocal()

# CRUD operations

db.close()

This code would have to be repeated in every route.

Using Dependency Injection allows every endpoint to simply receive the database session as a parameter:

db: Session = Depends(get_db)

FastAPI automatically handles everything else.

Benefits
Cleaner code
No repeated session creation
Automatic cleanup
Better scalability
Easier testing
Recommended FastAPI practice
6.7 app/models/user.py
Purpose

This file defines the User database model.

A model represents a table inside PostgreSQL.

Each object of the User class corresponds to one row in the users table.

Instead of writing SQL statements manually, SQLAlchemy converts Python objects into database records.

Responsibilities
Define the structure of the users table.
Specify column names and data types.
Configure constraints such as Primary Key and Unique values.
Enable ORM mapping between Python objects and PostgreSQL.
Important Code
class User(Base):
Explanation

Every database model must inherit from Base.

This tells SQLAlchemy that this class should be treated as a database table.

__tablename__ = "users"
Explanation

Specifies the actual table name inside PostgreSQL.

Without this, SQLAlchemy would generate a table name automatically.

Using an explicit table name makes the database easier to understand.

id = Column(Integer, primary_key=True, index=True)
Explanation

Creates the Primary Key of the table.

Integer data type.
Automatically increments.
Every record gets a unique ID.
Indexed for faster searching.
full_name = Column(String, nullable=False)
Explanation

Stores the user's full name.

nullable=False means this field is mandatory.

The database will reject records where the name is missing.

email = Column(String, unique=True, index=True, nullable=False)
Explanation

Stores the user's email address.

Important constraints:

unique=True → Two users cannot have the same email.
index=True → Speeds up searching.
nullable=False → Email is required.

This is why we encountered the UniqueViolation error while testing duplicate emails during development.

Why use Models?

Models represent how data is stored inside the database.

They define:

Table names
Columns
Data types
Constraints
Relationships (in future phases)

Every database operation performed by SQLAlchemy is based on these model definitions.

Summary

The User model became the first database model of Atlas and established the pattern that future models such as Subjects, Notes, Assignments, Expenses, and Exams will follow.
6.8 app/schemas/user.py
Purpose

This file contains all Pydantic Schemas used by the User module.

Unlike SQLAlchemy Models, which define how data is stored inside the database, Schemas define how data is received from clients and how responses are returned by the API.

Schemas act as a validation layer between the client and the database.

Responsibilities
Validate incoming request data.
Define the structure of API responses.
Prevent invalid data from reaching the database.
Automatically generate request and response documentation in Swagger UI.
Why are Schemas Separate from Models?

Although Models and Schemas may appear similar, they serve completely different purposes.

Model
Represents a database table.
Interacts directly with PostgreSQL.
Used by SQLAlchemy.
Schema
Represents API request and response data.
Performs validation.
Used by FastAPI and Pydantic.

Keeping these responsibilities separate makes the application easier to maintain and more secure.

UserCreate Schema
Purpose

Defines the data required when creating a new user.

Important Code
class UserCreate(BaseModel):
Explanation

Every Pydantic schema inherits from BaseModel.

This enables automatic validation and serialization.

full_name: str
Explanation

Defines the user's full name.

The value must be a string.

If another data type is provided, FastAPI automatically returns a validation error.

email: EmailStr
Explanation

Instead of using a normal string, we used EmailStr.

EmailStr validates whether the provided value follows the correct email format.

Example of a valid email:

manit@example.com

Example of an invalid email:

manit123

During development, this required installing the email-validator package because EmailStr depends on it for validation.

UserResponse Schema
Purpose

Defines the data returned to the client after successful API operations.

Important Code
class UserResponse(BaseModel):

This schema represents the API response returned after creating, updating, or retrieving a user.

id: int
full_name: str
email: EmailStr
Explanation

These fields match the information that should be returned to the client.

Notice that passwords or other sensitive fields are not included.

Schemas allow complete control over what data leaves the backend.

Important Code
model_config = ConfigDict(from_attributes=True)
Explanation

This configuration tells Pydantic that it is allowed to read values directly from SQLAlchemy model objects.

Without this configuration, FastAPI would not be able to automatically convert SQLAlchemy objects into API responses.

Earlier versions of Pydantic used:

class Config:
    orm_mode = True

In Pydantic Version 2, this was replaced by ConfigDict(from_attributes=True).

UserUpdate Schema
Purpose

Defines the data used when updating an existing user.

Unlike UserCreate, every field is optional.

Important Code
full_name: str | None = None
email: EmailStr | None = None
Explanation

The | None syntax indicates that the value can either contain data or remain empty.

This allows partial updates.

For example, the client may update only the user's name while leaving the email unchanged.

Benefits of Using Schemas

Using separate schemas provides several advantages:

Automatic request validation.
Cleaner API design.
Consistent response format.
Better Swagger documentation.
Prevents invalid data from reaching the database.
Protects sensitive information by controlling API responses.
Summary

The schemas created in this phase formed the validation layer of Atlas. They ensured that every request received by the backend was properly validated before any database operation was performed, significantly improving the reliability and maintainability of the application
6.9 app/services/user_service.py
Purpose

The user_service.py file contains the business logic of the User module.

Instead of writing database queries directly inside API endpoints, all database operations are placed inside the service layer. This keeps the routes simple and makes the code easier to reuse, test, and maintain.

This file acts as the bridge between the API layer and the database layer.

Responsibilities
Create new users.
Retrieve all users.
Retrieve a user by ID.
Update user information.
Delete users.
Communicate with the database using SQLAlchemy.
Why Do We Need a Service Layer?

Without a service layer, every API endpoint would directly contain SQLAlchemy queries.

Example:

@router.post("/")
def create_user():
    db.add(...)
    db.commit()
    db.refresh(...)

If multiple endpoints required the same database logic, the code would have to be copied repeatedly.

Instead, the route simply calls:

create_user(db, user)

This keeps API routes focused only on handling HTTP requests and responses, while the service layer manages all business logic.

Function 1 — create_user()
Purpose

Creates a new user and stores it in the PostgreSQL database.

Important Code
db_user = User(
    full_name=user.full_name,
    email=user.email
)
Explanation

Creates a SQLAlchemy User object using the data received from the API request.

At this stage, the object exists only in memory and has not yet been saved to the database.

db.add(db_user)
Explanation

Marks the object to be inserted into the database.

The record is still not permanently stored.

db.commit()
Explanation

Commits the transaction.

This permanently saves the new user into PostgreSQL.

Without commit(), the data would never be stored.

db.refresh(db_user)
Explanation

Reloads the object from the database.

This is important because PostgreSQL automatically generates values such as the Primary Key (id). After refreshing, the object contains these newly generated values.

return db_user
Explanation

Returns the newly created user object to the API route, which then sends it back to the client.

Function 2 — get_all_users()
Purpose

Returns every user stored in the database.

Important Code
return db.query(User).all()
Explanation
query(User) selects the User table.
.all() retrieves every record.
Returns a list of User objects.
Function 3 — get_user_by_id()
Purpose

Retrieves a single user using its Primary Key.

Important Code
return db.query(User).filter(User.id == user_id).first()
Explanation
Selects the User table.
Filters records where the ID matches.
Returns only the first matching record.
Returns None if no user exists.
Function 4 — update_user()
Purpose

Updates an existing user's information.

Step 1
db_user = get_user_by_id(db, user_id)
Explanation

Searches for the requested user before attempting an update.

Step 2
if not db_user:
    return None
Explanation

If the user does not exist, the function immediately returns None.

The API route later converts this into a 404 Not Found response.

Step 3
if user.full_name is not None:
    db_user.full_name = user.full_name
Explanation

Updates the user's name only if a new value has been provided.

This prevents existing values from being overwritten with empty data.

Step 4
if user.email is not None:
    db_user.email = user.email
Explanation

Updates the email only when a new email is supplied.

Step 5
db.commit()
db.refresh(db_user)
Explanation
Saves the updated information.
Reloads the latest values from PostgreSQL.
Step 6
return db_user

Returns the updated user object to the API.

Function 5 — delete_user()
Purpose

Deletes an existing user from the database.

Important Code
db_user = get_user_by_id(db, user_id)
Explanation

Checks whether the requested user exists before attempting deletion.

if not db_user:
   return None
Explanation

If the user cannot be found, the function returns None.

The API route later converts this into a 404 Not Found response.

db.delete(db_user)
Explanation

Marks the selected user for deletion.

The deletion is not permanent until the transaction is committed.

db.commit()
Explanation

Permanently removes the record from PostgreSQL.

return db_user
Explanation

Returns the deleted object, allowing the API route to send a confirmation message.

Why Is This File Important?

The Service Layer separates business logic from HTTP request handling.

Instead of mixing SQL queries with API endpoints, each responsibility is placed in its appropriate layer:

Routes → Handle HTTP requests and responses.
Services → Implement business logic.
Models → Represent database tables.
Schemas → Validate request and response data.

This separation makes the backend cleaner, easier to test, more reusable, and much easier to extend as Atlas grows into a larger application.

Summary

user_service.py became the core business logic layer of Atlas during Phase 1. Every CRUD operation passed through this file before interacting with the database, making it one of the most important components of the backend architecture.
6.10 app/api/routes/health.py
Purpose

The health.py file was created to provide a simple API endpoint that verifies whether the backend server and the PostgreSQL database are functioning correctly.

This endpoint was the very first API developed in Atlas and served as a diagnostic tool throughout Phase 1. Before implementing the User module, this endpoint was repeatedly used to confirm that the application, database connection, and SQLAlchemy configuration were working as expected.

Responsibilities
Verify that the FastAPI server is running.
Verify that PostgreSQL is connected successfully.
Display PostgreSQL version information.
Help identify configuration or database connection issues during development.
Why was it created?

Before building any CRUD operations, it was important to confirm that the backend could successfully communicate with the database.

Instead of immediately implementing complex APIs, a small health endpoint provides confidence that the backend infrastructure is functioning correctly.

This approach follows a common development practice where connectivity is tested before implementing business logic.

API Endpoint
GET /
Expected Response
{
    "app": "Atlas API",
    "database": "Connected Successfully ✅",
    "postgres_version": "PostgreSQL 16..."
}
Important Code
@router.get("/")
Explanation

This decorator registers an HTTP GET endpoint.

Whenever a client sends a GET request to the root URL (/), FastAPI executes the function immediately below the decorator.

db: Session = Depends(get_db)
Explanation

Instead of creating a database session manually, the endpoint receives one using FastAPI's Dependency Injection system.

The get_db() dependency automatically creates the session before the request begins and closes it after the request finishes.

db.execute(text("SELECT version();"))
Explanation

A simple SQL query is executed directly on PostgreSQL.

This query retrieves the PostgreSQL server version.

If the query executes successfully, it confirms that:

The database server is running.
The connection string is correct.
SQLAlchemy Engine is working.
Database sessions are working correctly.
return {
    "app": "Atlas API",
    "database": "Connected Successfully ✅",
    "postgres_version": version
}
Explanation

Returns a JSON response containing:

Application name
Database connection status
PostgreSQL version

This information is extremely useful during development because it immediately confirms whether the backend has connected successfully.

Why use a Health Check API?

Health endpoints are widely used in production systems.

They allow developers, monitoring systems, Docker containers, Kubernetes, and cloud platforms to quickly determine whether an application is healthy and ready to serve requests.

Without a health endpoint, developers would have to inspect logs or attempt database operations manually.

What did we verify using this endpoint?

During Phase 1, this endpoint helped verify:

FastAPI server startup
Successful loading of environment variables
PostgreSQL container availability
SQLAlchemy Engine configuration
Database session creation
Successful execution of SQL queries
Summary

Although this is one of the smallest files in the project, it played a critical role during Phase 1. Every major backend milestone was verified using the Health API before moving on to more advanced functionality. It served as the first confirmation that the Atlas backend and PostgreSQL database were communicating successfully and became the foundation for testing the rest of the backend architecture.
6.12 app/api/router.py
Purpose

The router.py file serves as the central routing hub for the entire Atlas backend. Instead of registering every route individually inside main.py, all route modules are combined in this file and exposed through a single router.

This approach keeps the application organized and makes it easy to add new modules in future phases without modifying the application's entry point.

Responsibilities
Create the central API router.
Register all route modules.
Organize API endpoints.
Provide a single router that is imported into main.py.
Why was it created?

As backend applications grow, the number of API endpoints increases rapidly.

If every route were registered directly inside main.py, the file would become difficult to read and maintain.

A central router solves this problem by collecting all module-specific routers into one location.

Important Code
from fastapi import APIRouter
Explanation

Imports FastAPI's APIRouter class.

APIRouter allows endpoints to be grouped into logical modules instead of placing every endpoint inside a single file.

from app.api.routes.health import router as health_router
from app.api.routes.user import router as user_router
Explanation

Imports the routers defined inside the Health and User modules.

The keyword as is used to rename each imported router, making the code easier to read and avoiding naming conflicts.

api_router = APIRouter()
Explanation

Creates the main router for the entire application.

This router acts as a container that combines all feature-specific routers.

api_router.include_router(health_router)
Explanation

Registers all endpoints defined inside the Health module.

After this statement, every endpoint inside health.py becomes accessible through the application.

api_router.include_router(user_router)
Explanation

Registers every User-related endpoint.

This includes:

Create User
Get All Users
Get User by ID
Update User
Delete User

Without this statement, FastAPI would never recognize the User API endpoints.

How Routing Works in Atlas

The request flow is as follows:

Client
   │
   ▼
main.py
   │
   ▼
api_router
   │
   ├── health_router
   │       │
   │       ▼
   │   health.py
   │
   └── user_router
           │
           ▼
       user.py

When a client sends a request, main.py forwards it to api_router, which then determines the appropriate module responsible for handling that request.

Why Use a Central Router?

Using a central router offers several advantages:

Keeps main.py clean and focused.
Makes the project modular.
Simplifies adding new modules.
Improves readability.
Reduces maintenance effort.
Follows the architecture commonly used in production FastAPI applications.

For example, when future modules such as Subjects, Notes, Finance, or Attendance are added, they only need to be imported and registered in router.py. No other part of the application needs to change.

Summary

The router.py file acts as the central navigation system of the Atlas backend. It connects all feature-specific routers into a single entry point, enabling a modular and scalable architecture. This design ensures that the backend remains organized and easy to extend as new modules are introduced in future phases.

7. Testing Performed

After completing the implementation of the backend foundation, every major component was thoroughly tested to ensure that the application behaved as expected. Testing was carried out incrementally after each major milestone rather than waiting until the end of the phase. This approach helped identify configuration issues, routing errors, database problems, and validation mistakes at an early stage.

The primary testing tool used during this phase was Swagger UI, which allowed every API endpoint to be executed directly from the browser. Database connectivity was verified using PostgreSQL, while application logs generated by Uvicorn and SQLAlchemy were used to confirm backend behavior.

7.1 Database Connection Testing
Objective

Verify that the FastAPI application could successfully establish a connection with the PostgreSQL database.

Testing Method
Started the PostgreSQL Docker container.
Started the FastAPI server using Uvicorn.
Accessed the Health API endpoint.
Verified that PostgreSQL responded successfully.
Expected Result

The API returned:

Application name
Database connection status
PostgreSQL version
Actual Result

The backend successfully connected to PostgreSQL and returned the expected response without any errors.

Status: ✅ Passed

7.2 Database Initialization Testing
Objective

Verify that database tables were created automatically during application startup.

Testing Method
Started the backend server.
Observed SQLAlchemy startup logs.
Verified that the users table was created automatically.
Expected Result

The database should contain the users table without requiring manual SQL commands.

Actual Result

SQLAlchemy successfully initialized the database and created the required tables.

Status: ✅ Passed

7.3 User Creation API Testing
Endpoint
POST /users
Objective

Verify that a new user could be inserted into the PostgreSQL database.

Test Data
{
  "full_name": "Manit Garg",
  "email": "manit@example.com"
}
Expected Result
HTTP Status Code 201 Created
User stored successfully in the database.
Generated ID returned in the response.
Actual Result

The API successfully created the user and returned the expected response.

Status: ✅ Passed

7.4 Get All Users API Testing
Endpoint
GET /users
Objective

Verify that all stored users could be retrieved successfully.

Expected Result

Return a list containing every user stored in the database.

Actual Result

The API returned the expected list of users.

Status: ✅ Passed

7.5 Get User by ID Testing
Endpoint
GET /users/{user_id}
Objective

Retrieve a single user using its unique ID.

Expected Result

Return the requested user's information.

If the user does not exist, return 404 Not Found.

Actual Result

Both scenarios worked correctly.

Existing user returned successfully.
Invalid user ID returned HTTP 404.

Status: ✅ Passed

7.6 Update User Testing
Endpoint
PUT /users/{user_id}
Objective

Verify that an existing user's information could be updated.

Expected Result

Modified information should be saved in PostgreSQL and returned in the API response.

Actual Result

The selected user's information was successfully updated.

Status: ✅ Passed

7.7 Delete User Testing
Endpoint
DELETE /users/{user_id}
Objective

Verify that an existing user could be removed from the database.

Expected Result

The record should be permanently deleted and the API should return a success message.

Actual Result

The user was successfully deleted from PostgreSQL.

Subsequent retrieval attempts correctly returned 404 Not Found.

Status: ✅ Passed

7.8 Swagger Documentation Testing
Objective

Verify that all API endpoints appeared correctly in Swagger UI.

Expected Result

Swagger should display:

Health API
User CRUD APIs
Request models
Response models
Actual Result

All endpoints appeared correctly and were fully interactive.

Every endpoint was successfully tested using Swagger UI.

Status: ✅ Passed

7.9 Validation Testing
Objective

Verify that invalid request data was rejected before reaching the database.

Tests Performed
Invalid email format.
Duplicate email address.
Non-existent User ID.
Missing required fields.
Actual Result

Pydantic and PostgreSQL correctly rejected invalid data and returned appropriate error responses.

Status: ✅ Passed

7.10 Overall Testing Summary

At the end of Phase 1, all implemented functionality was tested successfully.

Component	Status
FastAPI Server	✅ Passed
PostgreSQL Connection	✅ Passed
SQLAlchemy ORM	✅ Passed
Database Initialization	✅ Passed
User Model	✅ Passed
Create User API	✅ Passed
Get All Users API	✅ Passed
Get User by ID API	✅ Passed
Update User API	✅ Passed
Delete User API	✅ Passed
Request Validation	✅ Passed
Response Validation	✅ Passed
Swagger Documentation	✅ Passed
Conclusion

The testing performed during Phase 1 confirmed that the backend foundation of Atlas was stable, functional, and ready for future development. All major backend components—including database connectivity, ORM configuration, request validation, business logic, and CRUD operations—worked together successfully. This successful testing phase marked the completion of the backend foundation and provided a reliable base for implementing future modules in subsequent phases.

8. Concepts Learned

Phase 1 was not only about writing code but also about understanding the fundamental concepts behind modern backend development. Throughout this phase, several new technologies, design principles, and development practices were learned and applied while building Atlas. These concepts form the foundation for all future backend modules.

8.1 FastAPI Framework

During this phase, the FastAPI framework was used for the first time to build REST APIs.

Key Learnings
Creating a FastAPI application.
Defining API endpoints.
Handling HTTP requests and responses.
Automatic Swagger documentation.
Request validation using Pydantic.
Response serialization.
API routing using APIRouter.
8.2 PostgreSQL

A relational database was integrated into the project using PostgreSQL.

Key Learnings
Connecting FastAPI with PostgreSQL.
Storing application data permanently.
Creating tables.
Understanding rows and columns.
Primary Keys.
Unique Constraints.
Database indexing.
8.3 SQLAlchemy ORM

Instead of writing SQL queries manually, SQLAlchemy ORM was used.

Key Learnings
Object Relational Mapping (ORM).
Creating models.
Mapping Python classes to database tables.
Querying data using Python.
CRUD operations through SQLAlchemy.
Database sessions.
Engine configuration.
8.4 Pydantic

Pydantic introduced automatic validation of incoming API data.

Key Learnings
Creating request schemas.
Creating response schemas.
Automatic type validation.
Email validation using EmailStr.
Response serialization.
Difference between Models and Schemas.
8.5 Dependency Injection

FastAPI's Dependency Injection system was introduced for database session management.

Key Learnings
Creating reusable dependencies.
Automatic database session management.
Resource cleanup using yield.
Cleaner API routes.
Reduced code duplication.
8.6 Layered Architecture

One of the most important concepts learned during this phase was separating the backend into different layers based on responsibility.

The architecture implemented in Atlas is:

Client
   │
   ▼
API Routes
   │
   ▼
Service Layer
   │
   ▼
Database Layer
   │
   ▼
PostgreSQL
Benefits
Better organization.
Easier debugging.
Improved scalability.
Easier testing.
Code reusability.
Cleaner project structure.
8.7 Service Layer

Business logic was separated from API routes.

Key Learnings
Separation of concerns.
Reusable database operations.
Cleaner endpoint implementation.
Easier maintenance.
8.8 REST API Development

Complete CRUD APIs were implemented following REST principles.

Key Learnings
POST requests.
GET requests.
PUT requests.
DELETE requests.
URL parameters.
HTTP methods.
Resource-based routing.
8.9 HTTP Status Codes

Different HTTP status codes were encountered throughout development.

Status Codes Used
Status Code	Meaning
200	Request completed successfully
201	Resource created successfully
404	Resource not found
422	Request validation failed
500	Internal server error

Understanding these status codes made debugging API responses much easier.

8.10 Swagger UI

Swagger UI became the primary tool for testing APIs during development.

Key Learnings
Interactive API documentation.
Sending HTTP requests.
Viewing request bodies.
Viewing responses.
Testing CRUD operations.
Understanding automatically generated API documentation.
8.11 Docker

Docker was used to run PostgreSQL inside a container.

Key Learnings
Running database containers.
Managing services using Docker Compose.
Keeping the development environment consistent.
Avoiding manual PostgreSQL installation.
8.12 Version Control Using Git

Throughout Phase 1, Git was used to manage project versions.

Key Learnings
Tracking code changes.
Creating meaningful commits.
Pushing code to GitHub.
Maintaining project history.
Managing development milestones.
8.13 Project Organization

A major takeaway from Phase 1 was the importance of organizing a project before adding more features.

Instead of placing all code in a single file, the backend was divided into multiple folders based on their responsibilities.

This organization improves:

Readability.
Scalability.
Collaboration.
Maintainability.
Long-term project management.
8.14 Overall Learning Outcome

By the end of Phase 1, the following concepts had been successfully understood and implemented:

FastAPI application development.
PostgreSQL database integration.
SQLAlchemy ORM.
Database models.
Pydantic schemas.
Dependency Injection.
Service Layer architecture.
Layered backend design.
CRUD API development.
Swagger-based API testing.
Docker-based database management.
Git and GitHub workflow.

These concepts established a strong backend foundation and prepared the project for implementing larger functional modules in the upcoming phases of Atlas.

9. Interview Notes

This section contains the important concepts, design decisions, and implementation details that should be understood before discussing Phase 1 in a technical interview. Rather than memorizing code, the focus should be on explaining the reasoning behind the implementation and the technologies used.

9.1 Explain the Project Structure

One of the first questions an interviewer may ask is how the backend is organized.

The Atlas backend follows a layered architecture, where each layer has a single responsibility.

Client
   │
   ▼
API Routes
   │
   ▼
Service Layer
   │
   ▼
Database Layer
   │
   ▼
PostgreSQL

You should be able to explain how a request travels through these layers before reaching the database and how the response returns back to the client.

9.2 Difference Between Models and Schemas

This is one of the most common FastAPI interview questions.

SQLAlchemy Model
Represents a database table.
Used for database operations.
Defines columns, constraints, and relationships.
Communicates directly with PostgreSQL.
Pydantic Schema
Represents API request and response data.
Performs validation.
Ensures only valid data enters the application.
Controls what information is returned to the client.

Although both may contain similar fields, their responsibilities are completely different.

9.3 Why Did You Use FastAPI?

FastAPI was selected because it provides:

High performance.
Automatic Swagger documentation.
Built-in request validation.
Type hint support.
Modern asynchronous capabilities.
Clean and readable code structure.

These features make backend development faster while reducing boilerplate code.

9.4 Why PostgreSQL Instead of SQLite?

PostgreSQL was chosen because it is a production-grade relational database.

Compared to SQLite, PostgreSQL provides:

Better scalability.
Improved concurrency.
Advanced indexing.
Strong data integrity.
Better support for large applications.

Since Atlas is intended to grow into a complete Student Operating System, PostgreSQL was a more suitable choice.

9.5 Why SQLAlchemy ORM?

SQLAlchemy was used to simplify database interaction.

Instead of writing raw SQL queries, developers interact with the database using Python classes and objects.

Advantages include:

Cleaner code.
Database abstraction.
Easier maintenance.
Improved readability.
Better integration with FastAPI.
9.6 Why Dependency Injection?

Dependency Injection was used to manage database sessions automatically.

Without it, every API endpoint would need to manually create and close database sessions.

Using Depends(get_db) ensures:

Automatic session management.
Cleaner endpoints.
Reduced code duplication.
Better resource management.
9.7 Why Create a Service Layer?

The Service Layer separates business logic from API routes.

API routes should only:

Receive requests.
Validate input.
Call services.
Return responses.

The Service Layer handles:

Database operations.
Business rules.
Data processing.

This separation improves maintainability and scalability.

9.8 Explain CRUD Operations

CRUD stands for:

Create – Insert new data into the database.
Read – Retrieve existing data.
Update – Modify existing data.
Delete – Remove existing data.

During Phase 1, complete CRUD functionality was implemented for the User module and successfully tested using Swagger UI.

9.9 Explain the Purpose of APIRouter

APIRouter helps organize API endpoints into separate modules.

Instead of placing every endpoint inside main.py, each module manages its own routes.

Benefits include:

Better organization.
Easier maintenance.
Improved scalability.
Cleaner project structure.
9.10 Explain Swagger UI

Swagger UI is automatically generated by FastAPI.

It provides:

Interactive API documentation.
API testing directly from the browser.
Automatic request and response examples.
Faster debugging during development.

Throughout Phase 1, Swagger UI was the primary tool used for testing all CRUD APIs.

9.11 Explain the Overall Request Flow

You should be able to describe what happens when a client sends a request to the backend.

Example:

The client sends an HTTP request.
FastAPI receives the request.
The appropriate API route is selected.
Request data is validated using Pydantic.
A database session is provided through Dependency Injection.
The Service Layer performs the required business logic.
SQLAlchemy communicates with PostgreSQL.
The result is returned to the API route.
FastAPI converts the response into JSON.
The client receives the final response.

This demonstrates a complete understanding of how the backend processes requests.

9.12 Key Takeaways for Interviews

After completing Phase 1, the following topics should be comfortably explainable without referring to the code:

FastAPI fundamentals.
Backend project structure.
PostgreSQL integration.
SQLAlchemy ORM.
Pydantic validation.
Models vs Schemas.
Dependency Injection.
Service Layer architecture.
CRUD operations.
APIRouter.
Swagger UI.
Dockerized database setup.
Complete request lifecycle.
Overall backend architecture of Atlas.

Being able to explain these concepts clearly demonstrates not only that the project was built successfully, but also that the underlying design decisions and implementation approach are well understood.

10. Phase Summary

Phase 1 marked the transition of Atlas from a basic project setup into a functional backend application. A clean, modular, and scalable architecture was established using FastAPI, PostgreSQL, SQLAlchemy, and Pydantic. Complete CRUD functionality for the User module was implemented, tested, and documented, providing a strong foundation for all future development.

With the successful completion of this phase, Atlas now possesses a production-inspired backend structure capable of supporting larger modules such as Academic Management, Finance Tracking, Dashboard, and AI-powered features. The concepts learned, architecture adopted, and implementation completed during this phase will serve as the foundation for every subsequent phase of the project.