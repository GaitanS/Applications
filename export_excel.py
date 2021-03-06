import mysql.connector as mysql
import xlsxwriter


def get_data(table_name):
    db = mysql.connect(host='localhost', user='root', password='Frectie!234', database='trainers')
    with db.cursor() as c:
        c.execute('SELECT * FROM ' + table_name)
        header = [row[0] for row in c.description]

        rows = c.fetchall()
        c.close()

    return header, rows


def export_to_excel(table_name):
    # Create an new Excel file and add a worksheet
    workbook = xlsxwriter.Workbook(table_name + '.xlsx')
    worksheet = workbook.add_worksheet('Trainers')

    # Create style for cells
    header_cell_format = workbook.add_format({'bold': True, 'border': True, 'bg_color': 'yellow'})
    body_cell_format = workbook.add_format({'border': True})

    header, rows = get_data(table_name)

    row_index = 0
    column_index = 0

    for column in header:
        worksheet.write(row_index, column_index, column, header_cell_format)
        column_index += 1
    row_index += 1
    for row in rows:
        column_index = 0
        for column in row:
            worksheet.write(row_index, column_index, column, body_cell_format)
            column_index += 1
        row_index += 1

    workbook.close()


export_to_excel('trainer')
