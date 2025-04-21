import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].count().reset_index()
    actor_director = actor_director[actor_director['timestamp'] >= 3].drop(columns = 'timestamp', axis = 1)
    return actor_director