import csv
import openpyxl
import os


def csv_to_excel(csv_files, excel_file):
    wb = openpyxl.Workbook()

    if 'Sheet' in wb.sheetnames:
        wb.remove(wb['Sheet'])


    for csv_file in csv_files:
        sheet_name = os.path.splitext(os.path.basename(csv_file))[0]

        ws = wb.create_sheet(title=sheet_name)

        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                ws.append(row)

    wb.save(excel_file)



if __name__ == "__main__":
    csv_files = ['1.csv', '2.csv', '3.csv']
    excel_file = 'output.xlsx'
    csv_to_excel(csv_files, excel_file)