order = 'spagetti'
menu = { 'spam':500, 'ham':700, 'egg':300, 'spagetti':900}
price = menu.get(order,0)
print(price)