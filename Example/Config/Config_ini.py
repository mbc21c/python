import configparser
import sys

config = configparser.ConfigParser()
config.read('config.ini')

x = config.get('DEFAULT', 'x')
y = config.get('DEFAULT', 'y')
cnt = config.get('DEFAULT', 'cnt')
print(x, y, cnt)



config.set('DEFAULT','x','500')
config.set('DEFAULT','y','600')
config.set('DEFAULT','cnt','30')

with open('config.ini', 'w') as configfile:
    config.write(configfile)
