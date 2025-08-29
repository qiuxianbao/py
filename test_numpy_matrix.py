
import numpy as np
# 参考资料：https://www.hahack.com/math/math-matrix

# 例子
# a = np.matrix([[5,2,7],[1,3,4]])
# a = np.matrix('5 2 7;1 3 4')

# b = np.matrix([[5,2,7,6],[1,3,4,2],[8,2,-2,3]])
# b = np.matrix('5 2 7 6;1 3 4 2;8 2 -2 3')

# print(type(a)) # <class 'numpy.matrix'>
# b = a.getA()
# print(type(b)) # <class 'numpy.ndarray'>

# print(a[1,1]) # 1


# 运算
a = np.matrix('1 0 1;1 2 1;2 1 1')
# print(a)
# [[1 0 1]
#  [1 2 1]
#  [2 1 1]]


b = np.matrix('2 1 -1;0 -1 2;2 -1 0')
# print(b)
# [[ 2  1 -1]
#  [ 0 -1  2]
#  [ 2 -1  0]]

# print(a + b)  # 两个矩阵的行数和列数必须相同，否则无定义
# print(a - b)  # 两个矩阵的行数和列数必须相同，否则无定义

# print(a * b)
# [[ 4  0 -1]
#  [ 4 -2  3]
#  [ 6  0  0]]

# print(b * a)    # a * b ≠ b * a
# [[ 1  1  2]
#  [ 3  0  1]
#  [ 1 -2  1]]

# c = np.matrix('5 7 2;4 3 1')
# d = np.matrix('1;5;6')
# print(c * d)
# [[52]
#  [25]]

# a * b * d = a * (b * d)


# 创建一个3阶【单元矩阵】
# 它的一个特性是与其他矩阵相乘都等于那个矩阵本身

# I = np.eye(3)
# print(I)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# print(a*I)
# [[1. 0. 1.]
#  [1. 2. 1.]
#  [2. 1. 1.]]


# 创建一个3阶 【零矩阵】
# z = np.full((3, 3), 0)
# print(z)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

# print(a * z)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

# print(b * z)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]


# 除（求逆）
# print(a.I)

# 转置
a = np.matrix('2 4;1 3')
print(a)
# [[2 4]
#  [1 3]]

print(a.T)  #矩阵的行变成了列
# [[2 1]
#  [4 3]]

b = np.matrix('1 2 3;4 5 6')
print(b.T)  #矩阵的行变成了列
# [[1 4]
#  [2 5]
#  [3 6]]


a = np.matrix('2 4;1 3')
b = np.matrix('1 6;2 5')
# print(a*b)
# [[10 32]
#  [ 7 21]]

# print(b.T*a.T)      #(a*b)T = (b.T*a.T)
# [[10  7]
#  [32 21]]


# 示例
a = np.matrix('3 2; -1 1')
b = np.matrix('7; 1')

# print(np.linalg.solve(a, b))    # 算法库，解线性方程组
# [[1.]
#  [2.]]
