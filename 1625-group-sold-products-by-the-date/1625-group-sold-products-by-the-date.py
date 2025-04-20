import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.sort_values(by = ['product', 'sell_date'], ascending = True).drop_duplicates()
    activities = activities.groupby(['sell_date']).agg({'product': ','.join}).reset_index()
    activities['num_sold'] = activities['product'].str.count(',') + 1
    activities = activities.rename(columns = {'product': 'products'})
    activities = activities[['sell_date', 'num_sold', 'products']]
    return activities