import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Load datasets
cust = pd.read_csv('../data/Customers.csv')
prod = pd.read_csv('../data/Products.csv')
trans = pd.read_csv('../data/Transactions.csv')

# Data preparation
cust['SignupDate'] = pd.to_datetime(cust['SignupDate'])
trans['TransactionDate'] = pd.to_datetime(trans['TransactionDate'])
data = trans.merge(cust, on='CustomerID').merge(prod, on='ProductID')
data = data.drop(columns=['Price_y'])
data.rename(columns={'Price_x': 'Price'}, inplace=True)
data['Spend'] = data['Quantity'] * data['Price']

# Create customer profiles
profiles = data.groupby('CustomerID').agg({
    'Spend': 'sum',
    'Quantity': 'sum',
    'Region': lambda x: x.mode()[0],
    'Category': lambda x: ','.join(x.mode())
}).reset_index()

# Encode categorical data
region_enc = pd.get_dummies(profiles['Region'], prefix='Region')
cat_enc = pd.get_dummies(profiles['Category'], prefix='Cat')
features = pd.concat([profiles[['Spend', 'Quantity']], region_enc, cat_enc], axis=1)

# Standardize features
scaler = StandardScaler()
scaled_feat = scaler.fit_transform(features)

# Calculate similarity matrix
sim_matrix = cosine_similarity(scaled_feat)
sim_df = pd.DataFrame(sim_matrix, index=profiles['CustomerID'], columns=profiles['CustomerID'])

# Generate lookalike recommendations
lookalikes = {}
for cid in profiles['CustomerID'][:20]:  
    similar = sim_df[cid].sort_values(ascending=False)[1:4] 
    lookalikes[cid] = list(zip(similar.index, similar.values))

# Save results
output = pd.DataFrame({
    'CustomerID': list(lookalikes.keys()),
    'SimilarCustomers': [x for x in lookalikes.values()]
})
output.to_csv('../output/lookalike_results.csv', index=False)

print(f"Lookalike recommendations generated for {len(lookalikes)} customers")
print(f"Results saved to: ../output/lookalike_results.csv")

#example
print("Sample Lookalike Recommendations:")
print(output.head())
