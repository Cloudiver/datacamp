# -------DataFrame通过列名排序----------------
"""
当列有相同的值时, 可以指定其他列一起进行排序

1列	df.sort_values("breed")  传入字符串   默认是升序排列
>= 2列	df.sort_values(["breed", "weight_kg"])   # 传入排序列表  --- 指定其他列进行排序
"""
# Sort homelessness by individual
homelessness_ind = homelessness.sort_values('individuals')

# Print the top few rows
print(homelessness_ind.head())   # 输出前5行


# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members', ascending=False)   # 根据family_members降序排列

# Print the top few rows
print(homelessness_fam.head())



# Sort homelessness by region, then descending family members
# 用多列进行排序, 如果第一个参数的值相同, 然后再按照第二个参数的值排列,  再通过ascending指定分别的降序, 升序规则, 列表
# 默认是升序
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending=[True, False]) 

# Print the top few rows
print(homelessness_reg_fam.head())