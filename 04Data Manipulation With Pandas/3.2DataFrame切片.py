# -------------根据索引进行切片------------
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()   # 必须先对索引进行排序

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc['Pakistan':'Russia'])  # 首尾都包含在内

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc['Lahore':'Moscow'])  # 返回混乱的数据

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[('Pakistan', 'Lahore'):('Russia', 'Moscow')])  # 传入元组, 必须匹配元组中的内容
# 选择country = Pakistan, city = Lahore  和  country = Russia, city = Moscow


# -------------根据索引(二级索引)进行切片------------
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad')])   # 传入元组 

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,'date':'avg_temp_c'])  # 所有行, date 到 avg_temp_c列

# Subset in both directions at once
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad'),'date':'avg_temp_c'])
# 根据行和列选择 


# -------------根据时间进行切片------------
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
print(temperatures[(temperatures["date"] >= "2010") & (temperatures["date"] < "2012")])  # 根据布尔条件来判断

# Set date as an index
temperatures_ind = temperatures.set_index("date")

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])  # 默认时间是 2010-01-01~2011-01-01

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])


# -------------根据数字索引(iloc)进行切片------------
# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22,1])   # [x, y] 获取元素值

# Use slicing to get the first 5 rows
print(temperatures.iloc[0:5])   # [起始行, 终止行]  终止行不包含在内

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])  # 所有行的 3, 4列

# Use slicing in both directions at once
print(temperatures.iloc[0:5, 2:4])  # 0~4行, 3, 4列