"""
����� ForeignPassport �������� ����������� �� ������ Passport. ����� PrintInfo
���������� � ����� �������. PassportList ������������ ����� ������, ���������� �������
����� �������. ����� ������ PrintInfo ��� ������� �������� ������ ������������� ���
����������� ���������.
"""

class Passport:
    def __init__(self, first_name, last_name, birthday, number, country):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.number = number
        self.country = country


    def print_info(self):
        print(self.first_name, self.last_name, self.birthday, self.number, self.country)

class ForeignPassport(Passport):
    def __init__ (self, first_name, last_name, birthday, number, country, visa):
        self.visa = visa
        super(). __init__(first_name, last_name, birthday, number, country)

    def print_info(self):
        super().print_info()
        print(self.visa)

passportlist = []
foreignpassport = ForeignPassport("Alex", "Asper", "23.09. 2004", 13452, "Abkhazia", "����")
passport = Passport("Alex", "Asper", "23.09. 2004", 13422, "Abkhazia")
passportlist.append(foreignpassport)
passportlist.append(passport)
print(passportlist)
print(passportlist[0].number)
