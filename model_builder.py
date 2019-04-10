import pandas as pd

df = pd.read_csv('emp_attrition.csv')

# Remove Unwanted Columns
df = df.drop(columns=['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'])

# Categorize Binary Data
df['Attrition'].replace(to_replace=['Yes','No'], value=[1,0],inplace=True)
df['Gender'].replace(to_replace=['Male','Female'], value=[1,0],inplace=True)
df['OverTime'].replace(to_replace=['Yes','No'], value=[1,0],inplace=True)

# Categorize Continuous Data
bin = [17,30,40,50,60]
category = pd.cut(df.Age, bin ,labels =["Age18-30","Age31-40","Age41-50","Age51-60"])
df['AgeCat'] = category
df['AgeCat'].value_counts()

bin = [0,10,20,30]
category = pd.cut(df.DistanceFromHome, bin ,labels =["DFH0-10","DFH10-20","DFH20-30"])
df['DistanceFromHomeCat'] = category
df['DistanceFromHomeCat'].value_counts()

bin = [0,16,20,26]
category = pd.cut(df.PercentSalaryHike, bin ,labels =["SH0-16","SH17-20","SH21-25"])
df['PercentSalaryHikeCat'] = category
df['PercentSalaryHikeCat'].value_counts()

bin = [-1,5,15,25,41]
category = pd.cut(df.TotalWorkingYears, bin ,labels =["TWY0-5","TWY6-15","TWY16-25", "TWY25-41"])
df['TotalWorkingYearsCat'] = category
df['TotalWorkingYearsCat'].value_counts()

bin = [0,5000,10000,15000,20000]
category = pd.cut(df.MonthlyIncome, bin ,labels =["MI0-5k", "MI5-10k", "MI10-15k", "MI15-20k"])
df['MonthlyIncomeCat'] = category
df['MonthlyIncomeCat'].value_counts()

bin = [-1,2,8,16]
category = pd.cut(df.YearsSinceLastPromotion, bin ,labels =["YSLP0-2", "YSLP3-8", "YSLP9-16"])
df['YearsSinceLastPromotionCat'] = category
df['YearsSinceLastPromotionCat'].value_counts()

bin = [-1,5,15,25,40]
category = pd.cut(df.YearsAtCompany, bin ,labels =["YAC0-5","YAC5-15","YAC15-25","YAC25-40"])
df['YearsAtCompanyCat'] = category
df['YearsAtCompanyCat'].value_counts()

df = pd.concat([df,pd.get_dummies(df['AgeCat'])], axis=1)
df = pd.concat([df,pd.get_dummies(df['Department'])], axis=1)
df = pd.concat([df,pd.get_dummies(df['DistanceFromHomeCat'])], axis=1)
df = pd.concat([df,pd.get_dummies(df['PercentSalaryHikeCat'])], axis=1)
df = pd.concat([df,pd.get_dummies(df['MaritalStatus'])], axis=1)
df = pd.concat([df,pd.get_dummies(df['TotalWorkingYearsCat'])], axis=1)
df = pd.concat([df,pd.get_dummies(df['MonthlyIncomeCat'])], axis=1)
df = pd.concat([df,pd.get_dummies(df['YearsSinceLastPromotionCat'])], axis=1)

tar_df = df['Attrition']

df = df.drop(columns=['Age', 'Attrition', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome', 'Education', 'EducationField', 'EnvironmentSatisfaction', 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager', 'AgeCat', 'DistanceFromHomeCat', 'PercentSalaryHikeCat', 'TotalWorkingYearsCat', 'MonthlyIncomeCat','YearsSinceLastPromotionCat', 'YearsAtCompanyCat'])

from sklearn.model_selection import train_test_split
from random import randint
from sklearn import preprocessing

X = df
X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
y = tar_df
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.25, random_state=randint(0, 9))

from sklearn.tree import DecisionTreeClassifier
drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)

drugTree.fit(X_trainset,y_trainset)

predTree = drugTree.predict(X_testset)
from sklearn import metrics
print("DecisionTrees's Accuracy - Test: ", metrics.accuracy_score(y_testset, predTree))


predTrain = drugTree.predict(X_trainset)
print("DecisionTrees's Accuracy - Train: ", metrics.accuracy_score(y_trainset, predTrain))

#save model to disk
# save the model to disk
from sklearn.externals import joblib
filename = 'finalized_model.sav'
joblib.dump(drugTree, filename)
"""
# Learn how to do this
from sklearn.model_selection import cross_val_score
score = cross_val_score(drugTree, X_testset, predTree, cv=10)
print (score)
"""
