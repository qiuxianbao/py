import numpy as np

"""
Python等动态类型语言一般比C和C++等静态类型语言（编译型语言）运算速度慢。实际上，如果是运算量大的处理对象，用 C/C++写程序更好。
为此，当 Python中追求性能时，人们会用 C/C++来实现处理的内容。
Python则承担“中间人”的角色，负责调用那些用 C/C++写的程序。NumPy中，主要的处理也都是通过C或C++实现的。
"""

"""
数学上将一维数组称为向量，将二维数组称为矩阵。另外，可以将一般化之后的向量或矩阵等统称为张量（tensor）
"""


def test_array_one_dim():
    # 一维数组
    print("######### demo1：一维数组 np.array #########")
    x = np.array([1.0, 2.0, 3.0])
    # [1. 2. 3.]
    print(x)
    # <class 'numpy.ndarray'>
    print(type(x))

    # 运算
    y = np.array([2.0, 4.0, 6.0])
    # [3. 6. 9.]
    print(x + y)
    # [-1. -2. -3.]
    print(x - y)
    # [ 2.  8. 18.]
    print(x * y)
    # [0.5 0.5 0.5]
    print(x / y)

    # [0.5 1.  1.5]
    print(x / 2)


def test_array_two_dim():
    print("######### demo2：N维数组 np.array #########")
    A = np.array([[1, 2], [3, 4]])

    # [[1 2]
    #  [3 4]]
    print(A)
    # 2
    print(A.ndim)  # 维度
    # (2, 2)
    print(A.shape)  # 形状
    # int64
    print(A.dtype)

    B = np.array([[3, 0], [0, 6]])

    # [[4 2]
    #  [3 10]]
    print(A + B)

    similar_songs_array = np.array([
        ('song_A', 0.95),  # (歌曲名, 相似度分数)
        ('song_B', 0.87),
        ('song_C', 0.82),
        ('song_D', 0.78),
        ('song_E', 0.75)
    ])

    # ['song_A' 'song_B' 'song_C' 'song_D' 'song_E']
    print(similar_songs_array[:, 0])


def test_array_broadcast():
    print("######### demo3：广播 #########")
    """
    在2×2的矩阵A和标量10之间进行了乘法运算
    标量10被扩展成了2 × 2的形状，然后在与矩阵A进行乘法运算。这个巧妙的功能称为广播（broadcast）
    """

    # [[10 20]
    #  [30 40]]
    A = np.array([[1, 2], [3, 4]])
    print(A * 10)

    A = np.array([[1, 2], [3, 4]])
    B = np.array([10, 20])
    # [[10 40]
    #  [30 80]]
    print(A * B)


def test_array_slip():
    print("######### demo4：访问元素 #########")
    X = np.array([[51, 55], [14, 19], [0, 4]])
    print(X)

    # [51 55]
    print(X[0])
    # 55
    print(X[0, 1])

    for row in X:
        print(row)

    # 矩阵变平转数组
    X = X.flatten()
    print(X)  # [51 55 14 19  0  4]

    print(X[np.array([0, 1, 2])])

    """
    抽取数据
    对NumPy数组使用不等号运算符等（上例中是X > 15）,结果会得到一个布尔型的数组。
    """
    # [ True  True False  True False False]
    print(X > 15)
    # [51 55 19]
    print(X[X > 15])


def test_array_exp():
    """
    指数函数
    """
    print("######### 指数函数 np.exp #########")
    # 1.0
    print(np.exp(0))
    # 2.718281828459045
    print(np.exp(1))
    arr = np.array([0, 1, 2, 3])
    # [ 1.          2.71828183  7.3890561  20.08553692]
    print(np.exp(arr))


