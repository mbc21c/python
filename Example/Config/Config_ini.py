import configparser
import sys

config = configparser.ConfigParser()
config.read('config.ini')

x = config.get('TIME1', 'x')
y = config.get('TIME1', 'y')
cnt = config.get('TIME1', 'cnt')
print(x, y, cnt)



config.set('TIME1','x','500')
config.set('TIME1','y','600')
config.set('TIME1','cnt','30')

with open('config.ini', 'w') as configfile:
    config.write(configfile)
