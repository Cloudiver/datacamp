# --------------------dict键名及访问-----------------
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())  # 输出字典的全部键名

# Print out value that belongs to key 'norway'
print(europe['norway'])


# --------------------dict新增键值及判断键名是否在字典中-----------------
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)   # 判断键名是否在字典中

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)  # 字典没有固有顺序


# --------------------dict键值更新-----------------
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany
europe['germany'] = 'berlin'   # 键名唯一, 所以可以用来更新键值

# Remove australia
del(europe['australia'])   # 删除键名, 键值对都会被删除

# Print europe
print(europe)


# --------------------dict中添加dict-----------------
# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])  # 访问键值

# Create sub-dictionary data
data = {'capital':'rome', 'population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data  # 添加新的键值对

# Print europe
print(europe)