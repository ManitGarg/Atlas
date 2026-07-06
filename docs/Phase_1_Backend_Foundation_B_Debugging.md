1. Debugging Overview

Debugging was an integral part of Phase 1 and played a significant role in the successful completion of the backend foundation. While implementing the FastAPI backend, several issues were encountered related to project configuration, package dependencies, database connectivity, routing, schema validation, and CRUD operations. Each issue required careful investigation to identify its root cause before an appropriate solution could be applied.

Rather than treating debugging as a separate activity, it became a continuous part of the development process. Every error helped improve the understanding of FastAPI, SQLAlchemy, Pydantic, PostgreSQL, and the overall backend architecture. Instead of immediately searching for fixes, effort was made to understand why each error occurred, how it affected the application, and what changes were required to resolve it correctly.

This document records every significant debugging session encountered during Phase 1 in chronological order. For each issue, the original error, its root cause, the investigation process, the implemented solution, and the lessons learned have been documented. Maintaining this debugging journal serves two important purposes: it provides a reference for future development and demonstrates the practical problem-solving process followed during the implementation of Atlas.

By the end of Phase 1, all identified issues were successfully resolved, resulting in a stable backend foundation with fully functional CRUD operations, proper database integration, and a clean project architecture. The experience gained through these debugging sessions significantly strengthened the understanding of backend development and established better practices that will be followed in future phases of the project.

2. Debugging Case 1 – Missing email-validator Package
Problem

While starting the FastAPI application after implementing the User schemas, the server failed to start and terminated immediately with an import-related error.

Error Message
ModuleNotFoundError: No module named 'email_validator'

ImportError: email-validator is not installed,
run `pip install 'pydantic[email]'`
When Did It Occur?

This issue occurred during Phase 1.3 after introducing the EmailStr data type inside the UserCreate and UserResponse Pydantic schemas.

The backend had previously been running correctly until email validation was added.

Root Cause

The project used Pydantic's EmailStr type for validating email addresses.

Although EmailStr is provided by Pydantic, it internally depends on an external package called email-validator.

Since this package had not been installed, Pydantic was unable to perform email validation, causing the application startup to fail.

Investigation

The complete error traceback was examined carefully.

The final lines of the traceback clearly indicated:

ImportError:
email-validator is not installed

The error message also suggested the required package to install, confirming that the issue was caused by a missing dependency rather than an error in the application code.

Solution

The missing package was installed using pip.

pip install email-validator

After installation, the project dependencies were updated.

pip freeze > requirements.txt

This ensured that anyone setting up the project in the future would automatically install the required package.

Verification

After installing the package:

FastAPI started successfully.
Pydantic loaded the schemas correctly.
Email validation worked as expected.
Swagger UI opened without errors.

The issue was completely resolved.

Lesson Learned

Some features provided by frameworks depend on additional third-party packages that are not installed automatically.

Before using advanced validation types such as EmailStr, it is important to verify whether they require external dependencies.

Updating the requirements.txt file after installing new packages is also essential to ensure that the project remains reproducible on other systems.

Prevention

To avoid similar issues in future development:

Carefully read the documentation of new libraries and data types before using them.
Install all required dependencies immediately after introducing a new feature.
Update requirements.txt whenever new packages are added.
Test the application after every dependency installation to identify issues early in the development process.

3. Debugging Case 2 – api_router Import Error
Problem

After implementing the User CRUD module, the FastAPI server failed to start because it could not import the central API router.

Error Message
ImportError: cannot import name 'api_router'
from 'app.api.router'
When Did It Occur?

This issue occurred during Phase 1.3 after creating the routing structure for the User module and attempting to start the application using Uvicorn.

Root Cause

The main.py file expected an object named api_router.

from app.api.router import api_router

However, the router.py file only contained a router named:

router = APIRouter(...)

Since the object api_router did not exist, Python raised an ImportError during application startup.

Investigation

The complete traceback was analyzed, and the last few lines clearly pointed towards the router.py file.

After comparing main.py and router.py, it became clear that the imported variable name and the actual variable name were different.

This was not a FastAPI issue but simply a naming mismatch.

Solution

The routing file was updated by creating the correct central router.

api_router = APIRouter()

All module routers were then registered using:

api_router.include_router(...)

Finally, main.py successfully imported:

