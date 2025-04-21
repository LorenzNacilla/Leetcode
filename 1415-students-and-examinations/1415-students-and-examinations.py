import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    student_subjects = pd.merge(
        left = students,
        right = subjects,
        how = 'cross'
    )
    examinations = examinations.groupby(['student_id', 'subject_name'])['subject_name'].count().reset_index(name = 'attended_exams')
    student_subjects = pd.merge(
        left = student_subjects,
        right = examinations,
        how = 'left',
        on = ['student_id', 'subject_name']
    ).sort_values(by = ['student_id', 'subject_name'], ascending = True)
    student_subjects['attended_exams'] = student_subjects['attended_exams'].fillna(0)
    return student_subjects