from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name:str
    age:int

students=[]
@app.get('/students')
def get_students():
    return students

@app.get('/student/{student_id}')
def get_student(student_id: int):
    return students[student_id]

@app.post('/students')
def create_student(student:Student):
    students.append(student)
    return student

@app.put('/students/{student_id}')
def update_student(student_id: int, student: Student):
    students[student_id]= student
    return student

@app.delete('/students/{student_id}'):
def delete_student(student_id: int):
    students.pop(student_id)
    return {'message':'Student deleted'}