from app.api.router import api_router

without any errors.

Verification

After correcting the router name:

FastAPI started successfully.
No ImportError was generated.
Swagger UI loaded correctly.
All registered endpoints became visible.

The issue was completely resolved.

Lesson Learned

Whenever a module imports an object from another file, the imported name must exactly match the object defined in that file.

Even a small naming inconsistency can prevent the entire application from starting.

Maintaining consistent naming conventions across files significantly reduces import-related errors.

Prevention

To avoid similar issues in future development:

Use meaningful and consistent variable names.
Verify imports immediately after creating new files.
Ensure exported objects and imported objects have identical names.
Test the application after every structural change instead of making multiple changes before running the server.

4. Debugging Case 3 – user_router Not Defined
Problem

After fixing the api_router import issue, the application still failed to start. This time, FastAPI reported that user_router was not defined while registering routes in the central router.

Error Message
NameError: name 'user_router' is not defined.
Did you mean: 'api_router'?
When Did It Occur?

This issue occurred during Phase 1.3 while integrating the User module into the central routing system.

Root Cause

The router.py file attempted to register the User router using:

api_router.include_router(user_router)

However, the user_router object had never been imported into the file.

Since Python executes code from top to bottom, it encountered user_router before knowing what it referred to, resulting in a NameError.

Investigation

The error traceback pointed directly to the following line inside router.py:

api_router.include_router(user_router)

On reviewing the file, it was found that only APIRouter had been imported, while the User router itself was missing.

The required import statement had not been added.

Solution

The missing import statement was added at the beginning of the file.

from app.api.routes.user import router as user_router

The Health router was also imported in the same manner.

from app.api.routes.health import router as health_router

After importing both routers, they were successfully registered.

api_router.include_router(health_router)
api_router.include_router(user_router)
Verification

After saving the file and restarting the backend:

The application started successfully.
No NameError was generated.
Swagger UI displayed both the Health and User endpoints.
All API routes became accessible.

The issue was completely resolved.

Lesson Learned

Before using any object inside a Python file, it must first be imported.

A missing import statement can completely stop the application, even if the remaining code is correct.

When encountering a NameError, the first step should always be to verify whether the required object has been imported properly.

Prevention

To avoid similar issues in future development:

Import every required module before using it.
Verify imports after creating new files.
Read the complete traceback carefully, as it usually identifies the exact line causing the error.
Test the application after adding each new router instead of registering multiple routers at once.

5. Debugging Case 4 – Incorrect router.py Structure
Problem

After fixing the import-related issues, the backend still failed to work correctly. The problem was no longer related to missing imports but to the overall structure of the router.py file.

Error Description

The application either failed to start correctly or the expected API endpoints did not appear in Swagger UI.

Further investigation revealed that the router.py file contained incorrect code and did not follow the intended routing architecture.

When Did It Occur?

This issue occurred during Phase 1.3 while integrating the User CRUD module into the backend.

Root Cause

The router.py file was mistakenly written as if it were a route file.

Instead of acting as the central router, it contained endpoint-related code.

As a result:

The routing architecture became inconsistent.
main.py could not properly register application routes.
The project no longer followed the intended layered structure.
Investigation

The contents of router.py were reviewed and compared with the intended project architecture.

It became clear that the file had two responsibilities mixed together:

Registering routes.
Defining API endpoints.

These responsibilities should always remain separate.

The correct architecture should be:

main.py
      │
      ▼
api/router.py
      │
      ├── health.py
      └── user.py

Instead, endpoint logic had accidentally been placed inside the central router file.

Solution

The router.py file was rewritten completely.

Its responsibility was reduced to only:

Creating the central APIRouter
Importing feature-specific routers
Registering those routers using include_router()

The API endpoint implementations remained inside their respective files:

health.py
user.py

This restored the intended project architecture.

Verification

After restructuring the routing system:

FastAPI started successfully.
Swagger UI displayed all endpoints.
The User module became accessible.
Route registration worked correctly.
The backend architecture matched the planned design.

The issue was fully resolved.

Lesson Learned

Every file should have one clearly defined responsibility.

The central router should only register route modules.

API endpoint implementations should remain inside their own route files.

Mixing responsibilities increases complexity and makes debugging much more difficult.

Prevention

To avoid similar issues in future development:

