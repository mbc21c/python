import numpy as np
import pandas as pd

obj = pd.read_excel('d:\source\python\pandas\mandoo.xlsx', sheet_name='Sheet1')
obj['근무시간'] = obj['퇴근시간'] - obj['출근시간']
obj['시간당만두'] = obj['만두생산'] - obj['근무시간']
obj = obj.sort_values(by=['시간당만두','근무시간'], ascending=[False,False])

print(obj)

obj.to_excel('d:\\source\\python\\pandas\\result.xlsx', sheet_name='Sheet1')