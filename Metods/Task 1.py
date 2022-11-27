"""
�������� ����� Person � �������� ����� �������� name � age.
�������� ����� ���������� ������� ������� ���������� � ��������.
�������� ����� ������ ������� ���������� ����� ������ ������
������� ������� ������� ��������: ����������� ��� - ��� ������� �������� � �����.
(���������: ��� ����� ������������ ����� today().year ������ date �� ������ datetime)
�������� ����������� ����� ������� ��������� �������� �� ���������������� ������� ������� �������� ���������� � �����.
"""
from datetime import date

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def ptintname(self):
        print(self.name, self.age)

    @classmethod
    def classmethod(cls, year):
        return Person("�����", date.today().year - year)

    @staticmethod
    def staticmethod(age):
        if age < 18:
            return "no soversh"
        else:
            return "yes soversh"


alex = (Person.classmethod(2004))
print(alex.name)
print(alex.age)
print(alex.staticmethod(17))