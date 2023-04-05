from pydantic import BaseModel
from datetime import datetime

class Employee_Details(BaseModel):
    company_id: int
    employee_id: int
    employee_name: str
    in_time: datetime
    out_time: datetime

    class Config:
        orm_mode = True


# class Response(Employee_Details):
#     # company_id: int
#     # employee_id: int
#     # year: int
#     employee_name: str
#     january: int
#     february: int
#     march: int
#     april: int
#     may: int
#     june: int
#     july: int
#     august: int
#     september: int
#     october: int
#     november: int
#     december: int
#
#     class Config:
#         orm_mode = True