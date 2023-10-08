import random
lower_alpha="abcdefghijklmnopqrstuvwxyz"
upper_alpha=lower_alpha.upper()
numbers="123456789"
symbols="~!@#$%^&*()"
password=lower_alpha+upper_alpha+numbers+symbols
length_password=int(input("enter the length of password:"))
a="".join(random.sample(password,length_password))
print(f"your password is {a}")