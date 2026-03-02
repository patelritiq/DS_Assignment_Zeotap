# Customer Analytics & Segmentation 📊

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-green.svg)](https://pandas.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive data science project for customer analytics, segmentation, and lookalike modeling. Built as an assignment for [Zeotap](https://github.com/zeotap) Data Science internship position (January 2025).

---

## Project Statistics 📈

- **200 customers** analyzed
- **1,000 transactions** processed
- **5 customer segments** identified (K-Means clustering)
- **Davies-Bouldin Index: 1.05** (optimal clustering quality)
- **3 analysis modules** (EDA, Clustering, Lookalike)
- **20 lookalike recommendations** generated
- **4 key features** (Total Spend, Avg Spend, Transaction Count, Avg Quantity)

---

## Project Overview 🎯

This project demonstrates end-to-end customer analytics capabilities including exploratory data analysis, customer segmentation using machine learning, and lookalike modeling for targeted marketing. Developed as part of the Zeotap Data Scientist internship assessment.

### Assignment Context
- **Company**: Zeotap (Customer Data Platform)
- **Position**: Data Science Internship
- **Date**: January 2025
- **Objective**: Demonstrate data science skills in customer analytics and segmentation

### Key Objectives
1. **Exploratory Data Analysis (EDA)**: Analyze customer, product, and transaction data
2. **Customer Segmentation**: Group customers using K-Means clustering
3. **Lookalike Modeling**: Identify similar customers for targeted campaigns

---

## Data Science Skills Demonstrated 🔬

### Machine Learning
- K-Means clustering for customer segmentation
- Davies-Bouldin Index for cluster quality evaluation
- PCA (Principal Component Analysis) for dimensionality reduction
- Cosine similarity for lookalike modeling

### Data Analysis
- Exploratory Data Analysis (EDA)
- Feature engineering and aggregation
- Data merging and transformation
- Statistical analysis and profiling

### Data Preprocessing
- StandardScaler for feature normalization
- One-hot encoding for categorical variables
- DateTime parsing and manipulation
- Missing value handling

---

## Project Structure 📁

```
DS_Assignment_Zeotap/
├── data/
│   ├── Customers.csv          # Customer profiles (200 records)
│   ├── Products.csv           # Product catalog
│   └── Transactions.csv       # Transaction history (1,000 records)
├── src/
│   ├── eda.py                 # Exploratory Data Analysis
│   ├── clustering.py          # Customer Segmentation (K-Means)
│   └── lookalike.py           # Lookalike Modeling
├── reports/
│   ├── eda_report.pdf         # EDA insights and visualizations
│   └── clustering_report.pdf  # Segmentation analysis and recommendations
├── output/
│   └── lookalike_results.csv  # Lookalike recommendations
├── .gitignore
├── LICENSE
└── README.md
```

---

## Installation & Setup 🛠️

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/patelritiq/DS_Assignment_Zeotap.git
   cd DS_Assignment_Zeotap
   ```

2. **Install required libraries:**
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

---

## Usage 📖

### 1. Exploratory Data Analysis (EDA)

Analyze datasets and visualize insights:

```bash
cd src
python eda.py
```

**Output:**
- Data summaries and statistics
- Most purchased products
- Customer behavior patterns

**Report:** See `reports/eda_report.pdf` for detailed insights and business recommendations.

---

### 2. Customer Segmentation (Clustering)

Perform K-Means clustering to segment customers:

```bash
cd src
python clustering.py
```

**Output:**
- Optimal number of clusters: 5
- Davies-Bouldin Index: 1.05
- PCA visualization of customer segments

**Report:** See `reports/clustering_report.pdf` for detailed segmentation analysis.

---

### 3. Lookalike Modeling

Generate similar customer recommendations:

```bash
cd src
python lookalike.py
```

**Output:**
- Lookalike recommendations for 20 customers
- Results saved to `output/lookalike_results.csv`

---

## Customer Segmentation Results 🎯

### 5 Customer Segments Identified

| Cluster | Description | Characteristics | Recommendation |
|---------|-------------|-----------------|----------------|
| **Cluster 0** | High-Frequency Buyers | Medium spending, active engagement | Loyalty programs, personalized offers |
| **Cluster 1** | Occasional Buyers | Low frequency, low spending | Basic incentives, re-engagement campaigns |
| **Cluster 2** | High-Value Customers | Significant spending, moderate engagement | Premium services, upselling strategies |
| **Cluster 3** | Inactive Customers | Very little activity | Reactivation campaigns, personalized offers |
| **Cluster 4** | Moderate Spenders | Frequent purchases, consistent engagement | Increase basket size, bundled products |

### Clustering Methodology

- **Algorithm**: K-Means (chosen for efficiency and interpretability)
- **Features**: Total Spend, Avg Spend, Transaction Count, Avg Quantity
- **Optimization**: Davies-Bouldin Index (lower = better)
- **Visualization**: PCA for 2D representation

---

## Key Findings 📊

### Dataset Overview
- **Customers**: 200 unique customers
- **Transactions**: 1,000 transaction records
- **Products**: Multiple product categories
- **Regions**: Multiple geographic regions

### Segmentation Quality
- **Optimal Clusters**: 5 segments
- **Davies-Bouldin Index**: 1.05 (acceptable quality)
- **Clear Separation**: PCA visualization shows distinct clusters

### Business Impact
- Enables targeted marketing campaigns
- Identifies high-value customer segments
- Supports personalized customer engagement
- Facilitates lookalike audience targeting

---

## Future Enhancements 🔮

- [ ] Hierarchical clustering for comparison
- [ ] DBSCAN for density-based segmentation
- [ ] Time-series analysis for customer lifetime value
- [ ] Churn prediction modeling
- [ ] Real-time recommendation system
- [ ] Interactive dashboard (Streamlit/Dash)
- [ ] A/B testing framework
- [ ] Advanced feature engineering (RFM analysis)

---

## Reports & Documentation 📄

Detailed analysis reports are available in the `reports/` folder:

- **EDA Report** (`eda_report.pdf`): Comprehensive exploratory analysis with visualizations and business insights
- **Clustering Report** (`clustering_report.pdf`): Customer segmentation analysis with cluster descriptions and recommendations

---

## Technologies Used 💻

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning algorithms
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical visualizations

---

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author 👨‍💻

**Ritik Pratap Singh Patel**

- Data Science & Machine Learning Enthusiast
- **Email**: patelritiq@gmail.com

---

## Acknowledgments 🙏

This project was developed as an assignment for Zeotap's Data Scientist position. It demonstrates practical application of data science techniques for customer analytics and segmentation.

**Zeotap**: [https://github.com/zeotap](https://github.com/zeotap)

---

## Quick Start 🚀

```bash
# Clone repository
git clone https://github.com/patelritiq/DS_Assignment_Zeotap.git
cd DS_Assignment_Zeotap

# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# Run EDA
cd src
python eda.py

# Run Clustering
python clustering.py

# Run Lookalike Modeling
python lookalike.py
```

Transform customer data into actionable insights! 📊✨
