# --------------------pandas DataFrame创建-----------------
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]   # 个数必须相同

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)    # 从字典中创建DataFrame

# Print cars
print(cars)


# ------------从list中创建DataFrame-------------
df = pd.DataFrame([[2.0, 1.0],
                   [3.0, 4],
                   [1.0, 0.0]],
                   columns=list('AB'))

print(df)
"""输出:
     A    B
0  2.0  1.0
1  3.0  4.0
2  1.0  0.0
"""


# --------------------DataFrame索引设置-----------------
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels  # 表格行索引设置

# Print cars again
print(cars)