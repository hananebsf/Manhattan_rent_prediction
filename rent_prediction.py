import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split


streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)


from sklearn.linear_model import LinearRegression

mlr = LinearRegression()

mlr.fit(x_train,y_train)

y_predict = mlr.predict (x_test)

# Predicting my future apartment price
my_apartment=[[1,1,750,4,2,10,0,0,1,1,1,1,1,1]]
predict = mlr.predict (my_apartment)
print("Predicted my rent: $%.2f" % predict)

#Scoring our model
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Get R-squared score
r2 = mlr.score(x_test, y_test)

# Get Mean Absolute Error (MAE) - Measures average absolute error
mae = mean_absolute_error(y_test, y_predict)

# Get Mean Squared Error (MSE) - Penalizes larger errors more
mse = mean_squared_error(y_test, y_predict)

# Print Scores
print(f"R-squared Score: {r2:.4f}")
print(f"Mean Absolute Error: ${mae:.2f}")
print(f"Mean Squared Error: ${mse:.2f}")
