from calc import MessageCreator
from handler import Handler


class ChatBot(Handler, MessageCreator):
    def get_username(self):
        print("What is your name?")
        self.get_last_text()
        self.github_username = self.last_text

    def show_message(self):
        self.get_username()
        self.get_message()
        print(self.message)
