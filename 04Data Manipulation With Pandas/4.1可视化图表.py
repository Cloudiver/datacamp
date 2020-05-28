# --------����ͼ----------------
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
# ����pandas����
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()  # ����ĳ���ȷ��� ��ѡ��Ԫ��

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")   # ����ֱ��ͼ

# Show the plot
plt.show()   # ��ʾͼ��


# --------����ͼ(��Ӧ������ʱ��仯�Ĺ���)--------------------
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
# �������ڷ���, Ȼ�����ÿ���������Ŀ
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind='line')  # ����ͼ

# Show the plot
plt.show()

# ���: https://pic.rmb.bdstatic.com/bjh/12343b62a070f5f3878356b431c1cafa.png


# --------ɢ��ͼ(�ж��������Ƿ����)--------------------
# Scatter plot of nb_sold vs avg_price with title
# ����ͼ���x, y������, ͼ������Ϊɢ��ͼ, ����
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()  # �۸�������Ĺ�ϵ

# ���: https://pic.rmb.bdstatic.com/bjh/abbb734662e2abb8d8e0d5f66c829409.png


# --------ֱ��ͼ--------------------
# Histogram of conventional avg_price 
avocados[avocados["type"] == "conventional"]["avg_price"].hist()  # ����ֱ��ͼ

# Histogram of organic avg_price
avocados[avocados["type"] == "organic"]["avg_price"].hist()

# Add a legend
plt.legend(["conventional", "organic"])   #.legend([])  list  ����ͼ��

# Show the plot
plt.show()


# ����͸����
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

# ���ÿ��С bins
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# ���: https://pic.rmb.bdstatic.com/bjh/f083723bc01527d32ca6c79f03bf4021.png