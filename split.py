import pandas as pd

# Load the dataset
df = pd.read_csv('transaction_data_copy.csv')

# Drop the columns: nameOrig, nameDest
df.drop(['step', 'nameOrig', 'nameDest'], axis=1, inplace=True)
df = pd.get_dummies(df, columns=['type'])

df.head()
fraud_df = df[df['isFraud'] == 1]  # Assuming isFraud is numeric
non_fraud_df = df[df['isFraud'] == 0]  # Assuming isFraud is numeric

# The target is to have the new dataframe (new_df) with a fraction of the size of the
# original dataframe (df)
# Calculate how many non-fraudulent transactions we need to include to achieve this, after including all fraud transactions
non_fraud_needed = max(df.shape[0] // 6 - fraud_df.shape[0], 0)  # Ensure non-negative

# If there are more fraud rows than half of the dataset, adjust non_fraud_needed to 0
non_fraud_needed = min(non_fraud_needed, non_fraud_df.shape[0])

# Randomly select non-fraudulent transactions if needed
selected_non_fraud = non_fraud_df.sample(n=non_fraud_needed, random_state=42) if non_fraud_needed > 0 else pd.DataFrame()

# Combine the two sets of rows
new_df = pd.concat([fraud_df, selected_non_fraud])

# Optional: Shuffle the new DataFrame to mix fraudulent and non-fraudulent rows
new_df = new_df.sample(frac=1, random_state=42).reset_index(drop=True)

for column in new_df.columns:
    print("{}: {}".format(column, new_df[column].dtypes))
# Save the new DataFrame to a new CSV file
new_df.to_csv('half_transaction_data.csv', index=False)
