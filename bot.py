import telebot
import random
token ="yourbotid"
bot = telebot.TeleBot(token)
HELP = """
/help - вывести список доступных команд.
/add - добавить задачу в список ( название задачи запрашиваем у пользователя).
/snow - напечатать все добавленные задачи.
/exit - выход из программы
/random - добавить случайную задачу на дату Сегодня"""

RANDOM_TASKS = ["Выучить внезапно французский язык", "Решить 27ое задание на Pascal","Помолить во славу Евангелиона", "Покормить дракона", "Напиться из-за четвёрки Лизы","Выучить Войну и мир", "Заблокировать Никиту", "Сказать, Денис токсик"]




tasks = {}

def add_todo(date, task):
  if date in tasks:
            # Дата есть в словаре
            # Добавляем в список задачу
            tasks[date].append(task)
  else:
            # Даты в словаер нет
            # Создаём запись с ключом date
            tasks[date] = []
            tasks[date].append(task)




@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message): #message.text = /print <date>
    command = message.text.split(maxsplit=1)
    dates = command[1].replace(' ', '').lower().split(',')
    text = ""
    for date in dates:
      if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text +"[] " + task + "\n"
      else:
          text = "Запланированных событий на этот день нет"
      bot.send_message(message.chat.id, text)




# Постоянно обращается к серверам телеграм
bot.polling(none_stop=True)
