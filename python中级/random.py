# --------------------生成随机浮点数------------------
# Import numpy as np
import numpy as np

# Set the seed
seed = np.random.seed(123)

# Generate and print random float
print(np.random.rand())   # 生成随机浮点数


# --------------------生成随机整数------------------
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))   # 生成1~7之前的随机整数 不包括7

# Use randint() again
print(np.random.randint(1,7))



# --------------------加入判断------------------
# Numpy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif 3 <= dice <= 5:
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)


# --------------------随机游走(以前一次步骤为基础)------------------
# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]  # 每次起始步以前一次结果为基准

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
		# step = max(0, step - 1)   保证起始步数不为负数
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)


# --------------------可视化步数过程------------------
# Numpy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)   # 只传入一个参数, plot根据参数的个数设置横坐标刻度

# Show the plot
plt.show()    # 图形: http://ww1.sinaimg.cn/large/9dc802a0gy1gend1cuf6fj20ky0go3yw.jpg



# --------------------总共进行10次这样的过程------------------
# Numpy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :   # 循环10次, 总共走10次

    # Code from before  # 这是走一次的情况
    random_walk = [0]  # 最开始的时候在0层
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)




# --------------------可视化10次过程, 分析机会------------------
# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)  # list变成一个二维数组

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)  # 将数组的行列交换重新组成数组, 如 [[0,1],[2,3]] ==> [[0,2],[1,3]]

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()    # 图形: http://ww1.sinaimg.cn/large/9dc802a0gy1genduqidtij20ky0gomzo.jpg



# --------------------可视化250次过程, 分析机会------------------
# numpy and matplotlib imported, seed set

# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001 :   # 0.1%的机会摔下去, 步数从0开始
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()


# --------------------直方图-可视化500次过程------------------
# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1, :]  # 选择二维数组中最后一行

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()  # 图形: http://ww1.sinaimg.cn/large/9dc802a0gy1geneo372sxj20ky0go0sr.jpg