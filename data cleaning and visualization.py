
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel("C:/Users/THIS/Downloads/Financial_Sample.xlsx")
df.shape
(700, 16)
df.head()
Segment	Country	Product	Discount Band	Units Sold	Manufacturing Price	Sale Price	Gross Sales	Discounts	Sales	COGS	Profit	Date	Month Number	Month Name	Year
0	Government	Canada	Carretera	NaN	1618.5	3	20.0	32370.0	0.0	32370.0	16185.0	16185.0	2014-01-01	1	January	2014
1	Government	Germany	Carretera	NaN	1321.0	3	20.0	26420.0	0.0	26420.0	13210.0	13210.0	2014-01-01	1	January	2014
2	Midmarket	France	Carretera	NaN	2178.0	3	15.0	32670.0	0.0	32670.0	21780.0	10890.0	2014-06-01	6	June	2014
3	Midmarket	Germany	Carretera	NaN	888.0	3	15.0	13320.0	0.0	13320.0	8880.0	4440.0	2014-06-01	6	June	2014
4	Midmarket	Mexico	Carretera	NaN	2470.0	3	15.0	37050.0	0.0	37050.0	24700.0	12350.0	2014-06-01	6	June	2014
df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 700 entries, 0 to 699
Data columns (total 16 columns):
 #   Column               Non-Null Count  Dtype         
---  ------               --------------  -----         
 0   Segment              692 non-null    object        
 1   Country              689 non-null    object        
 2   Product              692 non-null    object        
 3   Discount Band        638 non-null    object        
 4   Units Sold           695 non-null    float64       
 5   Manufacturing Price  700 non-null    int64         
 6   Sale Price           693 non-null    float64       
 7   Gross Sales          695 non-null    float64       
 8   Discounts            695 non-null    float64       
 9    Sales               700 non-null    float64       
 10  COGS                 700 non-null    float64       
 11  Profit               700 non-null    float64       
 12  Date                 700 non-null    datetime64[ns]
 13  Month Number         700 non-null    int64         
 14  Month Name           700 non-null    object        
 15  Year                 700 non-null    int64         
dtypes: datetime64[ns](1), float64(7), int64(3), object(5)
memory usage: 87.6+ KB
df.isnull().sum()
Segment                 8
Country                11
Product                 8
Discount Band          62
Units Sold              5
Manufacturing Price     0
Sale Price              7
Gross Sales             5
Discounts               5
 Sales                  0
COGS                    0
Profit                  0
Date                    0
Month Number            0
Month Name              0
Year                    0
dtype: int64
# Percentage of missing values
df.isnull().sum().sum()/df.shape[0]*100
15.857142857142856
# Heatmap on missing values
sns.heatmap(df.select_dtypes(include=np.number).isnull())
plt.show()

# finiding null values in Object COlumn
df.select_dtypes(include="object").isnull().sum()
Segment           8
Country          11
Product           8
Discount Band    62
Month Name        0
dtype: int64
# Finding mode values of object column
for col in df.select_dtypes(include='object').columns:
    print("Column Name :",col,"- Mode Value :",df[col].mode()[0])
Column Name : Segment - Mode Value : Government
Column Name : Country - Mode Value : France
Column Name : Product - Mode Value : Paseo
Column Name : Discount Band - Mode Value : High
Column Name : Month Name - Mode Value : October
# Filling Mode Values in Object Column
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(value=df[col].mode()[0])
# finiding null values in Object COlumn
df.select_dtypes(include="object").isnull().sum()
Segment          0
Country          0
Product          0
Discount Band    0
Month Name       0
dtype: int64
# finiding null values in Number COlumn
df.select_dtypes(include=np.number).isnull().sum()
Units Sold             5
Manufacturing Price    0
Sale Price             7
Gross Sales            5
Discounts              5
 Sales                 0
COGS                   0
Profit                 0
Month Number           0
Year                   0
dtype: int64
# Finding Mean Value of Number Column
for col in df.select_dtypes(include=np.number).columns:
    print("Column Name :",col,"- Mean Value :",df[col].mean())
Column Name : Units Sold - Mean Value : 1607.8805755395683
Column Name : Manufacturing Price - Mean Value : 96.47714285714285
Column Name : Sale Price - Mean Value : 117.91486291486291
Column Name : Gross Sales - Mean Value : 183967.04244604317
Column Name : Discounts - Mean Value : 13077.16234532374
Column Name :  Sales - Mean Value : 169609.07179999998
Column Name : COGS - Mean Value : 145475.21142857143
Column Name : Profit - Mean Value : 24133.860371428567
Column Name : Month Number - Mean Value : 7.9
Column Name : Year - Mean Value : 2013.75
# Filling Mean Value in Number Column
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].mean())
# finiding null values in Number COlumn
df.select_dtypes(include=np.number).isnull().sum()
Units Sold             0
Manufacturing Price    0
Sale Price             0
Gross Sales            0
Discounts              0
 Sales                 0
COGS                   0
Profit                 0
Month Number           0
Year                   0
dtype: int64
# Heatmap on missing values
sns.heatmap(df.select_dtypes(include=np.number).isnull())
plt.show()

df.isnull().sum()
Segment                0
Country                0
Product                0
Discount Band          0
Units Sold             0
Manufacturing Price    0
Sale Price             0
Gross Sales            0
Discounts              0
 Sales                 0
