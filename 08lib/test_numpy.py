import numpy as np


def test_np_where():
    """
    基础用法：返回满足条件的索引
    :return:
    """
    arr = np.array([10, 20, 30, 40, 50, 30, 60])
    indices = np.where(arr == 30)
    # <class 'tuple'>，注意逗号，是单元素元组
    print(type(indices))
    # 1
    print(len(indices))
    # (array([2, 5], dtype=int64),)
    print(f"元素等于30的索引: {indices}")
    # [2 5]
    print(f"元素等于30的索引 0: {indices[0]}")

    """
    二维数组中的条件索引
    """
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    #
    two_dim = np.where(matrix > 5)
    # 二维数组中的条件索引: (array([1, 2, 2, 2], dtype=int64), array([2, 0, 1, 2], dtype=int64))
    print(f"二维数组中的条件索引: {two_dim}")
    # 二维数组中的条件索引 0 : [1 2 2 2]
    print(f"二维数组中的条件索引 0 : {two_dim[0]}")
    # 二维数组中的条件索引 1: [2 0 1 2]
    print(f"二维数组中的条件索引 1: {two_dim[1]}")

    row, col = np.where(matrix > 5)
    # 输出: 大于5的元素位置: 行=[1 2 2 2], 列=[2 0 1 2]
    print(f"大于5的元素位置: 行={row}, 列={col}")

    """
    条件替换（类似三目运算）
    """
    scores = np.array([55, 78, 92, 45, 88, 60])
    result = np.where(scores >= 60, "及格", "不及格")
    # 输出: 成绩结果: ['不及格' '及格' '及格' '不及格' '及格' '及格']
    print(f"成绩结果: {result}")

    """
    多条件组合
    """
    values = np.array([12, 25, 8, 42, 33, 17])
    mask = np.where((values > 10) & (values < 30))
    print(f"介于10和30之间的值索引: {mask}, 值: {values[mask]}")
    # 输出: 介于10和30之间的值索引: (array([0, 1, 5], dtype=int64),), 值: [12 25 17]

    """
    最实用的场景：配合聚类结果使用
    """
    clusters = np.array([2, 0, 1, 0, 0, 2, 1, 1, 0, 2])

    # 找出所有属于簇0的元素
    cluster_0_indices = np.where(clusters == 0)[0]

    # 输出: 簇0的元素原始位置: [1 3 4 8]
    print(f"\n簇0的元素原始位置: {cluster_0_indices}")

    # 取前2个，类似书本里的用法
    for i, idx in enumerate(cluster_0_indices[:2]):
        # 输出:  簇0第1个元素 -> 原数组第1个位置
        #       簇0第2个元素 -> 原数组第3个位置
        print(f"  簇0第{i + 1}个元素 -> 原数组第{idx}个位置")


def test_np_argmax():
    """
    寻找最大值的索引位置
    :return:
    """
    # 3个类别的预测得分（或概率）
    scores = np.array([0.15, 0.72, 0.13])

    # 寻找最大值的索引
    best_class = np.argmax(scores)

    print("最大值的索引位置是:", best_class)
    # 输出: 1  （因为 0.72 最大，排在索引 1 的位置）

    # 映射回具体标签
    labels = ["科技", "体育", "娱乐"]
    print("预测的类别是:", labels[best_class])


def test_np_argmax_axis():
    import numpy as np

    # 模拟 3 张图片在 4 个类别上的得分矩阵
    y_batch = np.array([
        [0.1, 0.8, 0.05, 0.05],  # 图片 0 的得分 (最大值是 0.8，在索引 1)
        [0.2, 0.1, 0.6, 0.1],  # 图片 1 的得分 (最大值是 0.6，在索引 2)
        [0.7, 0.1, 0.1, 0.1]  # 图片 2 的得分 (最大值是 0.7，在索引 0)
    ])

    """
    axis=1 横向扫描（从左到右），看的是列
    [0.1, 0.8, 0.05, 0.05]  ──横向找最大──> 0.8 (索引 1)
    [0.2, 0.1, 0.6,  0.1 ]  ──横向找最大──> 0.6 (索引 2)
    [0.7, 0.1, 0.1,  0.1 ]  ──横向找最大──> 0.7 (索引 0)
    """
    p_row = np.argmax(y_batch, axis=1)
    print(p_row)  # [1 2 0]

    """
    axis=0 纵向扫描（从上到下），看的是行
      ↓    ↓    ↓    ↓
    [0.1, 0.8, 0.05, 0.05]
    [0.2, 0.1, 0.6,  0.1 ]
    [0.7, 0.1, 0.1,  0.1 ]
      │    │    │    │
      │    │    │    └─ 纵向最大 0.1 (第 1 行和第 2 行并列，返回第一个遇到的索引 1)
      │    │    └─ 纵向最大 0.6 (在第 1 行 -> 索引 1)
      │    └─ 纵向最大 0.8 (在第 0 行 -> 索引 0)
      └─ 纵向最大 0.7 (在第 2 行 -> 索引 2)
    """
    p_col = np.argmax(y_batch, axis=0)
    print(p_col)  # [2, 0, 1, 1]


def test_np_zeros():
    """
    用来创建全零数组（矩阵）的函数
    :return:
    """

    print(np.zeros(2))  # [0. 0.]

    """
    [[0. 0. 0.]
    [0. 0. 0.]]
    """
    # 创建一个 2 行 3 列的二维全零矩阵
    print(np.zeros((2, 3)))

    # 指定数据类型
    print(np.zeros(2, dtype=int))  # [0 0]


def _main():
    # test_np_where()
    # test_np_argmax()
    test_np_argmax_axis()
    # test_np_zeros()


if __name__ == '__main__':
    _main()
