import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(
        left = employee,
        right = employee,
        how = 'inner',
        left_on = ['id'],
        right_on = ['managerId']
    ).groupby(['id_x', 'name_x'], dropna = False)['id_y'].count().reset_index(name = 'count_of_direct_reports')
    df = df[df['count_of_direct_reports'] >= 5].drop(columns = ['id_x', 'count_of_direct_reports']).rename(columns = {'name_x': 'name'})
    return df