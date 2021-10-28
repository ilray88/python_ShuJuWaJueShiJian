import  pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
bf=pd.read_csv('BlackFriday.csv',header='infer')
print(bf.info())
print(bf.head(10))
print(bf.isna().any())
missing_percentage=(bf.isnull().sum()/bf.shape[0]*100).sort_values(ascending=False)
missing_percentage=missing_percentage[missing_percentage!=0].round(2)
print(missing_percentage)
bf.fillna(0,inplace=True)
bf.isna().any().sum()

def data_type(bf):
    for i in bf.columns:
        print(i,'------->>',bf[i].unique())
    print(data_type(bf))
#print(data_type(bf))

#性别和婚姻状况
# 哪些人群更可能在黑色星期五购买更多?
#Q1 性别：男性或女性+#Q4 婚姻状况: 结婚或者结婚  双重pie
bf_gen_mar = bf.groupby(['Gender','Marital_Status']).count().reset_index('Marital_Status')
bf_gen = bf.groupby(['Gender']).count()
# Female_0,Female_1 中的 "0"代表未婚，"1"代表已婚
plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
plt.figure(figsize=(9,6))
plt.subplots_adjust(left=0.017,right=0.983,bottom=0.033,top=0.921,wspace=0.2,hspace=0.2 )
plt.pie(bf_gen_mar.iloc[:,2],radius=1,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['blue','red','gray','White'],labels=['单身女性','已婚女性','单身男性','已婚男性'],autopct='%1.1f%%',pctdistance = 0.9)
plt.pie(bf_gen.iloc[:,1],radius=0.7,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['blue','red','gray','White'],labels=['女性','男性'],labeldistance = 0.6,autopct='%1.1f%%',pctdistance = 0.4)
plt.tight_layout()
plt.legend()
plt.axis('equal')
#plt.title('性别&婚姻状况')
plt.show()

bf_age=bf.groupby(['Age']).count()
sns.barplot(x=bf_age.index,y=bf_age.Purchase)
plt.show()

bf_Occ=bf.groupby(['Occupation']).count()
sns.barplot(x=bf_Occ.index,y=bf_Occ.Purchase)
plt.show()

bf_SYears=bf.groupby(['Stay_In_Current_City_Years']).count()
sns.barplot(x=bf_SYears.index,y=bf_SYears.Purchase)
plt.show()

bf_City=bf.groupby(['City_Category']).count()
plt.figure(figsize=(9,6))
plt.pie(bf_City.iloc[:,1],radius=0.7,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['blue','red','gray','White'],labels=['A','B','C'],
        labeldistance=0.8,autopct='%1.1f%%',pctdistance = 0.7)

plt.tight_layout()
plt.legend()
plt.axis('equal')
plt.title('City')
plt.show()

# 哪种产品在黑色星期五更畅销?（top 10）
fig1, ax1 = plt.subplots(figsize=(12,7))
bf.groupby('Product_ID')['Purchase'].sum().nlargest(10).sort_values().plot(kind='barh')
plt.show()

product=bf .loc[:,['Product_ID','Product_Category_1','Product_Category_2','Product_Category_3','Purchase']]
print('黑五期间涉及的销售商品共{}个。'.format(len(product['Product_ID'].unique())))
bf.loc[:,['User_ID','Product_ID','Purchase']].sort_values(by='Product_ID').head()
#将销售额按商品ID分类加和后由高到低排列，并计算累计销售额占比
product_purchase=product.loc[:,['Product_ID','Purchase']].groupby('Product_ID').sum().sort_values(by='Purchase',ascending=0).reset_index()
product_purchase['Percent']=product_purchase['Purchase']/product_purchase['Purchase'].sum()
product_purchase['P_Cumsum']=product_purchase['Percent'].cumsum()
product_purchase.head()

plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
fig=plt.figure(figsize=(12,6),dpi=100)
ax1=fig.add_subplot(111)
ax1.grid()
ax2=ax1.twinx()#建立副纵坐标轴
data_2=product_purchase['Purchase']
data_1=product_purchase['P_Cumsum']
x=np.arange(1,len(product_purchase)+1)
ax1.plot(x,data_1,color='gray',linewidth=5,label='销售额累计占比')
ax2.plot(x,data_2,color='black',linewidth=1,label='单个商品销售额')
ax1.set_xlabel('商品种类')
ax1.set_yticks(np.linspace(0,1,11))
ax1.set_yticklabels(['{:.0%}'.format(i/10) for i in range(11)])#y轴刻度显示百分比
ax1.set_ylabel('累计销售额占比')
ax2.set_ylabel('单个商品的销售额')
ax1.legend(loc=(0.83,0.14))
ax2.legend(loc=(0.83,0.08))
ax1.set_title('BlackFridy各产品销售额的帕累托图',fontsize=18)
plt.show()

