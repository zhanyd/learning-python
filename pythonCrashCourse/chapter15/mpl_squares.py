import matplotlib.pyplot as plt
import matplotlib

plt.style.use('seaborn')

# 设置matplotlib支持中文字符
matplotlib.rcParams['font.family'] = 'SimHei'  # 'SimHei' 是一种常用的中文黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号'-'显示为方块的问题

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)
ax.plot(input_values, squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize = 24)
ax.set_xlabel("值", fontsize = 14)
ax.set_ylabel("平方的值", fontsize = 14)

# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize = 14)

plt.show()