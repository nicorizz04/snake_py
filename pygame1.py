#kaggle 1st attempt

import pandas as pd
melbourne_houses = pd.read_csv("melb_data.csv")
melbourne_data = melbourne_houses.describe()
print(melbourne_data)