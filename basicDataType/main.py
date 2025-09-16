#python中的变量声明不需要显式指定类型
#定义变量的时候必须同时进行赋值

i = 1
b = True
f = 1.00
c = 1 + 2j
#输出数据的类型
print(type(i))
print(type(b))
print(type(f))
print(type(c))

#同时为多个变量赋值
#可以将多个变量赋值为相同的数值
a = b = c = 1
print(a, b, c)

#可以分别为多个变量赋值
m, n, k = 1, True, 1.0
print(m, n, k)



