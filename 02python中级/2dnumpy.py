# -------------------创建二维数组-----------------------------
# Create baseball, a list of lists  列表的列表
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(np_baseball)

# Print out the shape of np_baseball   # 数组的维度
print(np_baseball.shape)   # (4,2) 4行2列


# -------------------二维数组大小-----------------------------
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)


# --------------------数组元素-------------------------
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])

# -------------------二维数组运算-----------------------------
# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)    # 加法运算  列数需要相等

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])   # 或者 conversion = np.array((0.0254, 0.453592, 1))   # 用双括号

# Print out product of np_baseball and conversion
print(np_baseball * conversion)  # 乘法运算  列数需要相等

# -------------------二维数组函数-----------------------------
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))   # 平均数

# Print out the median of np_height_in
print(np.median(np_height_in))  # 中位数


# np_baseball is available
# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])   # 平均数   (逗号前面代表行, 后面代表列. 且冒号不能省略. 这代码表示所有行的第一列 )
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:,0])   # 中位数
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))   # 标准差

# Print out correlation between first and second column. Replace 'None'
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])   # 系列相关系数(函数有2个相关系数)
print("Correlation: " + str(corr))


# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)  # 一维数组
np_heights = np.array(heights)


# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']  # 可以通过true|false来选择元素

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))


# 按列分割函数
array1 = np.array([1,2,3])
array2 = np.array([2,3,4])
print(np.column_stack((array1,array2)))   # 输出[[1,2],[2,3],[3,4]]
