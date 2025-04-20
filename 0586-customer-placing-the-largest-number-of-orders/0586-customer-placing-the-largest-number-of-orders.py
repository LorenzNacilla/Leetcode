import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby(['customer_number'])['order_number'].count().reset_index().sort_values(by = ['order_number'], ascending = False).head(n = 1).drop(columns = ['order_number'])
    return orders