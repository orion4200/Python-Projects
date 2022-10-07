import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def fix_area_type(x):
  if x != 'Super built-up  Area':
    return 'Others'
  else:
    return x

def convert_total_sqft(x):
    try:
      if len(x.split('-')) > 1:
        return (float(x.split('-')[0]) + float(x.split('-')[1]))/2
      else:
        return float(x)
    except:
      return 0

def predict_price(size,sqft,bath,balcony,area,loc):
  input = np.zeros(len(xtrain.columns))

  input[0] = size
  input[1] = sqft
  input[2] = bath
  input[3] = balcony

  input[np.where(xtrain.columns == area)[0][0]] = 1
  input[np.where(xtrain.columns == loc)[0][0]] = 1

  return (lmodel.predict([input]))


df = pd.read_csv('Bengaluru_House_Data.csv')

df1 = df.drop(['availability' , 'society'] , axis='columns')

# print(df1.isnull().sum())
df2 = df1.dropna()

df2['size'] = df2['size'].apply(lambda x : int(x[0]))

#print(df2.dtypes)
df2['total_sqft'] = df2['total_sqft'].apply(convert_total_sqft) 
df3 = df2[df2['total_sqft'] != 0]

df3['PPS'] = (df3['price'] * 100000) / df3['total_sqft']

loc_count = df3['location'].value_counts()
#print(Loc_count)
loc_count_more_then_50 = loc_count[loc_count >= 50]
df4 = df3[df3['location'].apply(lambda x : x in loc_count_more_then_50)]

df5 = pd.DataFrame()

for loc,dfloc in df4.groupby('location'):
  m = dfloc['PPS'].mean()
  s = dfloc['PPS'].std()

  extracted_df = dfloc[(dfloc['PPS'] >= (m - 2 * s)) & (dfloc['PPS'] <= (m + 2 * s))]
  df5 = pd.concat([df5,extracted_df] , ignore_index=True)

df6 = df5.drop('PPS' , axis='columns')
df6['area_type'] = df6['area_type'].apply(fix_area_type)

at = pd.get_dummies(df6['area_type'])
loc = pd.get_dummies(df6['location'])

df7 = pd.concat((df6,at,loc) , axis=1)
df8 = df7.drop(['area_type', 'location'] , axis=1)

###################### training model #########################

X = df8.drop('price' , axis='columns')
Y = df8['price']

xtrain,xtest,ytrain,ytest = train_test_split(X,Y)
lmodel = LinearRegression()
lmodel.fit(xtrain,ytrain)

ytrain_pred = lmodel.predict(xtrain)
ytest_pred = lmodel.predict(xtest)

print(predict_price(3,1200,2,1,'Yelahanka','Super built-up  Area'))
