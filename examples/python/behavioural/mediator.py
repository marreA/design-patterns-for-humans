
# Mediator pattern adds a third party object (called mediator) to control the interaction between two objects (called colleagues). It helps reduce the coupling between the classes communicating with each other. Because now they don't need to have the knowledge of each other's implementation.

import datetime

class ChatRoomMediator:
    
    def show_message(self, user, message):
        pass
    

class ChatRoom(ChatRoomMediator):
    
    def show_message(self, user, message):
        time = datetime.datetime.now()
        sender = user.name
        print(f"{time} [{sender}]: {message}")

class User:

    def __init__(self, name, chat_mediator):
        self.name = name
        self.chat_mediator = chat_mediator

    def send(self, message):
        self.chat_mediator.show_message(self, message)


mediator = ChatRoom()
john = User("John Doe", mediator)
jane = User("Jane Doe", mediator)
john.send("Hi there!")
jane.send("Hey!")