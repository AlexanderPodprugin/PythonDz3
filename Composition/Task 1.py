"""
�������� ���������� User ���������� ��:
������� Profile �� ����������: name,last_name,age,pasport � ������� print_info.
������� Address �� ���������� : City,street,zipcode
������� Role �� ����������: role,hours_worked
������� BankAccount �� ����������: card_number, balance
������� Order � ������� ���������������� ��������� ������: Item,date,delivery,price
�������� � ���������� ������ �������� �������, ��������� ������, ����, �������� ����������� �������� � ���������� ������
"""

class Profile:
    def init(self, name, last_name, age, pasport):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.pasport = pasport
    def print_info(self):
        print(self.name, self.last_name, self.age, self.pasport)

class Address:
    def init(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode

class Role:
    def init(self, role, hours_worked):
        self.role = role
        self.hours_worked = hours_worked

class Bank_Account:
    def init(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance

class Order:
    def init(self, item, date, delivery, price):
        self.item = item
        self.date = date
        self.delivery = delivery
        self.price = price

class User:
    def create_profile(self):
        self.adress = []
        self.bank_ac = []
        self.order = []

    def new_profile(self, name, last_name, age, pasport):
        self.profile = Profile(name, last_name, age, pasport)

    def your_adress(self, city, street, zipcode):
        self.adress.append(Address(city, street, zipcode))

user1 = User()
user1.new_profile('�����', '���������', 18, 233424232 )
user1.your_adress('����', '�������������', 12)

print(user1.profile.name)
print(user1.adress.sity)
print(user1.profile.name, user1.profile.last_name)
print(user1.adress[0].city)

print(user1.adress[1].city)