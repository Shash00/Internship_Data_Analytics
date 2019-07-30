from openpyxl import Workbook
import csv

wb = Workbook()
sheet = wb.active

with open('cs.csv') as f:
    data = csv.reader(f)
   
    for i in data:
        sheet.append(i)
wb.save('student.xlsx')