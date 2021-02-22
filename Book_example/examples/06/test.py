from openpyxl import Workbook

for day in range(1,10):
    wb = Workbook()
    ws = wb.active
    for t in range(24):
        data = []
        data.append('2017.12.%d'%day)
        data.append('%2d:00:00'%t)
        data.append('log-data at \'2017-12-%d %2d:00:00\''%(day, t))
        ws.append(data)

    wb.save('2017.12.%d.xlsx'%day)