Follow the planned folder structure before writing code.
Ensure every file has a single responsibility.
Review the architecture whenever creating new modules.
Compare the implementation with the intended project structure before testing the application.

6. Debugging Case 5 – Pydantic Version Compatibility Issue
Problem

After implementing the Pydantic schemas, the application produced configuration-related issues because the project was using Pydantic Version 2, while some of the implementation followed the syntax used in Pydantic Version 1.

When Did It Occur?

This issue occurred during Phase 1.3 while implementing the response schemas for the User module.

Root Cause

Many FastAPI tutorials and older documentation still use the following configuration:

class Config:
    orm_mode = True

However, the project was using Pydantic Version 2, where this configuration has been replaced.

Using the older configuration can lead to compatibility problems and warnings.

Investigation

The installed package versions were checked, and it was confirmed that the project was using Pydantic V2.

The official Pydantic documentation was reviewed, which showed that the configuration syntax had changed in the newer version.

This confirmed that the issue was caused by version differences rather than incorrect application logic.

Solution

The old configuration:

class Config:
    orm_mode = True

was replaced with the Pydantic V2 configuration:

model_config = ConfigDict(from_attributes=True)

This configuration allows Pydantic to read data directly from SQLAlchemy model objects when generating API responses.

Verification

After updating the schema configuration:

The application started successfully.
Response models worked correctly.
SQLAlchemy model objects were converted into API responses without issues.
Swagger UI displayed the expected response structure.

The compatibility issue was completely resolved.

Lesson Learned

Frameworks evolve over time, and code written for older versions may not work correctly with newer releases.

Before following tutorials or documentation, it is important to verify the version of the library being used and refer to its corresponding official documentation.

Prevention

To avoid similar issues in future development:

Always check the installed library version before implementing code from external resources.
Prefer official documentation over outdated tutorials.
Read migration guides when upgrading major library versions.
Keep project dependencies documented in requirements.txt to ensure consistent versions across different development environments.

7. Debugging Case 6 – Duplicate Email Constraint Violation
Problem

While testing the Create User API, the first request successfully inserted a user into the database. However, sending another request with the same email address resulted in an error instead of creating another user.

Initially, this appeared to be a bug in the CRUD implementation.

Error Message
duplicate key value violates unique constraint
"ix_users_email"

DETAIL:
Key (email)=(manit@example.com) already exists.
When Did It Occur?

This issue occurred during Phase 1.3 while testing the POST /users endpoint using Swagger UI.

The API worked correctly for the first request but failed when attempting to create another user with the same email address.

Root Cause

The email column in the User model was defined as:

email = Column(
    String,
    unique=True,
    index=True,
    nullable=False
)

The unique=True constraint instructs PostgreSQL that every email address must be unique.

When another record with the same email was inserted, PostgreSQL correctly rejected the operation to preserve data integrity.

Therefore, the issue was not caused by FastAPI or SQLAlchemy—the database was behaving exactly as intended.

Investigation

The Uvicorn logs were carefully examined.

Initially, it appeared that the API had failed to create the user.

However, the server logs revealed that:

The first POST request returned HTTP 201 (Created).
The second POST request attempted to insert the same email again.
PostgreSQL rejected the second request because of the unique constraint.

This confirmed that the CRUD implementation was functioning correctly.

Solution

Instead of using the same email address repeatedly, a different email was provided for subsequent test requests.

Example:

{
    "full_name": "Atlas Test",
    "email": "atlas@test.com"
}

The new request completed successfully, confirming that the API behaved correctly.

Verification

After using a unique email address:

User creation succeeded.
PostgreSQL stored the new record.
Swagger returned HTTP 201 Created.
The user appeared in the GET /users response.

The issue was completely resolved.

Lesson Learned

Database constraints are an essential part of application design.

A Unique Constraint prevents duplicate records and helps maintain data consistency.

Not every error returned by the database indicates a bug in the application. Sometimes, the database is correctly enforcing the rules defined by the developer.

Understanding the difference between an application error and a database validation error is an important skill in backend development.

Prevention

To avoid similar situations in future development:

Use different test data while testing Create APIs.
Read the complete database error message before assuming there is a bug.
Understand the constraints defined in database models.
Consider handling duplicate record exceptions gracefully by returning meaningful API responses instead of exposing raw database errors.

