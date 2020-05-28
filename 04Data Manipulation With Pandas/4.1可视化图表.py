# --------条形图----------------
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
# 返回pandas序列
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()  # 根据某列先分类 再选出元素

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")   # 绘制直方图

# Show the plot
plt.show()   # 显示图表


# --------折线图(反应变量随时间变化的规律)--------------------
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
# 根据日期分类, 然后计算每天的销售数目
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind='line')  # 折线图

# Show the plot
plt.show()

# 结果: https://pic.rmb.bdstatic.com/bjh/12343b62a070f5f3878356b431c1cafa.png


# --------散点图(判断两变量是否相关)--------------------
# Scatter plot of nb_sold vs avg_price with title
# 设置图表的x, y轴数据, 图表类型为散点图, 标题
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()  # 价格和销量的关系

# 结果: https://pic.rmb.bdstatic.com/bjh/abbb734662e2abb8d8e0d5f66c829409.png


# --------直方图--------------------
# Histogram of conventional avg_price 
avocados[avocados["type"] == "conventional"]["avg_price"].hist()  # 绘制直方图

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist()

# Add a legend
plt.legend(["conventional", "organic"])   #.legend([])  list  放置图例

# Show the plot
plt.show()


# 设置透明度
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

# 设置块大小 bins
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# 结果: https://pic.rmb.bdstatic.com/bjh/f083723bc01527d32ca6c79f03bf4021.png