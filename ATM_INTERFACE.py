import time
print("Please Insert Your Card ")
time.sleep(2)
password=1234

balance=5000
pin=int(input("enter your pin : "))
while True :
    if pin==password:
        print(""" 
           1==balance
           2==withdraw balance
           3== deposite balance
           4==exit
        """)
        try:
            option=int(input("Please enter your choice :"))
        except:
            print("Please enter valid option")
        if option==1:
            print(f"Your current Balance is {balance}")
        if option==2:
            withdraw_amount=int(input("Please enter withdrawl amount :"))
            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your current balance is {balance}")

        if option==3:
            deposite_amount = int(input("Please enter deposite amount :"))
            balance = balance + deposite_amount
            print(f"{deposite_amount} is Credited from your account")
            print(f"your updated balance is {balance}")
        if option==4:
            break;
    else:
        print("Opps Wrong Pin !!\n Try again")
        pin=int(input("enter your pin : "))
        