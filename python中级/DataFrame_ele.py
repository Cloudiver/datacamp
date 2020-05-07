# --------------------读取DataFrame中列元素-----------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])  #  返回 Pandas Series

# Print out country column as Pandas DataFrame
print(cars[['country']])  # 返回DataFrame对象, 包含行列标签

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])  # [里面包含一个list对象]


# --------------------读取DataFrame中行元素-----------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])  # 行只需要单[]

# Print out fourth, fifth and sixth observation
print(cars[3:])


# --------------------读取DataFrame中行元素(DataFrame对象 loc函数)-----------------
# loc 使用行标签
# iloc 使用行索引


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JPN'])   # 单[]返回 Pandas Series

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])  # DataFrame



# --------------------读取DataFrame中行列元素(DataFrame对象 loc/iloc函数)-----------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])  # [x,y] 返回值

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])


# --------------------通过DataFrame列元素读取(DataFrame对象 loc/iloc函数)-----------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])  # 只能省略前面, 后面省略没什么意义

# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap' ,'drives_right']])
# print(cars[['cars_per_cap' ,'drives_right']])  # 两种方式效果一样, 下面的好像更加简洁?



