from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Anju', 'Ms.', 20, 4.7)

friend_one = Spy('Akriti', 'Ms.', 4.5, 21)
friend_two = Spy('Shelly', 'Ms.', 4.4, 20)
friend_three = Spy('Mohit', 'Mr.', 4.3, 20)
friend_four = Spy('Deepu', 'Ms.', 4.3, 20)


friends = [friend_one, friend_two, friend_three,friend_four]