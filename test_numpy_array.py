import numpy as np


"""
Python等动态类型语言一般比C和C++等静态类型语言（编译型语言）运算速度慢。实际上，如果是运算量大的处理对象，用 C/C++写程序更好。
为此，当 Python中追求性能时，人们会用 C/C++来实现处理的内容。
Python则承担“中间人”的角色，负责调用那些用 C/C++写的程序。NumPy中，主要的处理也都是通过C或C++实现的。
"""

"""
数学上将一维数组称为向量，将二维数组称为矩阵。另外，可以将一般化之后的向量或矩阵等统称为张量（tensor）
"""
# 一维数组
print("######### demo1：一维数组 #########")
x = np.array([1.0, 2.0, 3.0])
# [1. 2. 3.]
print(x)
# <class 'numpy.ndarray'>
print(type(x))

# 运算
y = np.array([2.0, 4.0, 6.0])
# [3. 6. 9.]
print(x+y)
# [-1. -2. -3.]
print(x-y)
# [ 2.  8. 18.]
print(x*y)
# [0.5 0.5 0.5]
print(x/y)

# [0.5 1.  1.5]
print(x/2)


print("######### demo2：N维数组 #########")
A = np.array([[1, 2], [3, 4]])

# [[1 2]
#  [3 4]]
print(A)

# (2, 2)
print(A.shape)
# int64
print(A.dtype)

B = np.array([[3, 0], [0, 6]])

# [[4 2]
#  [3 10]]
print(A+B)


print("######### demo3：广播 #########")
"""
在2×2的矩阵A和标量10之间进行了乘法运算
标量10被扩展成了2 × 2的形状，然后在与矩阵A进行乘法运算。这个巧妙的功能称为广播（broadcast）
"""

# [[10 20]
#  [30 40]]
A = np.array([[1, 2], [3, 4]])
print(A*10)


A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
# [[10 40]
#  [30 80]]
print(A*B)



print("######### demo4：访问元素 #########")
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)

# [51 55]
print(X[0])
# 55
print(X[0, 1])

for row in X:
    print(row)

X = X.flatten()
print(X)

print(X[np.array([0, 1, 2])])

"""
抽取数据
对NumPy数组使用不等号运算符等（上例中是X > 15）,结果会得到一个布尔型的数组。
"""
# [ True  True False  True False False]
print(X > 15)
# [51 55 19]
print(X[X>15])



# 向量
# a = np.array([-1, 2])
# b = np.array([3, 1])

# print(a + b)  #[2 3]
# print(a - b)  #[-4  1]
# print(a * 3)  #[-3  6]


# 点积
# a = np.array([3, 5, 2])
# b = np.array([1, 4, 7])

# print(a.dot(b))  # 37
# print(np.dot(a, b)) #37


# 投影
def get_projection(a, b):
    return a.dot(b)*1.0*b/b.dot(b)

# a = np.array([1, 2])
# b = np.array([2, 2])
# print(get_projection(a, b))  # [1.5  1.5]


# 差积
a = np.array([3, 5, 2])
b = np.array([1, 4, 7])
# print(np.cross(a, b))  # [27, -19, 7]


a = np.array([[1, 2]])
# [[1]
#  [2]]
# print(a.T)


# 最小二乘逼近、 线性回归
a = np.array([[1, 1], [1, -1], [0, 1]])
b = np.array([3, -2, 1])
x = np.linalg.lstsq(a,b)

# 解，残差，秩，奇异值
# (array([0.5, 2. ]), array([1.5]), 2, array([1.73205081, 1.41421356]))
print(x)
