# ***** 字符编码方式 *****

# python工程文件存储时，使用的是哪种编码，打开时就需要使用相同的编码，否则就会乱码。
# 字符底层存储时，本质上都是0101010101010101二进制。
# 字符和二进制的对应关系（编码）：
# 	- ascii编码，256个对应关系。【即标准键盘上的符号】 【1个字节】
# 	- gb2312，gbk，包含了中文和亚洲的一些国家文字的编码。【中文是2个字节，如下例】
# 	- unicode编码，分ucs2/ucs4，包括现在发现的所有文明。【分2个字节和4个字节两种形式】。
# 	- utf-8编码，【每个字符的字节数根据情况来定，中文用个3字节，如下例】
	
# Python默认解释器编码(utf-8)
# python.exe  xxx.py     # xxx.py默认应该是utf-8编码
# 如果将代码文件保存成了gbk编码，须将Python工程文件解释器编码修改成gbk，即在开头声明
# 以下声明对windows没有用，就像注释。(ch09 92~98有关联)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""字符串有.encode()属性"""
data1 = "a2/,<|"
res1 = data1.encode('utf-8')
res2 = data1.encode('gbk')
res3 = data1.encode('ascii')
print(res1)                   # b'a2/,<|'
print(res2)                   # b'a2/,<|'
print(res3)                   # b'a2/,<|'

data2 = '中'
res4 = data2.encode('utf8')   # 同utf-8
res5 = data2.encode('gbk')
print(res4)                   # b'\xe4\xb8\xad'
print(res5)                   # b'\xd6\xd0'

"""字符字节二进制有.decode()属性"""
data3 = b'\xe4\xb8\xad'
res6 = data3.decode('utf-8')
print(res6)                   # 中

data4 = b'\xd6\xd0'
res7 = data4.decode('gbk')
print(res7)                   # 中


# ***** 字符串格式化 *****

# 有3种方式: 1、 % 占位符()； 2､ .format占位； 3､ f解析


# 方式1: % (%c单个字符, %d整数, %e科学计数, %E, %f浮点数, %s字符串, %%百分号，……)

# 指定长度：%5d 右对齐，不足左边补空格；(23.8 --> '   23')
#         %-5d -代表左对齐，不足右边默认补空格；(23.8 --> '23   ', %-05d同样)
#         %05d 右对齐，不足左边补0. (23.8 --> '00023')

f0 = 23.8
print('%5d' % f0)                                           # 执行结果：   23
print('%05d' % f0)                                          # 执行结果：00023
print('%-5d' % f0)                                          # 执行结果：23   |
   
# 浮点数：%f 默认是输出6位有效数据，会进行四舍五入；
#       %.2f 保留小数点后2位；
#       %6.2f 6代表整个浮点数的长度，包括小数点和小数；2代表小数的位数
#             只有当字符串的长度大于6位才起作用，不足6位空格补足，可以用%06.2使用0补足空格

f1 = 1.987656789
print('%f' % f1)                                            # 执行结果：1.987657
print('%.2f' % f1)                                          # 执行结果：1.99
print('%6.2f' % f1)                                         # 执行结果：  1.99
print('%06.2f' % f1)                                        # 执行结果：001.99
print('%-06.2f' % f1)                                       # 执行结果：1.99  |

# \t 取table制表符的含义，用于对齐，就像\n一样，跟在任意字符后面都可以，试图保持4个空格一组
print('AAAAA %d\t BBB %s\t CC\t CC' % (8, 'X'))             # 执行结果：AAAAA 8  BBB X   CC      CC

# .isdigit() | 字符串专用方法，用来判断是不是数字型(得是整数，1.2或1 2都是False)字符串；
# .strip() | 去掉字符串首尾的空格，strip有撕掉包装的意思，在正则里面出现过；
# .split(',') | 以参数字符串为界，把字符串分割成多段，多段字符串构成一个列表；
s1 = r'and, your,  name,  hers,  are,same'
s2 = [item.strip() for item in s1.split(',')]

print('%% %c %d %.2e %.3f %s %%' % (65, 65, 65, 65, '65'))  # 执行结果：% A 65 6.50e+01 65.000 65 %
s3 = '%s' % 65                                              # 测试结果：65 <class 'str'>
s4 = '%%, %s, %s, %%' % (65, '65')                          # 测试结果：%, 65, 65, % <class 'str'>


# 方式2: .format占位

name = "可优"
lover = "柠檬小姐姐"
print("{}爱上了{}！".format(name, lover))

pi = 3.14159265359
print("圆周率（{:.5f}）有多长，爱你就有多深！".format(pi))

print("{:😍^20}".format("【爱的誓言】"))

self_info = {"name": "可优", "age": 17, "lover": "柠檬小姐姐"}
print("姓名: {name:💕<6}\n芳年: {age:💕<6}\n爱人: {lover:💕<6}".format(**self_info))

f2 = 'abc{2}xyz, efg{0}abc{1}efg'.format(100, 200, '300')   # 按index
print(f2.upper(), type(f2))

print('姓名是：{0:*^11}\n年龄是：{1:*>11}'.format('Tom', 20))


# 方式3: f解析

name = "可优"
lover = "柠檬"
sea = "🌊"
tortoise = "🐢"
print(f"{name}对{lover}的爱，犹如滔滔江水！{sea * 3}\n如果加一个期限，是{500+9500}年！{tortoise * 3}")

p = 23
q = '45'
r = f"abc{p}def,xyz{q}abc"
print(r.upper(), type(r))

self_info = {"name": "可优", "age": 17, "lover": "柠檬小姐姐"}
print(f"姓名: {self_info['name']}\n芳年: {self_info['age']}\n爱人: {self_info['lover']}")
