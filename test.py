import telebot
from telebot import types
BUT_TOKEN="8375049997:AAHd8vq0JwB6QB3uHdSDYfy6cjAc5TxIZV4"
bot=telebot.TeleBot(BUT_TOKEN)
@bot.message_handler(commands='start')
def start(message):
    markup=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    btn1=telebot.types.KeyboardButton('Videosmile')
    markup.add(btn1)
    bot.send_message(message.chat.id,"Online mini kurslar",reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def satrt(message):
    btn13=telebot.types.KeyboardButton('Asosiy menu')
    if message.text=="Asosiy menu":
        markup=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        btn1=telebot.types.KeyboardButton('3D modeling')
        btn2=telebot.types.KeyboardButton('3D modeling for games')
        btn3=telebot.types.KeyboardButton('Grafic design')
        btn4=telebot.types.KeyboardButton('Motion design')
        btn5=telebot.types.KeyboardButton('Web design')
        btn6=telebot.types.KeyboardButton('Cinema 4D')
        markup.add(btn1,btn2)
        markup.add(btn3,btn4)
        markup.add(btn5,btn6)
        
    elif message.text=="Videosmile":
        markup=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        btn1=telebot.types.KeyboardButton('3D modeling')
        btn2=telebot.types.KeyboardButton('3D modeling for games')
        btn3=telebot.types.KeyboardButton('Grafic design')
        btn4=telebot.types.KeyboardButton('Motion design')
        btn5=telebot.types.KeyboardButton('Web design')
        btn6=telebot.types.KeyboardButton('Cinema 4D')
        markup.add(btn1,btn2)
        markup.add(btn3,btn4)
        markup.add(btn5,btn6)
        bot.send_message(message.chat.id,"Bepul o'quv kurslari",reply_markup=markup)
    elif message.text=="3D modeling":
        markup=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        btn1=telebot.types.KeyboardButton('<1-Dars>')
        btn2=telebot.types.KeyboardButton('<2-Dars>')
        btn3=telebot.types.KeyboardButton('<3-Dars>')
        btn4=telebot.types.KeyboardButton('<4-Dars>')
        btn5=telebot.types.KeyboardButton('<5-Dars>')
        btn6=telebot.types.KeyboardButton('<6-Dars>')
        btn7=telebot.types.KeyboardButton('<7-Dars>')
        btn8=telebot.types.KeyboardButton('<8-Dars>')
        btn9=telebot.types.KeyboardButton('<9-Dars>')
        btn10=telebot.types.KeyboardButton('<10-Dars>')
        btn11=telebot.types.KeyboardButton('<11-Dars>')
        btn12=telebot.types.KeyboardButton('<12-Dars>')
        markup.add(btn1,btn2,btn3)
        markup.add(btn4,btn5,btn6)
        markup.add(btn7,btn8,btn9)
        markup.add(btn10,btn11,btn12)
        markup.add(btn13)
        bot.send_message(message.chat.id,"Darslar",reply_markup=markup)
    











    elif message.text=="Grafic design":
        markup=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        btn1=telebot.types.KeyboardButton('(1-Dars)')
        btn2=telebot.types.KeyboardButton('(2-Dars)')
        btn3=telebot.types.KeyboardButton('(3-Dars)')
        btn4=telebot.types.KeyboardButton('(4-Dars)')
        btn5=telebot.types.KeyboardButton('(5-Dars)')
        markup.add(btn1,btn2,btn3)
        markup.add(btn4,btn5)
        markup.add(btn13)
        bot.send_message(message.chat.id,"Darslar",reply_markup=markup)
    elif message.text=="3D modeling for games":
        markup=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        btn1=telebot.types.KeyboardButton('*1-Dars*')
        btn2=telebot.types.KeyboardButton('*2-Dars*')
        btn3=telebot.types.KeyboardButton('*3-Dars*')
        btn4=telebot.types.KeyboardButton('*4-Dars*')
        btn5=telebot.types.KeyboardButton('*5-Dars*')
        
        markup.add(btn1,btn2,btn3)
        markup.add(btn4,btn5)
        markup.add(btn13)
        bot.send_message(message.chat.id,"Darslar",reply_markup=markup)
    elif message.text=="Motion design":
        markup=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        btn1=telebot.types.KeyboardButton('!1-Dars!')
        btn2=telebot.types.KeyboardButton('!2-Dars!')
        btn3=telebot.types.KeyboardButton('!3-Dars!')
        btn4=telebot.types.KeyboardButton('!4-Dars!')
        markup.add(btn1,btn2)
        markup.add(btn3,btn4)
        markup.add(btn13)
        bot.send_message(message.chat.id,"Darslar",reply_markup=markup)
    elif message.text=="Web design":
        markup=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        btn1=telebot.types.KeyboardButton('^1-Dars^')
        btn2=telebot.types.KeyboardButton('^2-Dars^')
        btn3=telebot.types.KeyboardButton('^3-Dars^')
        markup.add(btn1,btn2,btn3)
        markup.add(btn13)
        bot.send_message(message.chat.id,"Darslar",reply_markup=markup)
    elif message.text=="Cinema 4D":
        markup=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
        btn1=telebot.types.KeyboardButton('#1-Dars#')
        btn2=telebot.types.KeyboardButton('#2-Dars#')
        btn3=telebot.types.KeyboardButton('#3-Dars#')
        btn4=telebot.types.KeyboardButton('#4-Dars#')
        btn5=telebot.types.KeyboardButton('#5-Dars#')
        btn6=telebot.types.KeyboardButton('#6-Dars#')
        btn7=telebot.types.KeyboardButton('#7-Dars#')
        btn8=telebot.types.KeyboardButton('#8-Dars#')
        markup.add(btn1,btn2,btn3)
        markup.add(btn4,btn5,btn6)
        markup.add(btn7,btn8)
        markup.add(btn13)
        bot.send_message(message.chat.id,"Darslar",reply_markup=markup)
    elif message.text=="<1-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8478")
    elif message.text=="<2-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8479")
    elif message.text=="<3-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8480")
    elif message.text=="<4-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8481")
    elif message.text=="<5-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8482")
    elif message.text=="<6-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8483")
    elif message.text=="<7-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8484")
    elif message.text=="<8-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8485")
    elif message.text=="<9-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8486")
    elif message.text=="<10-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8487")
    elif message.text=="<11-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8488")
    elif message.text=="<12-Dars>":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=579&pid=0&lid=8541")