def test_array_algorithms():
    print("######### 点积-(向量 dot 向量) np.dot #########")
    """
    # 计算公式
    ## 1.向量点积 (两两相乘 再 相加)
    对于两个 n 维向量 a 和 b：
    a = [a₁, a₂, ..., aₙ]
    b = [b₁, b₂, ..., bₙ]

    a · b = a₁b₁ + a₂b₂ + ... + aₙbₙ = Σ(aᵢ × bᵢ)
    """
    # a = np.array([-1, 2])
    # b = np.array([3, 1])

    # print(a + b)  #[2 3]
    # print(a - b)  #[-4  1]
    # print(a * 3)  #[-3  6]

    # 点积
    a = np.array([3, 5, 2])
    b = np.array([1, 4, 7])

    # print(a.dot(b))  # 37
    print(np.dot(a, b))  # 37

    print("######### 点积-(矩阵 dot 向量) np.dot #########")
    """
    # 计算公式
    ## 2.矩阵与向量点积
    A (m×n) · b (n×1) = c (m×1)
    
    例如：
    ┌1  2┐   ┌7┐   ┌1×7 + 2×8┐   ┌23┐
    │3  4│ · │8│ = │3×7 + 4×8│ = │53│
    └5  6┘         └5×7 + 6×8┘   └83┘
    
    ## 3.矩阵与矩阵点积
    C = A (m×n) · B (n×p) → C (m×p)
    C[i,j] = Σ(A[i,k] × B[k,j])  for k=0 to n-1

    # 几何意义
            b
           ↗
          /|
         / |
        /  |
       /θ  |
      a----→
    
    a · b = |a| × |b| × cos(θ)
    
    # 实际应用：
    相似度计算：余弦相似度 = (a·b) / (|a|×|b|)
    投影长度：向量 a 在 b 上的投影 = (a·b) / |b|
    判断方向关系：点积正负判断前后/左右关系
    """
    A = np.array([[1, 2], [3, 4], [5, 6]])

    B = np.array([7, 8])
    print(B.shape)

    # ValueError: shapes (2,) and (3,2) not aligned: 2 (dim 0) != 3 (dim 0)
    # print(np.dot(B, A))

    """
    一维数组 B = np.array([7, 8]) 具有特殊的灵活性, 它的 shape 是 (2,)
    它【不是】行向量（shape 应该是 (1, 2)）
    也【不是】列向量（shape 应该是 (2, 1)），它只是一个纯粹的一维数组（Vector）

    当它放在不同的位置时，NumPy 会自动将其视作不同的维度，
    (1) 放在右边时：视作【列向量】（维度 2 x 1）参与计算
    (2) 放在左边时：视作行向量（维度 1 x 2）

    np.dot(A, B)的计算结果确实是列向量[[23],[53],[83]],维度为 (3, 1)
    计算完成后，NumPy 会自动把结果的最后一个维度压缩掉，重新还原成一维数组。所以它的 shape 变成了 (3,)
    """
    # [23 53 83]
    print(np.dot(A, B))

    print("######### 差积(矩阵 cross 向量) np.cross #########")
    """
    # 差积（仅用于3D向量）
    ## 计算公式
    a = [a₁, a₂, a₃]
    b = [b₁, b₂, b₃]
    
    a × b = [a₂b₃ - a₃b₂,  a₃b₁ - a₁b₃,  a₁b₂ - a₂b₁]
    
    行列式形式（便于记忆）：
            | i   j   k  |
    a × b = | a₁  a₂  a₃ |
            | b₁  b₂  b₃ |
    
    = i(a₂b₃ - a₃b₂) - j(a₁b₃ - a₃b₁) + k(a₁b₂ - a₂b₁)
    
    ## 几何意义
                a × b (垂直于纸面向外)
                ↑
                |
                |
        b ↗    /|
          \   / |
           \ /  |
            O---→ a
            
    a × b 垂直于 a 和 b 构成的平面
    
    核心特性：
    1.方向：垂直于 a 和 b 所在的平面，遵循右手定则
        右手四指从 a 转向 b，拇指指向即为 a×b 方向
    2.模长：|a × b| = |a| × |b| × sin(θ)
        等于以 a、b 为邻边的平行四边形面积
    3.反交换律：a × b = -(b × a) （方向相反）
    
    """
    a = np.array([3, 5, 2])
    b = np.array([1, 4, 7])

    # print(np.cross(a, b))  # [27, -19, 7]

    # 投影
    def get_projection(a, b):
        return a.dot(b) * 1.0 * b / b.dot(b)

    # a = np.array([1, 2])
    # b = np.array([2, 2])
    # print(get_projection(a, b))  # [1.5  1.5]

    a = np.array([[1, 2]])
    # [[1]
    #  [2]]
    # print(a.T)

    # 最小二乘逼近、 线性回归
    a = np.array([[1, 1], [1, -1], [0, 1]])
    b = np.array([3, -2, 1])

    # least - squares
    x = np.linalg.lstsq(a, b)

    # 解，残差，秩，奇异值
    # (array([0.5, 2. ]), array([1.5]), 2, array([1.73205081, 1.41421356]))
    print(x)


def _main():
    # test_array_one_dim()
    # test_array_two_dim()
    # test_array_broadcast()
    # test_array_slip()
    # test_array_exp()
    test_array_algorithms()


if __name__ == '__main__':
    _main()
