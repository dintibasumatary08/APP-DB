import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("churn.csv")
print(df.head())
print(df.info())

# Clean the data
df.columns = df.columns.str.strip()
df = df.drop_duplicates()
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Handle missing values
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(df["MonthlyCharges"].median())
df = df.fillna({col: "Unknown" for col in df.select_dtypes("object").columns})

# Summary statistics
print(df.describe())
print(df["Churn"].value_counts())

# Visualize patterns
df["Churn"].value_counts().plot(kind="bar", title="Churn Count")
plt.show()

df.groupby("Contract")["Churn"].value_counts(normalize=True).unstack().plot(
    kind="bar", title="Churn by Contract Type")
plt.show()

df.boxplot(column="MonthlyCharges", by="Churn")
plt.show()
