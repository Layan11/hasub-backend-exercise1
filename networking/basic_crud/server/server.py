from fastapi import FastAPI, Request
from routes import students

app = FastAPI()

# # routes
app.include_router(students.router)

