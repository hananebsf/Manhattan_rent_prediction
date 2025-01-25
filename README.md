**Manhattan Rent Prediction**

This project predicts rental prices in Manhattan using a Linear Regression model based on real estate data from StreetEasy—New York City’s leading real estate marketplace, covering everything from studios to high-rises, from Brooklyn Heights to Harlem.

**Dataset Overview**

In this project, we use only the Manhattan dataset from a larger dataset that contains 5,000 rental listings across Manhattan, Brooklyn, and Queens. These listings were active on StreetEasy in June 2016.

The full dataset was originally broken into:

manhattan.csv (used in this project)
brooklyn.csv
queens.csv
Each rental listing includes the following features:

| Column              | Description |
|---------------------|------------|
| **rental_id**      | Unique rental listing ID |
| **rent**           | Monthly rent price (in dollars) |
| **bedrooms**       | Number of bedrooms |
| **bathrooms**      | Number of bathrooms |
| **size_sqft**      | Apartment size (in square feet) |
| **min_to_subway**  | Distance from the nearest subway station (in minutes) |
| **floor**          | Floor number |
| **building_age_yrs** | Age of the building (in years) |
| **no_fee**         | No broker fee? (`0` = No, `1` = Yes) |
| **has_roofdeck**   | Has a roof deck? (`0` = No, `1` = Yes) |
| **has_washer_dryer** | Has an in-unit washer/dryer? (`0` = No, `1` = Yes) |
| **has_doorman**    | Has a doorman? (`0` = No, `1` = Yes) |
| **has_elevator**   | Has an elevator? (`0` = No, `1` = Yes) |
| **has_dishwasher** | Has a dishwasher? (`0` = No, `1` = Yes) |
| **has_patio**      | Has a patio? (`0` = No, `1` = Yes) |
| **has_gym**        | Has a gym? (`0` = No, `1` = Yes) |
| **neighborhood**   | Example: Greenpoint |
| **borough**        | Example: Manhattan |



**Project Goal**

The goal is to train a machine learning model that predicts rent prices in Manhattan based on key features such as apartment size, number of bedrooms and bathrooms, proximity to the subway, building amenities, and more.

**Setup & Usage**

1. Install dependencies:
pip install pandas scikit-learn matplotlib
2. Run the script:
python rent_prediction.py

**Model Performance**
R-squared Score: ~80.5%
Mean Absolute Error (MAE): ~$877.41
Mean Squared Error (MSE): Larger due to squared differences but expected for rental price data.
The model explains approximately 80.5% of the variance in rent prices, which is a strong performance for a linear regression model.

**License**

This project is open-source under the MIT License.
