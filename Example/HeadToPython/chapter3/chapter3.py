import os


os.chdir('D:\Source\Python\Example\HeadToPython')

data = open('sketch.txt')
print(data.readline(), end='')
print(data.readline(), end='')

data.seek(0)

for each_line in data:
    if not each_line.find(':') == -1:
        (role, line_spoken) = each_line.split(':',1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')

data.close()
