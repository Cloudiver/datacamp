# ----------统计信息--------------
# Print the head of the sales DataFrame
print(sales.head())   # 输出前五行内容

# Print the info about the sales DataFrame
print(sales.info())   # DataFrame列信息

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())   # 平均数

# Print the median of weekly_sales
print(sales['weekly_sales'].median())   # 中位数



# Print the maximum of the date column
print(sales['date'].max())   # 最大值

# Print the minimum of the date column
print(sales['date'].min())  # 最小值


# A custom IQR function    # 四分位数
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
    
# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))   # 调用agg()方法


# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))   # 传入列表, 输出多个值


# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
# .agg()函数传入列表   分别计算iqr, 和中位数的值, agg()相当于调用了两个函数 ,一个是自己定义的, 另一个是内置函数
# .agg() 用一个函数计算多个列的多个统计值
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))  


# ----------累加值--------------
# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values('date')   # 排序

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()   # 返回累加值

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()  # 返回累积最大值  取得最大值后保存, 然后依次和后面的值比较

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])



# -----------删除重复值-----------------
# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=('store', 'type'))   # 根据 store 和 type 来去除重复值
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=('store', 'department'))
print(store_depts.head())

# Subset the rows that are holiday weeks and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates(subset='date')  # 根据一列去除重复值

# Print date col of holiday_dates
print(holiday_dates['date'])



# -----------统计元素个数-----------------
# Count the number of stores of each type
store_counts = stores["store_type"].value_counts()   # 统计store_type列中相同元素的个数
print(store_counts)

# Get the proportion of stores of each type
store_props = stores["store_type"].value_counts(normalize=True)  # 将统计个数计算百分比
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = departments["department_num"].value_counts(sort=True)  # 统计个数按降序排列
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = departments["department_num"].value_counts(sort=True, normalize=True)  # 统计个数计算为百分比, 然后降序排列
print(dept_props_sorted)