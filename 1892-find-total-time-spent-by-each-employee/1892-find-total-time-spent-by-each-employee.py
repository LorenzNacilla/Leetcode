import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['difference'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['emp_id', 'event_day'])['difference'].sum().reset_index(name = 'total_time')
    employees = employees.rename(columns = {'event_day': 'day'})
    employees = employees[['day', 'emp_id', 'total_time']]
    return employees