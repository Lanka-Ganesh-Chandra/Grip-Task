# Importing the necessary libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# Creating a dataframe with the hours studied and the corresponding percentage
data = {'Hours': [2.5, 5, 3, 8, 6, 1.5, 9, 7],
        'Percentage': [21, 47, 27, 75, 60, 20, 90, 69]}

df = pd.DataFrame(data)

# Separating the features (hours studied) and the target (percentage)
X = df[['Hours']]
y = df['Percentage']

# Creating an instance of the Linear Regression model
model = LinearRegression()

# Fitting the model to the data
model.fit(X, y)

# Taking input from the user
hours_studied = float(input("Enter the number of hours studied: "))

# Predicting the percentage based on the input
predicted_percentage = model.predict([[hours_studied]])

# Displaying the predicted percentage
print(f"The predicted percentage for {hours_studied} hours studied is: {predicted_percentage[0]:.2f}%")
