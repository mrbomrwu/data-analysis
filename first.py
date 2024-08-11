import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel(
    'C:/Users/海棠微雨/Desktop/C题/附件1.xlsx',
    sheet_name='Sheet1',
    header=0,  # 第一行作为列名
    usecols='A:D',  # 读取 A 到 D 列
    index_col=None,  # 第一列作为行索引
    skiprows=0,  # 跳过第一行
    nrows=None  # 读取前 10 行
)
print(df)
print(type(df))
print(df['分类'].head())
# # 数据
# labels = ['花叶类', '花菜类', '辣椒类', '茄类', '食用菌', '水生根茎类']
# sizes = [A, B, C, D, E, F]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0.05, 0.1, 0.05)  # 仅"爆炸"第一个扇区

# # 绘制饼状图
# plt.figure(figsize=(8, 8))
# plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140, shadow=True)

# # 设置标题
# plt.title('Pie Chart with Exploded Slice')

# # 添加图例
# plt.legend(labels, loc="best")

# # 显示图形
# plt.show()