8. Debugging Case 7 – DELETE Endpoint Testing Confusion
Problem

While testing the DELETE User API, the endpoint did not return the expected success message. Instead, the response appeared incorrect, leading to the assumption that the Delete API was not functioning properly.

Observed Behavior

Initially, the request was sent without specifying the required user_id path parameter.

As a result, the endpoint did not execute as expected, creating confusion about whether the DELETE API had been implemented correctly.

Later, after providing an ID, another request returned:

404 Not Found

which again appeared to indicate that the Delete API was broken.

When Did It Occur?

This issue occurred during Phase 1.3 while testing the User CRUD APIs using Swagger UI.

Root Cause

The issue was not caused by the backend implementation.

There were actually two separate testing mistakes:

1. Missing Path Parameter

The DELETE request was initially executed without providing the required user_id.

Instead of sending:

DELETE /users/1

the request was effectively sent without a valid user ID.

2. Incorrect User ID

Later, the request used an ID that had already been deleted.

Since PostgreSQL no longer contained that record, the backend correctly returned:

404 User not found

The API was working correctly.

The problem was the test data being used.

Investigation

The following steps were performed:

Verified the request URL.
Checked the current users using GET /users.
Confirmed that User ID 1 had already been deleted.
Observed that PostgreSQL had assigned the next created user the ID 3 instead of reusing ID 1.

This confirmed that the backend logic was functioning correctly.

Solution

The API was tested again using the correct user ID returned by:

GET /users

Example:

DELETE /users/3

The API then returned:

{
    "message": "User deleted successfully"
}

A follow-up request to:

GET /users

returned:

[]

confirming that the deletion had completed successfully.

Verification

After testing with the correct user ID:

DELETE endpoint worked successfully.
Record was removed from PostgreSQL.
Success message was returned.
GET request confirmed that the user no longer existed.

The issue was completely resolved.

Lesson Learned

Before assuming an API is faulty, always verify the data currently stored in the database.

When testing Update or Delete operations, confirm that:

The requested record actually exists.
The correct ID is being used.
The request URL contains all required path parameters.

Many API testing issues are caused by incorrect test data rather than errors in the backend implementation.

Prevention

To avoid similar issues in future development:

Always check the available records using GET before performing PUT or DELETE operations.
Verify that the correct path parameters are supplied in Swagger UI.
Read HTTP status codes carefully before assuming an implementation error.
Test CRUD operations sequentially (Create → Read → Update → Delete) to maintain consistent test data.

9. Debugging Case 8 – PostgreSQL Auto-Increment ID Confusion
Problem

After successfully deleting a user from the database, a new user was created for further testing. It was expected that PostgreSQL would assign the new user the same ID that had just been deleted.

However, the newly created user received a different ID, creating the impression that the database was behaving incorrectly.

Observed Behavior

Example:

Initial database:

ID	Name
1	Manit Garg

After deleting the record:

Database

(No Records)

After creating a new user:

ID	Name
3	Manit Garg

Instead of generating ID = 1, PostgreSQL generated ID = 3.

When Did It Occur?

This issue occurred during Phase 1.3 while repeatedly testing the User CRUD APIs.

After deleting users and creating new ones multiple times, the generated IDs continued increasing.

Root Cause

The behavior was caused by PostgreSQL's Auto-Increment Sequence.

Primary Keys generated using sequences are designed to produce unique values, not consecutive values.

When a row is deleted, PostgreSQL does not reuse previously assigned IDs.

Instead, it continues generating the next available sequence number.

This is normal and expected behavior.

Investigation

To verify whether this was a bug:

The existing users were checked using:
GET /users
A new user was created.
The returned ID was compared with previous IDs.

It was observed that every new record received a higher ID, regardless of whether earlier records had been deleted.

This confirmed that the sequence generator was functioning correctly.

Solution

No code changes were required.

The CRUD implementation was already correct.

Testing continued using the IDs returned by the API instead of assuming that deleted IDs would be reused.

Verification

After understanding PostgreSQL's sequence behavior:

User creation worked correctly.
GET requests returned the correct IDs.
Update operations worked using the generated IDs.
Delete operations also worked correctly.

The issue was identified as expected database behavior rather than an implementation error.

Lesson Learned

Auto-increment values are designed to guarantee uniqueness, not continuous numbering.

