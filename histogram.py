import matplotlib.pyplot as plt

# 示例数据
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 2]

# 绘制柱状图
plt.bar(categories, values)

# 添加标题和标签
plt.title('示例柱状图')
plt.xlabel('类别')
plt.ylabel('值')

# 显示图表
plt.show()
