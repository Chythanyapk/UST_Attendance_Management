# Employee Attendandance Management System
Welcome aboard fellow developer, This is a python-based system for managing employee attendance using FastAPI framework and PostgreSQL database.The system consist of two APIs, one for uploading data file and another for searching attendance data.
# Installation
1.Clone the repository
```bash
git clone https://github.com/username/repo-name.git
```
2.Install the dependencies

```bash 
pip install -r requirements.txt
```
3.Create a PostgreSQL database and update the credentials in the `.env` file:
  
  ```bash
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=''
DATABASE_NAME=Employee_Attendance
DATABASE_USERNAME=postgres
```

Add .env file path in config.py file

3.Start the Application

Upload Datafile

```bash
uvicorn app1:app --reload
```

View Attendance Details
```bash
uvicorn app:app --reload
```






#### Dataset: Attendance_Datasheet.csv
`` Columns: company_id,employee_id,employee_name,in_time,out_time``

## API Reference

#### Upload File



  Method:POST

```http://127.0.0.1:8000/uploadfile/
http://127.0.0.1:8000/uploadfile/
```

| Request | Request body     | Response               |
| :-------- | :------- | :------------------------- |
| `multipart/formdata` |**Required**. File  |{"filename": "Employee_Attendance_Datasheet.csv", "status": "uploaded succesfully"}                   |

#### Get data

Method: GET

```http://127.0.0.1:8000/viewattendance/{employee_id}/{company_id},{year}
http://127.0.0.1:8000/viewattendance/{employee_id}/{company_id},{year}
```

| Request | Request body     | Response                      |
| :-------- | :------- | :-------------------------------- |
| multipart/form-data      | `text`  **Required**. employee_id, company_id, year | (fetching the corresponding attendance data) |

#### Example
#### Request:
```bash
employee_id: 1001
company_id: 1
year: 2022
```
#### Response body:
```bash
{
  "company_id": 1,
  "employee_id": 1001,
  "year": 2022,
  "employee_name": "John Smith",
  "january": 16,
  "february": 20,
  "march": 17,
  "april": 15,
  "may": 16,
  "june": 19,
  "july": 19,
  "august": 18,
  "september": 20,
  "october": 19,
  "november": 21,
  "december": 21
}
```
```http://127.0.0.1:8000/docs```


## HTML,CSS,JS Files
#### Folder: templates

 - Home Page- home.html
#### Go to home page and explore!
## :)


### Images

![Homepage](images/Homepage.png)

![Uploadpage](images/Uploadpage.png)

![Viewattendance](images/Viewattendance.png)

![Attendancereport](images/Attendancereport.png)