Deleted IDs are normally not reused because doing so could create conflicts with logs, foreign keys, backups, and audit records.

This behavior is common across most production database systems.

Prevention

To avoid similar confusion in future development:

Never assume that newly created records will reuse deleted IDs.
Always use the ID returned by the API response.
Verify record IDs using GET requests before performing Update or Delete operations.
Understand how database sequences work before debugging Primary Key-related issues.

10. Debugging Case 9 – CRUD Verification and End-to-End Testing
Problem

After resolving all configuration, routing, dependency, and database-related issues, it was necessary to verify that every component of the backend worked together correctly.

Although individual files appeared to function properly, there was still a possibility that the complete request flow could fail due to integration issues between different layers of the application.

Objective

The objective of this debugging session was to verify the complete backend workflow by testing every CRUD operation sequentially.

Instead of testing individual files, the entire request lifecycle—from the client to the database and back—was validated.

Testing Sequence

The following order was followed:

Step 1 — Create User
POST /users

Expected Result:

User stored in PostgreSQL.
HTTP Status Code 201 Created.
Generated ID returned.

Result: ✅ Passed

Step 2 — Get All Users
GET /users

Expected Result:

Return all stored users.

Result: ✅ Passed

Step 3 — Get User by ID
GET /users/{user_id}

Expected Result:

Return the requested user.
Return 404 for invalid IDs.

Result: ✅ Passed

Step 4 — Update User
PUT /users/{user_id}

Expected Result:

Update the selected user's information.
Return updated data.

Result: ✅ Passed

Step 5 — Delete User
DELETE /users/{user_id}

Expected Result:

Remove the selected user.
Return a success message.

Result: ✅ Passed

Step 6 — Verify Deletion
GET /users

Expected Result:

[]

The database should contain no records after deleting the only user.

Result: ✅ Passed

Investigation

During this final testing phase, every layer of the backend participated in processing requests.

The request flow was successfully verified:

Client
   │
   ▼
Swagger UI
   │
   ▼
FastAPI Route
   │
   ▼
Pydantic Validation
   │
   ▼
Dependency Injection
   │
   ▼
Service Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL
   │
   ▼
Response

Each layer communicated correctly with the next, confirming that the overall backend architecture was functioning as intended.

Outcome

All CRUD operations completed successfully without any remaining issues.

The backend successfully demonstrated:

Database connectivity.
Request validation.
Business logic execution.
Database transactions.
Response serialization.
Error handling.

This confirmed that the backend foundation of Atlas was stable and ready for future feature development.

Lesson Learned

Individual files working correctly does not necessarily guarantee that the complete application works.

A final end-to-end integration test is essential before considering a development phase complete.

Testing the entire request lifecycle provides confidence that all application layers are properly connected and functioning together.

Prevention

For future phases of Atlas:

Perform integration testing after completing every major module.
Test all CRUD operations sequentially.
Verify both successful and failure scenarios.
Confirm database changes after every API operation.
Only mark a phase as complete after successful end-to-end verification.
11. Final Lessons Learned

Phase 1 was the first complete backend development phase of Atlas and provided valuable practical experience beyond simply writing code. Most issues encountered were not caused by complex algorithms but by configuration mistakes, dependency management, project structure, routing, and understanding how different backend components interact.

The most important lesson learned was that debugging is a structured process rather than trial and error. Reading complete error messages, identifying the root cause, verifying assumptions, and testing solutions systematically proved to be far more effective than making random code changes.

Another major takeaway was the importance of following a clean project architecture from the beginning. Separating responsibilities into Models, Schemas, Services, Routes, and Database components made the project easier to understand, debug, and extend.

Phase 1 also reinforced several development best practices:

Read the complete error message before attempting a fix.
Understand the root cause instead of only fixing the symptom.
Test every feature immediately after implementation.
Commit changes only after successful testing.
Follow a modular architecture with clearly defined responsibilities.
Keep project dependencies updated and documented.
Validate every API using Swagger before moving to the next task.

By documenting every debugging session, future development becomes easier because similar problems can be identified and resolved much more quickly. This debugging journal also serves as a record of the learning process throughout the development of Atlas.

With all identified issues successfully resolved and every CRUD operation verified, Phase 1 concluded with a stable, well-structured backend foundation ready for the implementation of larger functional modules in the upcoming phases.