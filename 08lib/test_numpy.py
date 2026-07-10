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


def _main():
    # test_np_where()
    test_np_argmax()


if __name__ == '__main__':
    _main()
