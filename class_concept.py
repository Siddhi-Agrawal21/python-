class SavingAccount:
    def __init__(self, rate, balance):
        self.annual_inter_rate = rate
        self.saving_balance = balance

    def MonthlyInterest(self):
        self.interest = (self.annual_inter_rate * self.saving_balance)/(12*100)
        print("Monthly Interest =", str(self.interest))
        self.saving_balance += self.interest
        print("total saving balance =", str(self.saving_balance))

    def Modify_interest_rate(self, new_rate):
        self.annual_inter_rate = new_rate


person1 = SavingAccount(5, 2000)
person1.MonthlyInterest()
person2 = SavingAccount(5, 3000)
person2.MonthlyInterest()

person1.Modify_interest_rate(7)
person2.Modify_interest_rate(7)

person1.MonthlyInterest()
person2.MonthlyInterest()
