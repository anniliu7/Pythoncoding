# The ordinal encoding approach assumes there is an inherent order of categories in the variable.

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Define a scoring mechanism to evaluate the impact of each encoding strategy on model performance
def score_encode_strategy(X_t=X_train, X_v=X_valid, y_t=y_train, y_v=y_valid):
    rf = RandomForestRegressor(n_estimators=50, random_state=9)
    rf.fit(X_t, y_t)
    preds = rf.predict(X_v)
    return mean_absolute_error(y_v, preds)

data_train = pd.read_csv("../data/raw/train.csv")
data_valid = pd.read_csv("../data/raw/valid.csv")

y_train = data_train["Methylation_Level"]
y_valid = data_valid["Methylation_Level"]
features = ["Grade_Category", "Age_Category", "BMI_Category"]

# Take a look at the categorical variable
# When we fit an ordinal encoder on the training data, it assigns each unique value a specific integer label. 
# If the validation data contains values that weren't present in the training set, the encoder will raise an error because those new values don't have an assigned integer.
# We can tailor an ordinal encoder to handle new categories, or remove the problematic categorical variables.
print("The unique values in 'Grade_Category' column in training data:", data_train['Grade_Category'].unique())
print("\nThe unique values in 'Grade_Category' column in validation data:", data_valid['Grade_Category'].unique())

ordinal_encoder = OrdinalEncoder()
X_train = ordinal_encoder.fit_transform(data_train[features]) 
X_valid = ordinal_encoder.transform(data_valid[features]) #
# For these categorical variables, we randomly map each unique category value to a distinct integer. 
# This straightforward method is widely used because it avoids the hassle of crafting custom labels. 
# However, we may achieve better performance by assigning more meaningful, informed labels to ordinal variables.
# We apply the same ordinal encoding parameters (categorical integer value) that were derived from the training data, without recalculating them on the validation data. 
# This ensures that the variable encoding process remains consistent and that the validation set doesn't influence the encoding statistics.

print("The mean absolute error from Ordinal Encoding:") 
print(score_encode_strategy(X_train, X_valid, y_train, y_valid))

