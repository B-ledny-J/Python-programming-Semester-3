import json

class Ticket:
    def __init__(self, number, base_price):
        self.number = number
        self.base_price = base_price

    def get_price(self):
        return self.base_price

    def print_ticket(self):
        print(f"Ticket Number: {self.number}")
        print(f"Ticket Price: {self.get_price()}")

class RegularTicket(Ticket):
    pass

class EarlyTicket(Ticket):
    def get_price(self):
        return self.base_price * 0.7

class LateTicket(Ticket):
    def get_price(self):
        return self.base_price * 1.2

class StudentTicket(Ticket):
    def get_price(self):
        return self.base_price * 0.5

def load_tickets(filename):
    tickets = []
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            number = item["number"]
            base_price = item["N"] * 100
            ticket_type = item["type"].lower()
            if ticket_type == "звичайний":
                ticket = RegularTicket(number, base_price)
            elif ticket_type == "попередній":
                ticket = EarlyTicket(number, base_price)
            elif ticket_type == "пізніше":
                ticket = LateTicket(number, base_price)
            elif ticket_type == "студентський":
                ticket = StudentTicket(number, base_price)
            else:
                continue
            tickets.append(ticket)
    return tickets

def find_ticket(tickets, number):
    for ticket in tickets:
        if ticket.number == number:
            return ticket
    return None

tickets = load_tickets("tickets.json")
search_number = input("Введіть номер квитка для пошуку: ")
ticket = find_ticket(tickets, search_number)
if ticket:
    ticket.print_ticket()
else:
    print("Квиток не знайдено.")