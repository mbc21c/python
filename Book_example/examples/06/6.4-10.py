from openpyxl import Workbook

# ���� ���� ������ ���� Ŭ���� ���� ����
xlsx = load_workbook('other.xlsx')

# '���ο��Ʈ2' ��Ʈ�� ������
sheet = xlsx['���ο��Ʈ2']

# ���� ���
print(sheet['A1'].value)

