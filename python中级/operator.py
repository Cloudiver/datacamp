# -----------------数据类型----------------
True == 1
False == 0
# bool要么是 True or False | 1 or 0

"abc" <= "b"   # True 根据首字母排序


# -----------------NumPy数组比较----------------
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)  # 返回bool值  numpy.ndarray

# my_house less than your_house
print(my_house < your_house)  # 返回bool值  # numpy.ndarray



# -----------------bool操作符----------------
not and or  # not的运算级别最高


# -----------------NumPy布尔判断----------------
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))  # 对应or   输出: [False  True False  True]

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))  # 对应 and  输出: [False False False  True]

														# np.logical_not() 对应 not


# -----------------pandas通过bool判断----------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']  # 返回bool

# Use dr to subset cars: sel
sel = cars[dr]  # 获取为True的值

# Print sel
print(sel)


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars.loc[:, 'cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

"""
小结:
	1. 先获取列系列
	2. 判断条件
	3. 获取为True的元素
"""


# -----------------借助NumPy的布尔函数来进行更复杂的判断----------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and(cars['cars_per_cap'] > 100, cars['cars_per_cap'] < 500)]
# cars['cars_per_cap'] > 100  返回bool序列

# Print medium
print(medium)