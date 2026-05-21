import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("sales_data.csv")
print(df)

# Missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove outliers
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)

IQR = Q3-Q1

lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR

df = df[(df["Age"]>=lower)&(df["Age"]<=upper)]

# New column
df["TotalAmount"] = df["Quantity"]*df["Price"]

print(df)

# Graph 1
sns.countplot(x="Gender",data=df)
plt.show()

# Graph 2
df.groupby("Category")["TotalAmount"].sum().plot(kind="bar")
plt.show()
df.to_csv("cleaned_sales.csv",index=True)
print("File saved successfully")