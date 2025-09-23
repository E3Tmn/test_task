import argparse
import csv
import os
from collections import defaultdict

from tabulate import tabulate


def read_csv(file_names, folder_name):
    students = []
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(row)
        else:
            print(f"Файл {file_path} не найден")

    return students


def get_student_grades(students):
    student_grades = defaultdict(list)
    for student in students:
        student_grades[student['student_name']].append(int(student['grade']))
    student_grades = sorted(
        [[name, round(sum(grades)/len(grades), 2)] for name, grades in student_grades.items()],
        key=lambda x: x[1],
        reverse=True)
    return student_grades


def main():
    parser = argparse.ArgumentParser(description='Скрипт читает файлы с данными об успеваемости студентов и формирует отчеты')
    parser.add_argument('--files', nargs='*', required=True, help='Названия исходных файлов')
    parser.add_argument('--report', help='Тип итогового отчета')
    args = parser.parse_args()
    file_names = args.files
    report_type = args.report
    folder_name = 'data'
    students = read_csv(file_names, folder_name)
    if report_type == 'student-performance':
        student_performance = get_student_grades(students)
        print(tabulate(student_performance, headers=['student_name', 'grade'], tablefmt="pipe"))
    else:
        print('Неизвестная форма отчета')


if __name__ == '__main__':
    main()
