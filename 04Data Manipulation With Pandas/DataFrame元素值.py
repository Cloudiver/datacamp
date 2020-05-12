# --------------DataFrame元素值---------------
# Select the individuals column
individuals = homelessness['individuals']   # 返回序列值

# Print the head of the result
print(individuals.head())


# Select the state and family_members columns
state_fam = homelessness[['state', 'family_members']]   # 选取2列的值, 返回DataFrame对象

# Print the head of the result
print(state_fam.head())



# --------------加入逻辑判断---------------------
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals'] > 10000]   # 通过逻辑判断来返回值

# See the result
print(ind_gt_10k)



# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region'] == 'Mountain']   # 通过 "相等"来判断

# See the result
print(mountain_reg)


# Filter for rows where family_members is less than 1000 
# and region is Pacific
# 加入 逻辑and来添加多个判断条件
fam_lt_1k_pac = homelessness[(homelessness['family_members'] < 1000) & (homelessness['region'] == 'Pacific')]

# See the result
print(fam_lt_1k_pac)



# Subset for rows in South Atlantic or Mid-Atlantic regions
# isin() 方法用来添加多个判断条件  或的关系(满足其一即可)  返回bool值
# 具体的列序列.isin([])  # 里面是元素值(list)
south_mid_atlantic = homelessness[homelessness["region"].isin(['South Atlantic', 'Mid-Atlantic'])]

# See the result
print(south_mid_atlantic)



# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness)







