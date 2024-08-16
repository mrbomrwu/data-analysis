import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 给定的 y 值
y = [1, 2, 5, 8, 9, 7]
x = np.arange(len(y))  # x 轴的索引值

# 创建插值函数
f = interp1d(x, y, kind='cubic')

# 生成更多的 x 值
x_smooth = np.linspace(0, len(y)-1, 500)
y_smooth = f(x_smooth)

# 绘制曲线
plt.plot(x_smooth, y_smooth)
plt.scatter(x, y, color='red')  # 标出原始点
plt.title("Smooth Curve")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
