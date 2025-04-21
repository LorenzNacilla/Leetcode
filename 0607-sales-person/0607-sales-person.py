import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    company = company[company['name'] == 'RED']
    df = pd.merge(
        left = company,
        right = orders,
        how = 'inner',
        on = 'com_id'
    ).drop(columns = ['com_id', 'name', 'city', 'order_id', 'order_date', 'amount'])
    df = pd.merge(
        left = sales_person,
        right = df,
        how = 'outer',
        on = 'sales_id',
        indicator = True
    )
    df = df[df['_merge'] == 'left_only'].get(['name'])
    return df