import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby(['class'])['student'].count().reset_index(name = 'count')
    courses = courses[courses['count'] >= 5].drop(['count'], axis = 'columns')
    return courses