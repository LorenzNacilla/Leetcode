import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(
        left = employee,
        right = department,
        how = 'inner',
        left_on = 'departmentId',
        right_on = 'id'
    )
    df['rank'] = df.groupby(['name_y'])['salary'].rank(method = 'dense', ascending = False)
    df = df[df['rank'] == 1]
    df = df.drop(['id_x', 'departmentId', 'id_y', 'rank'], axis = 1)
    df.rename(columns = 
    {'name_x': 'Employee',
    'salary': 'Salary',
    'name_y': 'Department'
    }, inplace = True)
    return df