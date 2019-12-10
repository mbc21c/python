import telepot
a_bot = telepot.Bot(token = '640207892:AAEbeoJ3T-MHl-_C_DJoaHzit_TK_X_RQX4')
mc = 215597857

a_bot.sendMessage(mc, "")

for i in a_bot.getUpdates():
    print(i)
#a_bot.sendMessage("aa")

