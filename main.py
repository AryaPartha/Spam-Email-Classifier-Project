import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from  sklearn.feature_extraction.text import TfidfVectorizer
from  sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 
 
df =pd.read_csv('mail_data.csv')
data = df.where((pd.notnull(df)),"")
data.head()

data.loc[data['Category']== 'spam', 'Category',]=0
data.loc[data['Category']== 'ham', 'Category',]=1

x= data['Message']
y= data['Category']

# split the data set for testing and training 
X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size=0.2,random_state= 3)
#80% data is used to train and 20% data is for testing   

#converting the text data to the input that is given to the logical regression
  
feature_extraction = TfidfVectorizer(min_df=1,stop_words='english',lowercase='True')
X_train_feature = feature_extraction.fit_transform(X_train)
X_test_feature = feature_extraction.fit_transform(X_test)

Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

model = LogisticRegression()
model.fit(X_test_feature, Y_train)
 

prediction_on_training_data = model.predict(X_test_feature)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)

prediction_on_test_data = model.predict(X_test_feature)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)
# input of the mail
input_your_mail = input[""]
# converting text to feature vector
input_data_features = feature_extraction.transform(input_your_mail)
prediction = model.predict(input_data_features)

#printing the result 

print (prediction)
if(prediction[0]==1):
    print ("Ham mail")
else:
    print("Spam mail")
