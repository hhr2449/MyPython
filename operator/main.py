#算术运算符
a = 10
b = 3
print(a // b)
print(a ** b)

#赋值运算符
c = 10
c //= 3
print(c)
c **= 3
print(c)
if((d := 3) < 4):
    print(d)

#逻辑运算符
#直接使用and or not来表示
a = True
b = False
if(a and b):
    print('True')
else:
    print('False')

if(a or b):
    print('True')
else:
    print('False')

if(not a):
    print('False')
else:
    print('True')