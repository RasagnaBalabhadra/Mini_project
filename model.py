import pandas as pd
df = pd.read_csv("Churn_final_data.csv")
print(df.head())
X = df[['Customer','Satisfaction Score','Hours Spend o']]