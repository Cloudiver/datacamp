# -----------设置和移除索引-------------
# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index('city')   # 将列设置为行索引(默认索引为行编号)

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())   # 重置上面设置的索引, 内容不变

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))   # 设置的行索引被删除

# -----------DataFrame选择元素值-------------
# Make a list of cities to subset on
cities = ['Moscow', 'Saint Petersburg']

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])   # [] 用isin() 判断

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])    #loc[] 里传入列表


# ---------设置多个行索引以及之后的元素选取-------------
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])   # 参数传入列表 大的范围在前

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]   # list中元素为元组

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])  # 同时满足元组中的country 和 city


# -----------根据索引排序-------------
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())   # 默认按索引1排序(升序)

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level="city"))   # 设置level, 指定索引排序

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country", "city"], ascending = [True, False]))  # 同时指定排序索引, 并分别按升序和降序