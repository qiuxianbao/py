import matplotlib.pyplot as plt
import numpy as np


print("######### demo1：plt.show #########")
"""
生成数据
"""
x = np.arange(0, 6, 0.1) # 以0.1为单位，生成0到5.9(不包含6)的数据
y1 = np.sin(x)
y2 = np.cos(x)

# # 绘制图形
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--",label="cos") # 使用虚线绘制
plt.xlabel("x") # x轴标签
plt.ylabel("y") # y轴标签
plt.title("sin & cos") # 标题

plt.legend() # 图例
# plt.show()


print("######### demo2：plt.imshow #########")
"""
读取图片
"""
from matplotlib.image import imread

#(dl) PS C:\VsCode\py> python .\test_matplotlib.py
# 命令在哪里执行，哪里就是根目录
img = imread('images/matplotlib/deepseek.png')

plt.imshow(img)
plt.show()
