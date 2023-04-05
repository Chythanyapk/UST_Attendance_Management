from database import Base
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, DateTime
from datetime import datetime

class AttendanceReport(Base):
    __tablename__ = 'attendance_sheet'

    #id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer)
    employee_id = Column(Integer)
    employee_name = Column(String, nullable=False)
    year = Column(Integer)
    january = Column(Integer)
    february = Column(Integer)
    march = Column(Integer)
    april = Column(Integer)
    may = Column(Integer)
    june = Column(Integer)
    july = Column(Integer)
    august = Column(Integer)
    september = Column(Integer)
    october = Column(Integer)
    november = Column(Integer)
    december = Column(Integer)
    __table_args__ = (
        PrimaryKeyConstraint('employee_id', 'year'),
    )


class AttendanceData(Base):
    __tablename__ = 'attendance_data'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    employee_id = Column(Integer)
    employee_name = Column(String, nullable=False)
    in_time = Column(DateTime)
    out_time = Column(DateTime)

    # __table_args__ = (
    #      PrimaryKeyConstraint('employee_id', 'company_id'),
    # )