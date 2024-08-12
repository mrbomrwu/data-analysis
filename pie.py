import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.font_manager as fm

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

df = pd.read_excel(
    'C:/Users/海棠微雨/Desktop/C题/附件1.xlsx',
    sheet_name='Sheet1',
    header=0,  # 第一行作为列名
    usecols='A:D',  # 读取 A 到 D 列
    index_col=None,  # 第一列作为行索引
    skiprows=0,  # 不跳过
    nrows=None  # 读取所有 行
)
data = df['分类名称']
A, B, C, D, E, F = 0, 0, 0, 0, 0, 0
for i in data:
    if i == '花叶类':
        A += 1
    elif i == '花菜类':
        B += 1
    elif i == '辣椒类':
        C += 1
    elif i == '茄类':
        D += 1
    elif i == '食用菌':
        E += 1
    elif i == '水生根茎类':
        F += 1
# 数据
labels = ['花叶类', '花菜类', '辣椒类', '茄类', '食用菌', '水生根茎类']
sizes = [A, B, C, D, E, F]      #占比
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink']#颜色
explode = (0.02, 0.02, 0.02, 0.02, 0.02, 0.02)  # 让扇区裂开

# 绘制饼状图
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=140, shadow=False)

# 设置标题
plt.title('Pie Chart with Exploded Slice')

# 添加图例
plt.legend(labels, loc="best", bbox_to_anchor=(1.15, 1))

# 调整图形的布局，使图例不重叠
plt.tight_layout()

# 显示图形
plt.show()

