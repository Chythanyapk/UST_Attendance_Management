import sqlalchemy
import pandas as pd


def read_data(file):
    file_extension = file.filename.split('.')[-1]
    if file_extension == 'csv':
        df = pd.read_csv(file.file)
    elif file_extension == 'json':
        df = pd.read_json(file.file)
    else:
        raise ValueError('Invalid file format')
    return df


def data_filter(employee_data):
    employee_id, data = employee_data
    attendance_data = pd.DataFrame(data, columns=['company_id', 'employee_id', 'employee_name', 'in_time', 'out_time'])
    #
    # def convert_timezone(attendance_data, timezone='Asia/Kolkata', to_timezone='UTC'):
    #     if attendance_data['in_time'].dt.tz is None:
    #         attendance_data['in_time'] = attendance_data['in_time'].dt.tz_localize(timezone)
    #     else:
    #         attendance_data['in_time'] = attendance_data['in_time'].dt.tz_convert(to_timezone)
    #
    #     if attendance_data['out_time'].dt.tz is None:
    #         attendance_data['out_time'] = attendance_data['out_time'].dt.tz_localize(timezone)
    #     else:
    #         attendance_data['out_time'] = attendance_data['out_time'].dt.tz_convert(to_timezone)
    #     attendance_data['in_time'] = attendance_data['in_time'].dt.strftime('%Y-%m-%dT%H:%M:%S')
    #     attendance_data['out_time'] = attendance_data['out_time'].dt.strftime('%Y-%m-%dT%H:%M:%S')
    #
    #     return attendance_data
    #
    # attendance_data = convert_timezone(attendance_data)
    # print(attendance_data.head())
    # attendance_data['in_time'] = pd.to_datetime(attendance_data['in_time'])
    # attendance_data['out_time'] = pd.to_datetime(attendance_data['out_time'])
    attendance_data['in_time'] = attendance_data['in_time'].apply(
        lambda x: pd.NaT if pd.isna(x) or x in ['L', 'Leave', 'null', 0] else pd.to_datetime(x,
                                                                                             errors='coerce').strftime(
            '%Y-%m-%dT%H:%M:%S') if x != '0000-00-00 00:00:00' else pd.NaT)
    attendance_data['out_time'] = attendance_data['out_time'].apply(
        lambda x: pd.NaT if pd.isna(x) or x in ['L', 'Leave', 'null', 0] else pd.to_datetime(x,
                                                                                             errors='coerce').strftime(
            '%Y-%m-%dT%H:%M:%S') if x != '0000-00-00 00:00:00' else pd.NaT)
    attendance_data.drop(
        attendance_data[(attendance_data['in_time'].isna()) | (attendance_data['out_time'].isna())].index, inplace=True)

    # column_map = {
    #     'company_id': 'companyId',
    #     'employee_id': 'employeeId',
    #     'employee_name': 'employeeName',
    #     'in_time': 'check_in',
    #     'out_time': 'check_out'
    # }
    # attendance_data = attendance_data.rename(columns=column_map)
    # print(attendance_data)
    try:
        engine = sqlalchemy.create_engine(
            f'postgresql://postgres:Chachupk15&@localhost:5432/Demo')

        attendance_data.to_sql(name='attendance_data', con=engine, if_exists='append', index=False)

    except Exception as e:
        print(e)
    # return attendance_data