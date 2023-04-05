from fastapi import FastAPI,Response, status, HTTPException, UploadFile,File,Depends, Request, Form
from process1 import data_filter,read_data
from processing import workcall 
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy.orm import Session
import models
import schemas
from fastapi.encoders import jsonable_encoder
from typing import List
from database import engine,get_db,SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import asyncio

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def process_file(file: UploadFile):
    df = read_data(file)
    df = df.dropna(inplace=False)
    employee_attendance = df.groupby(['company_id', 'employee_id']).apply(
        lambda x: x[['company_id', 'employee_id', 'employee_name', 'in_time', 'out_time']].values.tolist())
    with ThreadPoolExecutor(max_workers=4) as executor:
         executor.map(data_filter, employee_attendance.items())


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    process_file(file)
    await asyncio.sleep(5)
    workcall()
    response = JSONResponse(content={"filename": file.filename, "status": "uploaded successfully"})
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response





@app.get('/record/viewattendance/{employee_id}/{company_id}/{year}', status_code=status.HTTP_302_FOUND, response_model=schemas.Response)
def get_record(employee_id: int, company_id: int, year: int, db: Session = Depends(get_db)):
    record = db.query(models.AttendanceReport).filter(models.AttendanceReport.employee_id == employee_id, models.AttendanceReport.company_id == company_id, models.AttendanceReport.year == year).first()
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
    return record
    # record_dict = record._dict_
    # record_dict.pop('_sa_instance_state')
    # record_dict['company_id'] = company_id
    # record_dict['year'] = year
    # headers = {
    #     "Access-Control-Allow-Origin": "*"
    # }

    # return JSONResponse(content=record_dict, headers=headers)

    #return record_dict