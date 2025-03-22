import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if x['employee_id'] % 2 !=0 and x['name'][0] != 'M' else 0, axis = 1)
    employees = employees.sort_values(by = 'employee_id', ascending = True).get(['employee_id', 'bonus'])
    return employees