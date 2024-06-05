# Question 1
string=str(input("Enter a string: "))
length=len(string)
count=0
for i in range(0,length//2):
    if string[i]==string[length-i-1]:
        count+=1
if count==length//2:
    print("Yes")
else:
    print("No")
# Question 2
ls=[3,'d','e',4,1,'hello',3,'e']
new=set(ls)
print(new)
# Question 3
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(amount," has been deposited")
    def withdraw(self,amount):
        self.balance-=amount
        print(amount," has been withdrawn")
    def checkBalance(self):
        print("Your existing balance is ",self.balance)
user1=BankAccount(4000)
user1.deposit(150)
user1.withdraw(200)
user1.checkBalance()