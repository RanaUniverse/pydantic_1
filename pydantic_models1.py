from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr


class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"


class Employee(BaseModel):

    employee_id: UUID = uuid4()
    name: str
    email: EmailStr
    date_of_birth: date
    salary: float
    department: Department
    elected_benefits: bool


e1 = Employee(
    name="Chris DeTuma",
    email="cdetuma@example.com",
    date_of_birth="1998-04-02",
    salary=123_000.00,
    department="IT",
    elected_benefits=True,
)

print(e1)

e2 = Employee(
    name="Rana Universe",
    email="ranauniverse321@gmail.com",
    date_of_birth=date(2000, 1, 1),
    salary=2000,
    department=Department.ENGINEERING,
    elected_benefits=True,
)
print(e2)
