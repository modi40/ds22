import pandas as pd
from sklearn.preprocessing import Normalizer

data = {
    'City': ['Pune', 'Mumbai', 'Bangalore', 'Delhi', 'Hyderabad'],
    'House_Type': ['Apartment', 'Villa', 'Apartment', 'Studio', 'Villa'],
    'House_Area': [1200, 2500, 1400, 600, 2200],
    'Number_of_Rooms': [3, 5, 3, 1, 4],
    'Monthly_Rent': [25000, 65000, 30000, 12000, 50000]
}

df = pd.DataFrame(data)

print("Original House DataFrame:")
print(df)

num_cols = ['House_Area', 'Number_of_Rooms', 'Monthly_Rent']
normalizer = Normalizer()
normalized_vals = normalizer.fit_transform(df[num_cols])

normalized_df = df.copy()
normalized_df[num_cols] = normalized_vals

print("\nNormalized Numerical Attributes:")
print(normalized_df)
