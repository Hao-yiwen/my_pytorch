import numpy as np
import matplotlib.pyplot as plt

# 使用numpy实现向量乘法
x = np.array([1, 2, 3, 4, 5])
w = np.array([0.2, 0.4, 0.6, 0.8, 1.0])

f = np.dot(x, w)
print(f)

# python基础语法

a1 = 5
a2 = "hello, world"
a3 = 10  # int类型
a4 = True  # bool类型
a5 = "python"  # 字符串
a6 = [1, 2, 3, 4];  # 列表 容许重复元素和增删改 可以通过索引访问
a7 = (1, 2, 3, 4);  # 元组 不容许增删改 可以通过索引访问
a8 = {10, 2, 3, 4};  # 集合 不容许重复元素 可以增删改 不能通过索引访问
a8.add(5)

a9 = {"name": "张三", "age": 18};  # 字典

# 条件语句
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# 循环
print("=======循环======")
for i in range(5):
    print(i)

print("=======while循环======")
count = 0
while count < 5:
    print(count)
    count += 1

# 函数
def add(a,b):
    return a+b
result = add(1,2)
print("=======函数======")
print(result)

# 类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("wangwang")
        print("my name is", self.name)

my_dog = Dog("Rex", 2)
print("=======类======")
my_dog.bark()
print(my_dog.name)

# 列表操作
my_list = [1,2,3,4,5]
print(my_list[0])

my_list.append(6)
print(my_list)

my_list.remove(3)
print(my_list)

for i in my_list:
    print(i)

# 字典操作
my_dict = {"name": "张三", "age": 18}

print(my_dict["name"])

my_dict["name"] = "李四"
print(my_dict)

my_dict["city"] = "北京"
print(my_dict)

for key,value in my_dict.items():
    print(key, value)

# 文件操作
with open("example.txt", "w") as file:
    file.write("hello, world")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 异常处理
try:
    result = 10/0
except Exception:
    print("division by zero")
finally:
    print("this is always executed")

# 列表推导
squares = [i**2 for i in range(10)]
print(squares)

import time
# 迭代器
def countdown(n):
    print("counting down from", n)
    while n > 0:
        # 延时2000ms
        time.sleep(2)
        yield n
        n -= 1

for i in countdown(5):
    print(i)

# 模块和包
import math

print(math.sqrt(16))

# 画图
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 绘制3D曲面图
ax.plot_surface(X, Y, Z, cmap='viridis')

plt.show()
