from fastapi import FastAPI

app = FastAPI(
    title="Atlas API",
    description="Backend API for Atlas - Personal Student Operating System",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Atlas API 🚀",
        "status": "Backend is running successfully!"
    }