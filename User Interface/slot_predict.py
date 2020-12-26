import pandas as pd
from sklearn import linear_model
import pickle

data = pd.read_csv('data_new.csv')
data.head(11)
crop_sow = {'Hour': list(data["Hour"]),
            'Minutes': list(data["Minutes"]),
            'Day': list(data["Day"]),
            'Slots': list(data["Slots"])
            }

df = pd.DataFrame(crop_sow,columns=['Hour','Minutes','Day','Slots'])

X = df[['Hour','Minutes','Day']]
Y = df['Slots']
 
# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)
pickle.dump(regr, open('model.pkl','wb'))





