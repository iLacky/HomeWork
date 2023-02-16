class Bot:
    def __init__(self, name):
        self.name = name
    def say_message(self, message):
        print(message)
    def say_name(self,):
        print(self.name)


obj = Bot('Marvin')
obj.say_name()
obj.say_message('message')


class TelegramBot(Bot):
    url = None
    chat_id = None
    def __init__(self, name):
        Bot.__init__(self, name)

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id
        
    def send_message(self, message):
        print(f'{self.name} bot says {message} to chat {self.chat_id} using {self.url}')


telegram_bot = TelegramBot('TG')
telegram_bot.say_name()
telegram_bot.set_url(1)
telegram_bot.send_message('Hello')
