pre = float(input("Enter Years Of Experience:"))


#importing pandas
import pandas as pd

#importing dataset
dataset = pd.read_csv("SalaryData.csv")

#setting features and target
y = dataset["Salary"]
x = dataset["YearsExperience"]


#importing linearregression
from sklearn.linear_model import LinearRegression

#here linear regression apply its method to the model
model = LinearRegression()


#converting into numpy array
x = x.values

#reshaping the x column
x = x.reshape(30,1)

#training of model
model.fit(x,y)


#storing output
output = model.predict([[ pre ]])

#print the output
print(output)
