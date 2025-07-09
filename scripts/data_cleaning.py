import pandas as pd

# Load the CSV file
gdp = pd.read_csv("./data/GDP Data.csv")

# Preview the first 5 rows
print(gdp.head())

# Show the shape of the dataset (rows, columns)
print(f"Shape: {gdp.shape}")

# Count missing values per column
print("Missing values per column:")
print(gdp.isnull().sum())

# Remove duplicate rows
gdp = gdp.drop_duplicates()

# Fill missing values with 'Unknown'
gdp = gdp.fillna(0)

# Preview cleaned data
print("Cleaned data preview:")
print(gdp.head())
# Add cleaned csv file
gdp.to_csv("./data/clean_gdp.csv", index=False)
