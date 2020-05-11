# -------------------直方图图绘制-----------------------------
plt.hist(life_exp)  # hist(x, bins,...) x表示输入的数据序列, 数组形式 , bins 是将数据分作几块,默认为10
print(life_exp)   
# Display histogram
plt.show()


# -------------------直方图图绘制2.bins的设置-----------------------------
# Build histogram with 5 bins
plt.hist(life_exp, 5)

# Show and clean up plot
plt.show()
plt.clf()   # 清除已有的图表, 不清除绘制的图表会重叠在一起

# Build histogram with 20 bins
plt.hist(life_exp, 20)
print(type(life_exp))
# Show and clean up again
plt.show()
plt.clf()