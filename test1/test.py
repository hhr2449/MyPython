# python的标识符可以使用字母、数字、下划线，但是开头只能够使用字母或是下划线
from email.utils import collapse_rfc2231_value

_As = 1
print(_As)
#单行注释
'''
多行注释
多行注释
'''
"""
多行注释
多行注释
"""


#测试1
#这里正常使用if else语句，因为两个print语句的缩进相同，所以是同一个代码块
print("test1")
if _As == 1:
    print("Anwer")
    print("true")
else:
    print("Answer")
    print("false")


#测试2
#这里print("false")的缩进和上面的不一样，所以不属于else代码块，无论真假都会输出
print("test2")
if _As == 1:
    print("Anwer")
    print("true")
else:
    print("Answer")
print("false")

'''
测试3
这里print("true")的缩进错误，使其不属于if的代码块中，由于if else必须联合使用，所以报错
if _As == 1:
    print("Anwer")
print("true")
else:
    print("Answer")
    print("false")
'''

item_1 = 1
item_2 = 2
item_3 = 3

sum = item_1 + item_2 + item_3
print(sum)
sum_2 = item_1 + \
        item_2 + \
        item_3
print(sum_2)

print("四种数字类型")
i = 1
b = False
f = 1.23
c1 = 1 + 2j
c2 = 2 + 3j

print("整数类型")
print(i)
print("布尔类型")
print(b)
print("浮点类型")
print(f)
print("复数类型")
print(c1 + c2)

print('字符串类型')
s1 = '字符串1'
print(s1)
s2 = '''字符串2
        字符串2
        字符串2'''
print(s2)
print('字符串3\n')
print(r'字符串4\n')

s3 = '字符串5' + 'tab 字符串5'
print(s3)
s4 = '字符串6 ' * 3
print(s4)

s5 = '0123456789'
#s5[0] = 1 Python中的字符串是不可进行改变的
#从左向右遍历的索引方式是0、1、2……
print(s5[0])
#从右向左遍历的索引方式是-1、-2、-3……，也就是-1是最后一个字符，-2则是倒数第二个字符……
print(s5[-1])
print(s5[-2])
#可以使用str[start:end]来进行字符串的切片，前闭后开,可以留空
print(s5[0:2])
print(s5[:-2])
print(s5[2:])
#start > end的切片方式是允许的，但是返回的是一个空的序列
s6 = s5[1:0]
print(s6)
#可以加上步长参数
print(s5[1:8:2])

none1 = None
print(none1)
none2 = None
print(none2)
print(none1 is none2)