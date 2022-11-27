class BankAccount():
    def __init__(self, name, balance, passport):
        self._name = name
        self.__balance = balance
        self.__passport = passport


    def getbalance(self):
        return self.__balance

    def getpassport(self):
        return self.__passport


    def setbalance(self, newbalance):
        if newbalance < 0:
            print("")
        else:
            print("")
            self.__balance = newbalance


    def setnomerpassport(self,password,passport):
        if password == "1234":
            print("")
            self.__passport = passport
        else:
            print("")


    def delpassport(self, password):
        if password == "123456789":
            del self.__passport


account1 = BankAccount("?????", 1000000, 99999)
print(account1.getbalance())
print(account1.getpassport())
account1.setbalance(-23)
account1.setnomerpassport(5346,25236)
account1.delpassport(2523)