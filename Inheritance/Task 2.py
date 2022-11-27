"""
Создайте класс который будет устанавливать свойство name и иметь метод
который к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП".
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""


class Fullname:

    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"{self.name} Гений")


class Name(Fullname):

    def display_info_dop(self):
        print(f"{self.name} гений и его не отчислят")

alex = Fullname("Алекс")
alex.display_info()

alex = Name("Алекс")
alex.display_info_dop()