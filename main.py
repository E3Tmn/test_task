import argparse
import csv
import os
from tabulate import tabulate

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скрипт читает файлы с данными об успеваемости студентов и формирует отчеты')
    parser.add_argument('--files', nargs='*', required=True, help='Названия исходных файлов')
    parser.add_argument('--report', help='Название итогового отчета')
    args = parser.parse_args()
    file_names = args.files
    report_name = args.report
    folder_name = 'data'
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers="keys", tablefmt="pipe"))
