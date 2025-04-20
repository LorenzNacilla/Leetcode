import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    category_lookup = {'category': ['Low Salary', 'Average Salary', 'High Salary'], 'accounts_count': [0, 0, 0]}
    category_lookup = pd.DataFrame(category_lookup)
    def category(x):
        if x < 20000:
            return 'Low Salary'
        elif x >=  20000 and x <= 50000:
            return 'Average Salary'
        else:
            return 'High Salary'
    accounts['category'] = accounts['income'].apply(category)
    accounts = accounts.groupby(['category'])['account_id'].count().reset_index(name = 'accounts_count')
    df = pd.merge(
        left = category_lookup,
        right = accounts,
        how = 'left',
        left_on = ['category'],
        right_on = ['category']
    )
    df['accounts_count_y'] = df['accounts_count_y'].fillna(df['accounts_count_x'])
    df = df.drop(columns = ['accounts_count_x'])
    df = df.rename(columns = {'accounts_count_y': 'accounts_count'})
    return df