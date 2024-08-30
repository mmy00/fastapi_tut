from fastapi import FastAPI
from pydantic import BaseModel
# انشاء تطبيق FastAPI
app = FastAPI()
# عشان الكود يشتغل في اي حتة
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # ده لازم يتقفل في النهاية
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )
# pydantic تعريف نموذج باستخدام
class Student(BaseModel):
    id:int
    name:str
    grade:int
# list قائمة لتخرين بيانات الطلبة
students = [
     Student(id=1,name="Karim",grade=5),
     Student(id=2,name="Kadija",grade=3)
     ]
#قراءة جميع العناصر
@app.get("/students/")
def read_students():
    return students
# post انشاء عنصر جديد باستخدام
@app.post("/students/")
def create_student(new_student:Student):
    students.append(new_student)
    return new_student
# put تحديث بيانات عنصر باستخدام
@app.put("/students/{student_id}")
def update_student(student_id:int,updated_student:Student):
    for index,student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {"error" : "student not found"}
# put حذف بيانات عنصر باستخدام
@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for index,student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {"message" : "student deleted"}
    return {"error" : "student not found"}
