# checkpoint3



get_ipython().system('pip install pandas # DATA VISUALIZATION')



get_ipython().system('pip install matplotlib')





get_ipython().system('pip install numpy')





import pandas as pd
pd.read_excel('titanic-passengers (1).xlsx')



data.shape





data=data.drop([ 'PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'], axis=1)





data.head()




data.describe()




data=data.dropna( axis=0)
data.shape




data.describe()





data.isnull().sum() #find missing information




data.dtypes #Replace missing values




import matplotlib.pyplot as plt





data['Pclass'].value_counts().plot.bar()





data['Age'].hist()




plt.xlabel('Sex')
plt.ylabel('Age')
plt.title('bar plot')
vc=data['Sex'].value_counts()
vc.plot.bar(rot=45)





plt.xlabel('Pclass')
plt.ylabel('Survived')
plt.title('bar plot')
vc=data['Pclass'].value_counts()
vc.plot.bar(rot=45)





data.groupby(['Survived','Pclass']).mean()





Title_Dictionary = {

                    "Capt":       "Officer",

                    "Col":        "Officer",

                    "Major":      "Officer",

                      "Dr":         "Officer",

                    "Rev":        "Officer”,

                    "Jonkheer":   "Royalty",

                    "Don":        "Royalty",

                    "Sir" :       "Royalty",

                   "Lady" :      "Royalty"

                  "the Countess": "Royalty",

                    "Dona":       "Royalty”,

                    "Mme":        "Miss",

                    "Mlle":       "Miss",

                    "Miss" :      "Miss",

                    "Ms":         "Mrs",

                    "Mr" :        "Mrs",

                    "Mrs" :       "Mrs

                    "Master" :    "Master"

                    }
data=pd.DataFrame(Title_Dictionary)
new_data=pd.contact([new_data,Title_Dictionary])
new_data
