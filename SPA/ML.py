import pandas as pd
import numpy as np


df = pd.read_csv('student-mat.csv',sep=';')
#print(df.head())

X = df.drop('G3',axis=1)
y = df['G3']



#all nominal data is now to be one hot encoded

def one_hot_enc(data, var, all_var):
    for label in all_var:
        data[var + '_' + label] = np.where(data[var] == label, 1, 0)


data = pd.read_csv('student-mat.csv', sep=';',
                   usecols=['sex', 'address', 'Pstatus', 'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup', 'famsup',
                            'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'school'])

all_var = [x for x in data.sex.value_counts().sort_values(ascending=False).index]
one_hot_enc(data, 'sex', all_var)
data.drop('sex', axis=1, inplace=True)


all_var = [x for x in data.address.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'address',all_var)
data.drop('address',axis=1,inplace=True)

all_var = [x for x in data.Pstatus.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'Pstatus',all_var)
data.drop('Pstatus',axis=1,inplace=True)


all_var = [x for x in data.Mjob.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'Mjob',all_var)
data.drop('Mjob',axis=1,inplace=True)


all_var = [x for x in data.Fjob.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'Fjob',all_var)
data.drop('Fjob',axis=1,inplace=True)

all_var = [x for x in data.reason.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'reason',all_var)
data.drop('reason',axis=1,inplace=True)

all_var = [x for x in data.guardian.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'guardian',all_var)
data.drop('guardian',axis=1,inplace=True)

all_var = [x for x in data.schoolsup.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'schoolsup',all_var)
data.drop('schoolsup',axis=1,inplace=True)

all_var = [x for x in data.famsup.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'famsup',all_var)
data.drop('famsup',axis=1,inplace=True)

all_var = [x for x in data.paid.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'paid',all_var)
data.drop('paid',axis=1,inplace=True)


all_var = [x for x in data.activities.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'activities',all_var)
data.drop('activities',axis=1,inplace=True)

all_var = [x for x in data.nursery.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'nursery',all_var)
data.drop('nursery',axis=1,inplace=True)

all_var = [x for x in data.higher.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'higher',all_var)
data.drop('higher',axis=1,inplace=True)

all_var = [x for x in data.internet.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'internet',all_var)
data.drop('internet',axis=1,inplace=True)


all_var = [x for x in data.romantic.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'romantic',all_var)
data.drop('romantic',axis=1,inplace=True)

all_var = [x for x in data.school.value_counts().sort_values(ascending=False).index]
one_hot_enc(data,'school',all_var)
data.drop('school',axis=1,inplace=True)


for i in data.columns:
    X[i] = data[i]
X.drop(['sex','address','Pstatus','Mjob','Fjob','reason','guardian','schoolsup','famsup', 'paid', 'activities', 'nursery',
              'higher', 'internet', 'romantic','school'],axis=1,inplace = True)


#engineering famsize by ordinal number placement
famsize_ranks = {'LE3':1 , 'GT3':2}

X['famsize_ranked'] = X.famsize.map(famsize_ranks)

X.drop(['famsize'],axis=1,inplace=True)

pd.set_option('display.max_columns', None)
print(X.head())


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

reg = make_pipeline(StandardScaler(), SGDRegressor(max_iter=1000, tol=1e-3))
reg.fit(X_train, y_train)
prediction_SGD = reg.predict(X_test)



import pickle
pickle.dump(reg, open('MODEL_SGD', 'wb'))
