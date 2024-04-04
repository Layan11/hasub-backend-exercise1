from fastapi import APIRouter, HTTPException, Request
from models.student_model import student_model
import utils.db_funcs as db_fns
import utils.auth_funcs as auth_fns

router = APIRouter()


@router.get('/students/')
def get_all_students(request: Request):
    if auth_fns.check_token(request):
        students_json = db_fns.load_db()
        return students_json
    else:
        raise HTTPException(400, "no token")


@router.get('/student/{student_id}')
def get_student(student_id, request: Request):
    if auth_fns.check_token(request):
        students = db_fns.load_db()

        for student in students["Students"]:
            if student["id"] == student_id:
                return student["name"]
        return "student not found"
    else:
        raise HTTPException(400, "no token")


@router.get('/student_by_class/{class_name}')
def get_student_by_class(class_name, request: Request):
    if not auth_fns.check_token(request):
        raise HTTPException(400, "no token")
    elif not auth_fns.check_admin(request):
        raise HTTPException(400, "access denied, only admin is allowed")
    else:
        students = db_fns.load_db()
        class_students = []
        for student in students["Students"]:
            if class_name in student["classes"]:
                class_students.append(student["name"])
        if len(class_students) == 0:
            return "No students in this class"
        return class_students


@router.post('/add_student/')
def add_student(Student: student_model, request: Request):
    if not auth_fns.check_token(request):
        raise HTTPException(400, "no token")
    elif not auth_fns.check_admin(request):
        raise HTTPException(400, "access denied, only admin is allowed")
    else:
        students = db_fns.load_db()
        for student in students["Students"]:
            if student["id"] == Student.id:
                return "Student already exists in db"
        db_fns.wrtie_to_db(Student)
        return "Student added successfully"
