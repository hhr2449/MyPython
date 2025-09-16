# 基本语法

1. 标识符：开头必须是字母或是下划线，后面可以是字母、数字、下划线。注意标识符不能和保留字相同

2. 注释：使用`#`来表示注释，多行注释可以使用` ''' `,和“““

3. 缩进：python使用缩进来表示代码块，缩进的空格数是可变的，但是同一个代码块必须保持缩进相同，父语句块的缩进数必须小于子语句块，用于表示语句块的层次关系

   ![image-20250904203852392](https://raw.githubusercontent.com/hhr2449/pictureBed/main/img/image-20250904203852392.png)

4. 多行语句：可以使用`\`来分割多行语句

   ![image-20250904204121462](https://raw.githubusercontent.com/hhr2449/pictureBed/main/img/image-20250904204121462.png)

5. 数字类型：python中一共有四种数字类型：int、float、bool、complex

   1. int型没有区分短整型，长整型等，只有一种整数类型是int，对于较小的数据会使用4个字节来进行储存，大于4个字节则会自动调整
   2. float默认是双精度浮点数
   3. bool类型只有两个值就是False、True，注意和cpp不同的是python中的首字母要大写
   4. conplex类型是复数类型，表示为a + bi，可以进行对应的运算

6. 字符串类型

   1. python中没有单独的字符类型，单个字符也算作字符串

   2. 单引号和双引号的使用方法完全相同，都可以直接用于指定一个字符串

   3. 使用` ''' ` 和 ` """ `可以用于指定一个多行的字符串

   4. 类似cpp，使用` \ `可以进行转义

   5. 字符串前面加上r可以取消转义

      ![image-20250904223034582](https://raw.githubusercontent.com/hhr2449/pictureBed/main/img/image-20250904223034582.png)

      ![image-20250904223104370](https://raw.githubusercontent.com/hhr2449/pictureBed/main/img/image-20250904223104370.png)

   6. 使用`+`来连接两个字符串，使用`*`来重复字符串特定次数

      ```python
      s3 = '字符串5' + 'tab 字符串5'
      print(s3)
      s4 = '字符串6 ' * 3
      print(s4)
      '''
      字符串4\n
      字符串5tab 字符串5
      字符串6 字符串6 字符串6
      '''
      ```

      

   7. 字符串的索引方式

      1. 有从左到右和从右到左两种索引方式，从左到右的索引是0、1、2……，从右往左的索引是-1、-2、-3……
      2. 可以使用`str[start:end]`进行字符串的切片，前开后闭，可以留空
      3. 允许start >= end，但是会返回空的序列
      4. 可以指定步长

      ```python
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
      
      '''
      0
      9
      8
      01
      01234567
      23456789
      
      1357
      '''
      ```

7. NoneType：空类型，只有一个值：None，类似于cpp中的nullptr，但是python中的None是一个特殊的单例对象

   ```python
   none1 = None
   print(none1)
   none2 = None
   print(none2)
   print(none1 is none2)
   
   '''
   1357
   None
   None
   True
   '''
   ```

8. 输出：使用print()函数

   ```python
   #print输出函数
   #print函数可以接受多个变量，中间使用,进行分割
   #多个参数之间会自动加入空格，结束会自动输出\n
   print("test", s5[1:])
   #可以设置分隔符和结束符
   print("hello", "world", s5[1:], sep = ' 分割 ', end = ' 结束\n')
   
   """
   test 123456789
   hello 分割 world 分割 123456789 结束
   """
   ```

9. 输入：使用input()函数

   ```python
   #使用input()进行输入
   #可以在括号中添加提示信息
   #函数返回值是一个string，如果想要得到其他类型的数据需要进行显式的类型转换
   question = input('请输入你的问题')
   print(question)
   num = int(input("请输入一个数字"))
   print(num)
   
   '''
   请输入你的问题你好世界
   你好世界
   请输入一个数字10
   10
   '''
   ```

10. 可以使用`;`分割来实现同行内写多行语句`print('第一行语句');print('第二行语句');print('第三行语句')`

11. 模块导入

    可以使用import somemoduel来实现导入模块，使用from somemodule import来导入模块中的某些函数



# 运算符

## 算术运算符

其他的和cpp类似，有两个特殊的运算符：

1. `//`表示除法，但是结果会向下取整
2. `**`表示幂次

```python
#算术运算符
a = 10
b = 3
print(a // b)
print(a ** b)

'''
3
1000
'''
```

## 赋值运算符

```python
#赋值运算符
c = 10
c //= 3
print(c)
c **= 3
print(c)
if((d := 3) < 4):
    print(d)
    
'''
3
27
3
'''
```

只有三个是没有见过的：

1. `//=`就是整除再赋值
2. `**=`就是先取幂次再赋值
3. `:=`可以实现先赋值，再返回赋值的结果

## 逻辑运算符

逻辑运算符直接使用and or not来充当

```python
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

False
True
True

```



# 基本数据类型

