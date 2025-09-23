import pytest

from main import get_student_grades, read_csv


def test_student_grades():
    students = [
        {'student_name': 'Семенова Елена', 'grade': 5},
        {'student_name': 'Титов Владислав', 'grade': 2},
        {'student_name': 'Семенова Елена', 'grade': 3},
        {'student_name': 'Семенова Елена', 'grade': 2}
    ]
    result = get_student_grades(students)
    assert len(result) == 2
    assert result[0][0] == 'Семенова Елена'
    assert result[0][1] == 3.33


def test_read_csv():
    students = read_csv(['not_extists.csv'], 'data')
    assert students == []
