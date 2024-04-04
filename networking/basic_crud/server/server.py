from fastapi import FastAPI, Request
from routes import students, auth_router

app = FastAPI()

# # routes
app.include_router(students.router)
app.include_router(auth_router.router)

