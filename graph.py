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

df1 = pd.read_excel(
    'C:/Users/海棠微雨/Desktop/C题/附件2.xlsx',
    sheet_name='Sheet1',
    header=0,  # 第一行作为列名
    usecols='A:G',  # 读取 A 到 D 列
    index_col=None,  # 第一列作为行索引
    skiprows=0,  # 不跳过
    nrows=None  # 读取所有 行
)

encoder = df['单品编码']
name = df['分类名称']

# 使用 zip() 函数将两个列表合并为一个字典
my_dict = dict(zip(encoder, name))

encoder1 = df1['单品编码']
date = df1['扫码销售时间']
Sales_status = df1['销售类型']

my_dict1 = dict(zip(date, encoder1))
first_key, first_value = next(iter(my_dict1.items()))
print(first_key, first_value)

# # 绘制多线图
# plt.figure(figsize=(10, 6))
# for column in df.columns[1:]:
#     plt.plot(df['时间'], df[column], label=column)

# # 添加图例
# plt.legend(loc='upper left')

# # 添加标题和标签
# plt.title('多线图示例')
# plt.xlabel('时间')
# plt.ylabel('数值')

# # 显示图形
# plt.show()
