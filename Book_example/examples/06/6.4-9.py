from openpyxl import Workbook

# ���ο� ���� ���� ������ ���� Ŭ���� ���� ����
xlsx = Workbook()

# '���ο��Ʈ2' �̸��� ���� ��Ʈ ����
sheet = xlsx.create_sheet('���ο��Ʈ2')
sheet['A1'] = '������'

# ���� ���Ϸ� ����
xlsx.save('other.xlsx')

