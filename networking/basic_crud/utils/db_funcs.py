import json
from models.student_model import student_model


def load_db(db='students_db.json'):
    with open(f'C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/networking/basic_crud/data/{db}') as f:
        students_json = f.read()
        students_json =json.loads(students_json)
        return students_json


def update_db(updated_db, db='students_db.json'):
    with open(f'C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/networking/basic_crud/data/{db}', 'w') as f:
        f.write(json.dumps(updated_db))
        f.close()


def wrtie_to_db(new_student, db='students_db.json'):
    with open(f'C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/networking/basic_crud/data/{db}', 'r') as f:
        students_json = f.read()
        students_json =json.loads(students_json)
        students = students_json["Students"]

        students.append(
            {"name": new_student.name, "id": new_student.id, "age": new_student.age, "classes": new_student.classes})

    with open(f'C:/Users/Layan/PycharmProjects/hasub-backend-exercise1/networking/basic_crud/data/{db}', 'w') as f:
        json.dump({"Students": [student for student in students]}, f, indent=3)

        return True


def find_user(username):
    db = load_db("auth_db.json")
    if username in db:
        return db[username]
    else:
        raise FileNotFoundError(f'username: {username} not in db')

# student = {"name": "newstudent", "id": "123", "age": 12, "classes": ['math']}
# s = student_model(**student)
# wrtie_to_db(s)