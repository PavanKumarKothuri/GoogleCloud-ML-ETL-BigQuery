# **GCP Data Pipeline for ML - ETL on BigQuery** 🏗️🚀  

📌 **Tech Stack:** `Python` | `Pandas` | `Google Cloud Storage (GCS)` | `BigQuery` | `gCloud CLI`  

📌 **Business Goal:** Build a **scalable data pipeline** to clean, transform, and analyze large datasets for **Machine Learning and Business Intelligence**.  

📌 **Problem Solved:** Companies deal with **raw, messy data** that needs to be **cleaned, processed, and stored efficiently** before ML models can use it. This project automates the **Extract, Transform, Load (ETL) process** using **GCP services** and **Python**.  

---

## 🚀 **Project Overview**  
This project automates **data ingestion, transformation, and storage** using **Google Cloud** services. The ETL pipeline extracts raw data from **CSV files**, cleans it using **Pandas**, and loads it into **BigQuery** for analysis. The entire process is **automated using Python & gCloud CLI**.  

✅ **Fully automated with Python & Cloud CLI**  
✅ **Minimal manual setup** for efficiency  
✅ **Scalable, cost-effective & secure**  
✅ **Supports large datasets without performance issues**  

---

## ⚡ **Project Architecture**  

🔹 **Extract**: Raw CSV data is uploaded to **Google Cloud Storage (GCS)**.  
🔹 **Transform**: Data cleaning, type conversion, and feature engineering using **Pandas**.  
🔹 **Load**: The cleaned data is loaded into **BigQuery** for SQL-based querying.  

📌 **Workflow:**  
1️⃣ Upload raw data to **Cloud Storage** 📤  
2️⃣ Python script cleans and processes the data 🧹  
3️⃣ Processed data is loaded into **BigQuery** 🎯  
4️⃣ Run SQL queries to analyze insights 📊  

---

## 🛠 **Technical Implementation**  

### **1️⃣ File Structure** 📂  
```
gcp-etl/
│── config.py               # GCP project & bucket details  
│── upload_to_gcs.py        # Upload raw data to Cloud Storage  
│── transform_data.py       # Clean & process data using Pandas  
│── load_to_bigquery.py     # Load transformed data into BigQuery  
│── query_bigquery.py       # Run SQL queries on BigQuery  
│── requirements.txt        # Python dependencies  
│── sample_data.csv         # Sample dataset  
│── README.md               # Project documentation  
```

---

### **2️⃣ Setup & Deployment** 🚀  

#### **🔹 Step 1: Set up Google Cloud Project**  
```sh
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

#### **🔹 Step 2: Enable Required Services**  
```sh
gcloud services enable storage.googleapis.com
gcloud services enable bigquery.googleapis.com
```

#### **🔹 Step 3: Install Dependencies & Activate Virtual Environment**  
```sh
python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
```

#### **🔹 Step 4: Upload Data to Cloud Storage**  
```sh
python upload_to_gcs.py
```

#### **🔹 Step 5: Transform Data using Pandas**  
```sh
python transform_data.py
```

#### **🔹 Step 6: Load Data into BigQuery**  
```sh
python load_to_bigquery.py
```

#### **🔹 Step 7: Query Data from BigQuery**  
```sh
python query_bigquery.py
```

---

## 🌟 **Challenges & Solutions**  

| Challenge 🤯 | Solution ✅ |
|-------------|------------|
| Large datasets slowing down processing 🚀 | Used **BigQuery’s distributed SQL engine** for fast queries. |
| Manual data uploads were inefficient ⏳ | Automated **Cloud Storage uploads** with `gcloud` and Python. |
| Schema mismatches when loading into BigQuery ❌ | Used **data type conversion & schema validation** in Pandas. |
| Cost optimization for BigQuery usage 💸 | **Pay-per-query model** and **table partitioning** to reduce costs. |
| Security & Access Control 🔒 | **IAM roles** and **Service Accounts** to restrict permissions. |

---

## 📈 **Business Impact**  

✅ **Faster Decision Making**: Processed data is **immediately available** for business insights.  
✅ **Scalability**: Works for **both small and large datasets** without infrastructure concerns.  
✅ **Automation**: Reduces **manual errors** and **improves efficiency** in ETL workflows.  
✅ **Cost-Efficient**: Pay-as-you-go model saves money compared to traditional databases.  

---

## 🔥 **Future Improvements**  

✅ **Integrate Apache Airflow** for orchestration 🎯  
✅ **Implement real-time streaming** with **Pub/Sub & Dataflow** 📡  
✅ **Use BigQuery ML** for direct machine learning model training 🤖  
✅ **Deploy on Google Cloud Functions** for serverless execution 🌐  

---

## 🎯 **Conclusion**  

This **GCP Data Pipeline** is a **powerful, scalable, and automated** ETL solution. It allows businesses to **process raw data efficiently** and **gain real-time insights** using BigQuery. The **automation** reduces human effort, and the **cloud-based architecture** ensures **high availability and security**.  

---

## ⭐ **Contribute & Connect**  
Built with ❤️ by **PavanKumar Kothuri** – 🚀 **Coding is Fun!** 😃  

- 🌐 [LinkedIn Profile](https://www.linkedin.com/in/Pavankumarkothuri/)
- 💻 [GitHub Profile](https://github.com/PavanKumarKothuri)  
- ✉️ [Email: pavankumarkothuri9@gmail.com](mailto:pavankumarkothuri9@gmail.com)

Feel free to connect with me for further discussions or contributions. 🌟 **Happy Coding!** 🚀