## 二次探索数据
##不同人群对不同产品的购买情况
# 随着年龄的上升，各类型的产品呈怎样的趋势
bf_P1=bf.groupby(['Age'])['Purchase'].sum()
bf_P2=bf[bf["Product_Category_2"]>0]
bf_P2=bf_P2.groupby(['Age'])['Purchase'].sum()
bf_P3=bf[bf["Product_Category_3"]>0]
bf_P3=bf_P3.groupby(['Age'])['Purchase'].sum()
fig=plt.figure(figsize=(9,6));
ax=fig.add_subplot(1,1,1)
ticks=ax.set_xticklabels(['0-17','18-25', '26-35','36-45','46-50','51-55','55+'])
#ax.set_title("不同年龄对不同产品类型购物情况")
ax.set_xlabel('年龄')
ax.set_ylabel('金额')
ax.legend(loc='best')
ax.plot(bf_P1,marker='o')
ax.plot(bf_P2,marker='*')
ax.plot(bf_P3,marker='.')
ax.legend(['产品类型1','产品类别2','产品类别3'])
plt.show()

## 二次探索数据
# 不同城市对不同产品的需求
bf1_city_sum1 = bf.groupby(['City_Category'])['Product_Category_1'].sum()
bf1_city_sum2 = bf.groupby(['City_Category'])['Product_Category_2'].sum()
bf1_city_sum3 = bf.groupby(['City_Category'])['Product_Category_3'].sum()
bf1_city_sum1

fig=plt.figure(figsize=(12,5));
# 图形位置与标题
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)
ax1.set_title('Product_Category_1')
ax2.set_title('Product_Category_2')
ax3.set_title('Product_Category_3')
# 作图
ax1.pie(bf1_city_sum1,radius=0.7,wedgeprops=dict(width=0.3,edgecolor='w'),
colors=['cyan','lightskyblue','linen','yellow'],labels=['A','B','C'],
labeldistance = 0.8,autopct='%1.1f%%',pctdistance = 0.5)
ax2.pie(bf1_city_sum2,radius=0.7,wedgeprops=dict(width=0.3,edgecolor='w'),
colors=['cyan','lightskyblue','linen','yellow'],labels=['A','B','C'],
labeldistance = 0.8,autopct='%1.1f%%',pctdistance = 0.5)
ax3.pie(bf1_city_sum3,radius=0.7,wedgeprops=dict(width=0.3,edgecolor='w'),
colors=['cyan','lightskyblue','linen','yellow'],labels=['A','B','C'],
labeldistance = 0.8,autopct='%1.1f%%',pctdistance = 0.5)
# 正圆与图例
ax1.axis('equal')
ax2.axis('equal')
ax3.axis('equal')
ax3.legend(['A','B','C'])
plt.show()


bf_C = bf.groupby(['City_Category','Age']).count().reset_index('Age')

fig=plt.figure(figsize=(14,8))
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)
ax1.set_title('A')
ax2.set_title('B')
ax3.set_title('C')

ax1.pie(bf_C.iloc[0:7,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 0.7)
ax2.pie(bf_C.iloc[7:14,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 0.7)
ax3.pie(bf_C.iloc[14:23,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 0.7)

ax1.axis('equal')
ax2.axis('equal')
ax3.axis('equal')
ax1.legend(['0-17','18-25','26-35','36-45','46-50','51-55' ,'55+'],loc="best")
plt.show()

plt.figure(figsize=(10,7))
plt.pie(bf_C.iloc[0:7,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 0.5)
plt.pie(bf_C.iloc[7:14,2],radius=0.7,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 0.8)
plt.pie(bf_C.iloc[14:23,2],radius=1,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 1.1)
plt.text(0,0.8,"C")
plt.text(0,0.55,"B")
plt.text(0,0.3,"A")
plt.tight_layout()
plt.legend(['0-17','18-25','26-35','36-45','46-50','51-55' ,'55+'],loc="best")
plt.axis('equal')
plt.title('Gender & Marital_Status')
plt.show()


