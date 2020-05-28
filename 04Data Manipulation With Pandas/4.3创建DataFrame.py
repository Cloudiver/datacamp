# ------创建DataFrame(手动创建)------------
"""
从字典/列表中创建DataFrame
DataFrame(list/dict)  
从行创建(list)
[{字典1},{字典2}]
从列创建(dict)
{
  'key1': [值1, 值2],
  'key2': [值1, 值2]
}
"""


# 从list中创建(从行中创建)
# Create a list of dictionaries with new data
avocados_list = [
    {'date': '2019-11-03', 'small_sold': 10376832, 'large_sold': 7835071},
    {'date': '2019-11-10', 'small_sold': 10717154, 'large_sold': 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)

# 从dict中创建(从列中创建)
# Create a dictionary of lists with new data
avocados_dict = {
  "date": ['2019-11-17', '2019-12-01'],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)


# ------创建DataFrame(读取csv文件)------------
"""
读取和写入csv
csv文件: 行数据已逗号分隔, 每行末尾换行符
1. csv 到 DataFrame
pd.read_csv('文件路径')
2. DataFrame 到 csv
DataFrame.to_csv('文件路径')
"""

#  1) csv to DataFrame

# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv('airline_bumping.csv')  # 读取

# Take a look at the DataFrame
print(airline_bumping.head())


# From previous step
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())

# For each airline, select nb_bumped and total_passengers and sum
# 按airline分类后统计nb_bumped, total_passengers 
airline_totals = airline_bumping.groupby('airline')[['nb_bumped', 'total_passengers']].sum()


# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
# 添加新列
airline_totals["bumps_per_10k"] = airline_totals['nb_bumped'] / airline_totals['total_passengers'] * 10000

# Print airline_totals
print(airline_totals)


#  1) DataFrame to csv

# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values('bumps_per_10k', ascending=False)  # 按 bumps_per_10k 降序

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv('airline_totals_sorted.csv')  # 将DataFrame保存到csv文件