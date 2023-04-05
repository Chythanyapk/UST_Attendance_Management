import sqlalchemy
import pandas as pd
import psycopg2
from sqlalchemy import create_engine,text
from concurrent.futures import ThreadPoolExecutor


def calculate_working_days(employee_data):
    employee_id, data = employee_data
    attendance_data = pd.DataFrame(data, columns=['company_id', 'employee_id', 'employee_name', 'in_time', 'out_time'])
    attendance_data['in_time'] = pd.to_datetime(attendance_data['in_time'])
    attendance_data['out_time'] = pd.to_datetime(attendance_data['out_time'])
    daily_working_hours = (attendance_data['out_time'] - attendance_data['in_time']).dt.total_seconds() / 3600
    attendance_data = attendance_data[daily_working_hours >= 8]
    monthly_working_days = attendance_data.groupby([
        pd.Grouper(key='in_time', freq='M'),
        'company_id',
        'employee_id',
        'employee_name'
    ]).apply(lambda x: len(x))

    results = {}

    for index, row in monthly_working_days.items():
        company_id, employee_id, employee_name = index[1], index[2], index[3]
        month = index[0].strftime('%B')
        year = index[0].year
        working_days = row
        key = (company_id, employee_id, employee_name, year)
        if key not in results:
            results[key] = {'january': 0, 'february': 0, 'march': 0, 'april': 0, 'may': 0, 'june': 0, 'july': 0, 'august': 0, 'september': 0, 'october': 0, 'november': 0, 'december': 0}
        results[key][month.lower()] = working_days
    try:
        df = pd.DataFrame.from_dict(results, orient='index').reset_index()
        df = pd.DataFrame.from_dict(results, orient='index').reset_index() \
            .rename(columns={'index': 'company_id_employee_id_employee_name_year',
                             'level_0': 'company_id',
                             'level_1': 'employee_id',
                             'level_2': 'employee_name',
                             'level_3': 'year'})
        #print(df.to_string(index=False))
       # print(df)
    except Exception as e:
     print(e)

    try:

          engine = sqlalchemy.create_engine(f'postgresql://postgres:Chachupk15&@localhost:5432/Demo')

          df.to_sql(name='attendance_sheet', con=engine, if_exists='append', index=False)

    except Exception as e:
      print(e)

    return df


def workcall():
    engine = sqlalchemy.create_engine(
        f'postgresql://postgres:Chachupk15&@localhost:5432/Demo'
    )
    query = "SELECT * FROM attendance_data;"
    df = pd.read_sql_query(sql=text(query), con=engine.connect())
    engine.dispose()
    #calculate_working_days(('employee_id', df))
    employee_attendance = df.groupby(['company_id', 'employee_id']).apply(
        lambda x: x[['company_id', 'employee_id', 'employee_name', 'in_time', 'out_time']].values.tolist())
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(calculate_working_days, employee_attendance.items())