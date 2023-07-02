import openpyxl as xl
wb1 = xl.load_workbook("wingspan-20221201.xlsx")
sheet = wb1["Birds"]


def habitats(x, y):




sums, names = sum_hits_in_columns(17, 24)
print(sums)
print(names)