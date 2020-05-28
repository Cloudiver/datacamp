# ---------------缺少值处理----------
"""
通过isna()判断是否有数据为空
isna().any() 判断某一列是否有空
isna().sum()   计算每列中为空的总数目个数


.dropna()  将会删除有空值的行  (整行数据被删除)
.fillna(0)  用指定的0去补充没有值的位置
"""

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())  # 元素是否存在NaN值

# Check each column for missing values
print(avocados_2016.isna().any())  # 每列是否存在NaN值

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')  # 绘制条形图  统计每列的NaN数目
# Show plot
plt.show()


# Remove rows with missing values
avocados_complete = avocados_2016.dropna()  # 删除存在NaN的行

# Check if any columns contain missing values
print(avocados_complete.isna().any())   # 判断是否还有NaN值



# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist() # 分别绘制这三列的直方图

# Show the plot
plt.show()

# 结果: https://pic.rmb.bdstatic.com/bjh/8703a4ca164869176ae9176ff4001495.png


# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)  # 用0填充NaN值

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()  # 重新绘制三列

# Show the plot
plt.show()

#结果: https://pic.rmb.bdstatic.com/bjh/8c46240d336f5979f9e08141065a9f51.png