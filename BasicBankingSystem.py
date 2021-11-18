# basic Banking system
# created by Zaur Hamzayev
''' 
Only for using class and functions in Python 
Created in Python 3.10 version
Jupyter IDE
'''
class Bank:

    def __init__(self, name, surname, password):

        self.name = name
        self.surname = surname
        self.password = password
        self.count_var = 0
        self.balance = 1000
    
    def check_customer(self):
        if self.name==self.name and self.surname==self.surname and self.password==self.password:
            print(f"{self.name}, Your Access Granted")
        else:
            print(f"{self.name}, please check again")
    
    def cash_in(self):
        cash_in_sum = int(input())
        self.balance = self.balance + cash_in_sum
        #return self.balance + cash_in_sum
        print(f"{self.name} Your balance has incrased to {self.balance}")
    
    def cash_out(self):
        cash_out_sum = int(input("How much money do you want to withdraw?  "))
        def warning(self):
            print(f'{self.name} {self.surname}, You are blocked, please call *1111')
        
        while cash_out_sum > self.balance:
            self.count_var += 1
            if self.count_var < 3:
                cash_out_sum = int(input("How much money do you want to withdraw?  ", ))
                            
            elif self.count_var == 3:
                return print(warning(self))
                                
        if cash_out_sum <= self.balance:
            self.count_var = 0
            self.balance = self.balance - cash_out_sum
            print("Your new balance is:", self.balance)
            
        else:
            pass
    
    def check_balance(self):
        print(self.balance)