"""
�������� ����� ������� ����� ������������� �������� name � ����� �����
������� � ����� ���������� ������� "�����". �������� ��� 1 �����, ����������� ����������.
�� ������ ������ �������� ����� ������ �������� � �������� � ������ ������� "�� ��� �������� ���� �� �� ����� ����� ���".
�������� ��������� ������� ������ � ����� ������ � �������� ����� ���������� ��� �������.
"""


class Fullname:

    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"{self.name} �����")


class Name(Fullname):

    def display_info_dop(self):
        print(f"{self.name} ����� � ��� �� ��������")

alex = Fullname("�����")
alex.display_info()

alex = Name("�����")
alex.display_info_dop()