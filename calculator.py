print('1.addition')
print('2.subtraction')
print('3.multiplication')
print('4.division')
operation=int(input('enter the operator:'))
a=int(input('enter the first number:'))
b=int(input('enter the second number number:'))
if operation==1:
    x=a+b
    print(x)
elif operation==2:
   x=a-b
   print(x)
elif operation==3:
   x=a*b
   print(x)
elif operation==4:
   x=a/b
   print(x)
else:
  print('enter valid operator')
