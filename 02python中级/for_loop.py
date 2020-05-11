# -----------for循环返回索引-------------------
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print("room " + str(index) + ": " + str(a))


# -----------for循环遍历字典-------------------
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for country, capital in europe.items():   # 使用items()函数
    print("the capital of " + country + " is " + capital)


# -----------for循环遍历numpy数组-------------------
# Import numpy as np
import numpy as np

# For loop over np_height
for x in np_height:  # 一维数组
    print(str(x) + " inches")
    
# For loop over np_baseball
for b in np.nditer(np_baseball): # 二维数组, 需要用np.nditer()函数
    print(b)


# -----------for循环遍历pandas-------------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for ele in cars:  # 这种形式只能输出所有列名
    print(ele)

# Iterate over rows of cars
for x, y in cars.iterrows():  # 通过DataFrame对象的iterrows()方法
    print(x)  # 行标签
    print(y)  # 每行对应的元素(序列)


# -----------for循环遍历pandas, 并获取元素-------------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))  # 通过列标签获取元素值


# -----------for循环 往DataFrame对象中添加列-------------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for x, y in cars.iterrows():  
    cars.loc[x, 'COUNTRY'] = y['country'].upper()   # 通过DataFrame对象的loc方法[横坐标, 纵坐标] = 需要添加的值

# Print cars
print(cars)

# 更加高效的方法
# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper) # 直接赋值
print(cars)