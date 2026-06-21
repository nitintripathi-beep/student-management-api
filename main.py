from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

students_db = {
    1: {"name": "Rahul", "age": 20, "city": "Delhi"},
    2: {"name": "Priya", "age": 22, "city": "Mumbai"},
    3: {"name": "Aman", "age": 21, "city": "Lucknow"}
}

class Student(BaseModel):
    name : str
    age : int
    city : str

@app.get("/students")    
def get_students():
    return students_db

@app.get("/students/{id}")
def student_id(id: int):
    if id not in students_db:
        raise HTTPException(status_code=404 , detail="Student not found")
    return students_db[id]

@app.post("/students")
def add_student(student: Student):
    new_id = len(students_db) + 1
    students_db[new_id] = student.dict()
    return {"message":"Student added!", "id" : new_id}  

@app.put("/students/{id}")
def update_students(id : int , student : Student):
    if id not in students_db:
        raise HTTPException(status_code=404 , detail="Student not found")
    students_db[id] = student.dict()
    return {"message" : f"Student {id} updated" , "updated data": student}

@app.delete("/students/{id}")
def delete_student(id : int):
    if id not in students_db:
        raise HTTPException(status_code=404 , detail="Student not found")
    del students_db[id] 
    return {"message": f"Student {id} deleted"}
