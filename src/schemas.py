from pydantic import BaseModel


class Employee_Details(BaseModel):
    company_id: int
    employee_id: int
    year: int
    # rating: Optional[int]=None


class Response(Employee_Details):
    # company_id: int
    # employee_id: int
    # year: int
    employee_name: str
    january: int
    february: int
    march: int
    april: int
    may: int
    june: int
    july: int
    august: int
    september: int
    october: int
    november: int
    december: int

    class Config:
        orm_mode = True