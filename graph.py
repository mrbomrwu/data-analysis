import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 示例数据
data = {
    '时间': ['2020Q3', '2020Q4', '2021Q1', '2021Q2', '2021Q3', '2021Q4', '2022Q1', '2022Q2', '2022Q3', '2022Q4', '2023Q1', '2023Q2'],
    '花菜类': [100, 150, 200, 250, 300, 250, 200, 150, 100, 50, 0, 50],
    '花叶类': [50, 100, 150, 200, 250, 300, 250, 200, 150, 100, 50, 0],
    '辣椒类': [0, 50, 100, 150, 200, 250, 300, 250, 200, 150, 100, 50],
    '茄类': [50, 0, 50, 100, 150, 200, 250, 300, 250, 200, 150, 100],
    '食用菌': [100, 50, 0, 50, 100, 150, 200, 250, 300, 250, 200, 150],
    '水生根茎类': [150, 100, 50, 0, 50, 100, 150, 200, 250, 300, 250, 200]
}

df = pd.DataFrame(data)

# 绘制多线图
plt.figure(figsize=(10, 6))
for column in df.columns[1:]:
    plt.plot(df['时间'], df[column], label=column)

# 添加图例
plt.legend(loc='upper left')

# 添加标题和标签
plt.title('多线图示例')
plt.xlabel('时间')
plt.ylabel('数值')

# 显示图形
plt.show()
