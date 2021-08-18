import os
import sys
from win32com.client import GetObject

 

WMI = GetObject('winmgmts:')
processes = WMI.InstancesOf('Win32_Process')

for process in processes:

    print(process.Properties_('Name').Value)