#_________________________________________________________________________________________________________________
    if message.text=="(1-Dars)":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=628&pid=0&lid=9263")
    elif message.text=="(2-Dars)":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=628&pid=0&lid=9264")
    elif message.text=="(3-Dars)":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=628&pid=0&lid=9265")
    elif message.text=="(4-Dars)":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=628&pid=0&lid=9266")
    elif message.text=="(5-Dars)":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=628&pid=0&lid=9267")
#____________________________________________________________________________________________________________________
    if message.text=="*1-Dars*":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=628&pid=0&lid=9263")
    elif message.text=="*2-Dars*":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=628&pid=0&lid=9264")
    elif message.text=="*3-Dars*":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=628&pid=0&lid=9265")
    elif message.text=="*4-Dars*":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=628&pid=0&lid=9266")
    elif message.text=="*5-Dars*":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=628&pid=0&lid=9267")
#______________________________________________________________________________________________________________________
    if message.text=="!1-Dars!":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=559&pid=0&lid=8163")
    elif message.text=="!2-Dars!":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=559&pid=0&lid=8165")
    elif message.text=="!3-Dars!":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=559&pid=0&lid=8167")
    elif message.text=="!4-Dars!":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=559&pid=0&lid=8169")
#________________________________________________________________________________________________________________________________
    if message.text=="^1-Dars^":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=623&pid=0&lid=9155")
    elif message.text=="^2-Dars^":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=623&pid=0&lid=9156")
    elif message.text=="^3-Dars^":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=623&pid=0&lid=9157")
#_____________________________________________________________________________________________________________
    if message.text=="#1-Dars#":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=569&pid=0&lid=8223")
    elif message.text=="#2-Dars#":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=569&pid=0&lid=8225")
    elif message.text=="#3-Dars#":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=569&pid=0&lid=8227")
    elif message.text=="#4-Dars#":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=569&pid=0&lid=8229")
    elif message.text=="#5-Dars#":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=569&pid=0&lid=8231")
    elif message.text=="#6-Dars#":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=569&pid=0&lid=8233")
    elif message.text=="#7-Dars#":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=569&pid=0&lid=8235")
    elif message.text=="#8-Dars#":
        bot.send_message(message.chat.id,"https://cloudlessons.ru/online/course.html?id=569&pid=0&lid=8237")

print("Salom")
bot.infinity_polling()