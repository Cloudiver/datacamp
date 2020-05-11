# -------------------给图表添加横纵轴说明, 以及图表标题-----------------------------
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)  # 绘制散点图
plt.xscale('log')   # 将横坐标变为对数形式

# Strings
xlab = 'GDP per Capita [in USD]'  # 横坐标说明
ylab = 'Life Expectancy [in years]'  # 纵坐标说明
title = 'World Development in 2007'  # 图表标题

# Add axis labels
plt.xlabel(xlab)  # 放置横坐标标题
plt.ylabel(ylab)  # 放置纵坐标标题


# Add title
plt.title(title)  # 放置图表标题

# After customizing, display the plot
plt.show()


# -------------------改变横坐标刻度显示-----------------------------

# Scatter plot
plt.scatter(gdp_cap, life_exp)  # 绘制散点图

# Previous customizations
plt.xscale('log')   
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]   # 原来的横坐标刻度
tick_lab = ['1k', '10k', '100k']   # 用来替换的横坐标刻度

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)   # 替换横坐标刻度,   plt.xtricks(老的刻度, 新的刻度)

# After customizing, display the plot
plt.show()

# -------------------改变散点图内点的大小-----------------------------
# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)   # 变为array

# Double np_pop
np_pop = np_pop * 2  # 每个元素都会被x2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)   # plt.scatter(横坐标, 纵坐标, 点大小<array>)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()


# -------------------改变散点图中点的样式-----------------------------
# Specify c and alpha inside plt.scatter()
# col是和国家一一对应的颜色, alpha是透明度, 0是完全透明, 1是完全不透明
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)


# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()  # 效果: http://ww1.sinaimg.cn/large/9dc802a0gy1geinglfcbuj20ky0got9m.jpg


# -------------------散点图添加格线-----------------------------
# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')   # plt.text(x,y,s) 横坐标, 纵坐标, 要显示的文本
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)  # 绘制栅格线

# Show the plot
plt.show()
