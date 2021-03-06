# -------------------折线图绘制-----------------------------
# Print the last item from year and pop
print(year[-1])
print(pop[-1])


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)   # (x,y)

# Display the plot with plt.show()
plt.show()

"""
总结:
	1.导入pyplot
	2.plt.plot(x,y)  x, y 为 list
	3.plt.show()
"""

# -------------------散点图绘制-----------------------------

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')  # 横坐标变为对数型

# Show plot
plt.show()