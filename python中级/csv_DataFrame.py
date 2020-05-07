# --------------------读取csv文件-----------------
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')  # 读取csv文件并返回DataFrame对象

# Print out cars
print(cars)


# --------------------读取csv文件, 指定表格标签-----------------
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)  # 第一列作为标签名

# Print out cars
print(cars)