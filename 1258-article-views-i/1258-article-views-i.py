import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views['author_id'] == views['viewer_id']].sort_values(by = 'author_id', ascending = True)
    views = views.rename(columns = {'author_id': 'id'})
    views = views[['id']].drop_duplicates()
    return views