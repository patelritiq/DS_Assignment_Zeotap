import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

cust = pd.read_csv('Customers.csv')
trans = pd.read_csv('Transactions.csv')

#Preparing
trans['TransactionDate'] = pd.to_datetime(trans['TransactionDate'])
data = trans.merge(cust, on='CustomerID')
profile = data.groupby('CustomerID').agg(
    total_spent=('TotalValue', 'sum'),
    avg_spent=('TotalValue', 'mean'),
    num_trans=('TransactionID', 'count'),
    avg_quantity=('Quantity', 'mean')
).reset_index()

#Standardize features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(profile.iloc[:, 1:])

#optimal clusters & DB Index
db_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(scaled_data)
    db_score = davies_bouldin_score(scaled_data, labels)
    db_scores.append((k, db_score))

optimal_k = min(db_scores, key=lambda x: x[1])[0]

#Final with optimal K
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
profile['cluster'] = kmeans.fit_predict(scaled_data)

#visualization
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)
profile['pca1'], profile['pca2'] = reduced_data[:, 0], reduced_data[:, 1]


plt.figure(figsize=(10, 6))
for cluster in profile['cluster'].unique():
    subset = profile[profile['cluster'] == cluster]
    plt.scatter(subset['pca1'], subset['pca2'], label=f'Cluster {cluster}')
plt.title('Customer Segments')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.grid()
plt.show()

#results
print(f"Optimal number of clusters: {optimal_k}")
print(f"DB Index for optimal clusters: {min(db_scores, key=lambda x: x[1])[1]}")