COGS                   0
Profit                 0
Date                   0
Month Number           0
Month Name             0
Year                   0
dtype: int64
df.head()
Segment	Country	Product	Discount Band	Units Sold	Manufacturing Price	Sale Price	Gross Sales	Discounts	Sales	COGS	Profit	Date	Month Number	Month Name	Year
0	Government	Canada	Carretera	High	1618.5	3	20.0	32370.0	0.0	32370.0	16185.0	16185.0	2014-01-01	1	January	2014
1	Government	Germany	Carretera	High	1321.0	3	20.0	26420.0	0.0	26420.0	13210.0	13210.0	2014-01-01	1	January	2014
2	Midmarket	France	Carretera	High	2178.0	3	15.0	32670.0	0.0	32670.0	21780.0	10890.0	2014-06-01	6	June	2014
3	Midmarket	Germany	Carretera	High	888.0	3	15.0	13320.0	0.0	13320.0	8880.0	4440.0	2014-06-01	6	June	2014
4	Midmarket	Mexico	Carretera	High	2470.0	3	15.0	37050.0	0.0	37050.0	24700.0	12350.0	2014-06-01	6	June	2014
df.columns
Index(['Segment', 'Country', 'Product', 'Discount Band', 'Units Sold',
       'Manufacturing Price', 'Sale Price', 'Gross Sales', 'Discounts',
       ' Sales', 'COGS', 'Profit', 'Date', 'Month Number', 'Month Name',
       'Year'],
      dtype='object')
# Finding COGS value by Segment
cbs = df.groupby(['Segment']).agg({'COGS':'sum'}).reset_index()
cbs
Segment	COGS
0	Channel Partners	474964.5
1	Enterprise	20226240.0
2	Government	41124913.5
3	Midmarket	1721780.0
4	Small Business	38284750.0
plt.figure(figsize=(6,3))
plt.plot(cbs.Segment , cbs.COGS ,marker="o" , color="red")
plt.xlabel('Segment Names')
plt.ylabel('Rupess in INR(Crore)')
plt.title('COGS by Segment')
plt.show()

# Table for Profit by Segment
pbs = df.groupby(['Segment']).agg({'Profit':'sum'}).reset_index()
pbs
Segment	Profit
0	Channel Partners	1.290808e+06
1	Enterprise	-6.145456e+05
2	Government	1.141417e+07
3	Midmarket	6.601031e+05
4	Small Business	4.143168e+06
plt.figure(figsize=(6,3))
plt.plot(pbs.Segment , pbs.Profit ,marker="o" , color="lightgreen")
plt.xlabel('Segment Names')
plt.ylabel('Rupess in INR(Crore)')
plt.title('Profit by Segment')
plt.show()

# COGS and Profit By Segment
plt.figure(figsize=(6,3))
plt.plot(pbs.Segment , pbs.Profit ,marker="o" , color="lightgreen")
plt.plot(cbs.Segment , cbs.COGS ,marker="o" , color="red")
plt.xlabel('Segment Names')
plt.ylabel('Rupess in INR(Crore)')
plt.title('COGS by Segment')
plt.show()

# Calculate NetSale, Costing, Profit
netSale = sum(cbs.COGS)
profit = sum(pbs.Profit)
costing = netSale-profit
print("Net_Sale : ",netSale)
print("Costing : ",costing)
print("Profit : ",profit)
Net_Sale :  101832648.0
Costing :  84938945.74
Profit :  16893702.26
# Visualization for Profit and Costing
plt.figure(figsize=(8,3))
plt.pie([profit,costing] , colors=["lightgreen","red"],labels=[profit/netSale*100,costing/netSale*100])
plt.legend(["Profit","COGS"])
plt.show()

df.head(2)
Segment	Country	Product	Discount Band	Units Sold	Manufacturing Price	Sale Price	Gross Sales	Discounts	Sales	COGS	Profit	Date	Month Number	Month Name	Year
0	Government	Canada	Carretera	High	1618.5	3	20.0	32370.0	0.0	32370.0	16185.0	16185.0	2014-01-01	1	January	2014
1	Government	Germany	Carretera	High	1321.0	3	20.0	26420.0	0.0	26420.0	13210.0	13210.0	2014-01-01	1	January	2014
# Manufacturing Price By Product
print("Product Name : ",df.Product.unique())
mbp = df.groupby(['Product']).agg({'Manufacturing Price':'sum'}).reset_index()
mbp
Product Name :  ['Carretera' 'Montana' 'Paseo' 'Velo' 'VTT' 'Amarilla']
Product	Manufacturing Price
0	Amarilla	23140
1	Carretera	276
2	Montana	465
3	Paseo	3693
4	VTT	27000
5	Velo	12960
# Sale Price by Product
print("Product Name : ",df.Product.unique())
sbp = df.groupby(['Product']).agg({'Sale Price':'sum'}).reset_index()
sbp
Product Name :  ['Carretera' 'Montana' 'Paseo' 'Velo' 'VTT' 'Amarilla']
Product	Sale Price
0	Amarilla	11342.829726
1	Carretera	10095.000000
2	Montana	10890.000000
3	Paseo	23054.744589
4	VTT	14721.829726
5	Velo	12436.000000
# Manufacturing and Sale Price By Product
plt.subplot(2,1,1)
plt.bar(mbp.Product,mbp['Manufacturing Price'])
plt.ylabel('Manufacturing Price')
plt.title("Manufacturing Price And Sale Price By Products")
plt.subplot(2,1,2)
plt.bar(sbp.Product,sbp['Sale Price'],color="crimson")
plt.ylabel('Sale Price')
plt.xlabel('Product Name')
plt.show()

FINISH