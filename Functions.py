import requests
class scripts:
    def __init__(self,api,amount=""):
        self.api = api
        self.amount = amount
        self.data = requests.get(api).json
        self.date = self.data()["date"]
        self.rates = self.data()["rates"]["EUR"]
        self.base = self.data()["base"]
        self.exchange_to = list(self.data()["rates"])[0]
    def exchange(self):
        self.amount=input("Please Enter amount currency: ")
        user_exchange_to=input("please Enter what is the currency do you need exchange? ")
        if user_exchange_to.upper() == self.exchange_to:
            print(f" {self.amount} {self.base} = {round((float(self.amount) * self.rates),4)} {self.exchange_to}  ------- last update {self.date} ")
        else:
            print(f"sorry your current entry {user_exchange_to.upper()} is not available now please try again latter.")
        