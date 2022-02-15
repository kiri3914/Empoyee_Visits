import openpyxl

book = openpyxl.Workbook()

sheet = book.active

sheet['A1'] = 'Имя'
sheet['B1'] = 'email'
sheet['C1'] = 'Телефон'

book.save('my_book.xlsl')
book.close()

