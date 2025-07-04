# Retail ETL Pipeline Project

A simple, real-world ETL pipeline using **Apache Airflow** and **PySpark** to process retail transaction data. This project is designed to run locally on macOS, Windows, or Linux using only open-source tools.

---

## 📦 Project Structure
etl_pipeline_project/
├── dags/                       # Apache Airflow DAGs
│   └── retail_etl_dag.py       # Main DAG definition
│
├── spark_jobs/                # PySpark jobs
│   ├── clean_data.py           # Cleans raw retail data
│   └── aggregate_data.py       # Aggregates data for reporting
│
├── data/                      # Data directories
│   ├── raw/                    # Contains raw input CSV files
│   └── processed/              # Cleaned and transformed data
│
├── output/                    # Final report or analytics output
│   └── final_report.csv        # Generated after pipeline runs
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation


---

## 🛠️ Setup Instructions

### 1. **Clone the Repository**

```sh
git clone https://github.com/VaishArya/retail-etl-pipeline.git
cd retail-etl-pipeline/etl_pipeline_project
```

### 2. **Create and Activate Virtual Environment**

- **macOS/Linux:**
  ```sh
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Windows:**
  ```sh
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. **Install Requirements**

```sh
pip install -r requirements.txt
```

### 4. **Set Airflow Home**

- **macOS/Linux:**
  ```sh
  export AIRFLOW_HOME=$(pwd)/airflow_home
  ```
- **Windows:**
  ```sh
  set AIRFLOW_HOME=%cd%\airflow_home
  ```

### 5. **Symlink or Copy DAGs Folder (if needed)**

- **macOS/Linux:**
  ```sh
  rm -rf airflow_home/dags
  ln -s $(pwd)/dags airflow_home/dags
  ```
- **Windows (Command Prompt):**
  ```sh
  rmdir /S /Q airflow_home\dags
  mklink /D airflow_home\dags %cd%\dags
  ```

### 6. **Initialize Airflow and Create Admin User**

```sh
airflow db migrate
airflow users create ^
  --username your_username ^
  --firstname FirstName ^
  --lastname LastName ^
  --role Admin ^
  --email your_email@example.com ^
  --password your_secure_password
```
*(On Windows, use `^` for line continuation or put all options on one line.)*

---

## 📥 Download the Dataset

- **Option 1: UCI ML Repository**
  - Download [Online Retail Data Set (Excel)](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx)
  - Open in Excel/Google Sheets and save as `OnlineRetail.csv`
  - Place in `data/raw/OnlineRetail.csv`

- **Option 2: Kaggle**
  - Download from [Kaggle: Online Retail Customer Segmentation](https://www.kaggle.com/datasets/hellbuoy/online-retail-customer-segmentation)
  - Unzip and place `OnlineRetail.csv` in `data/raw/`

---

## 🚦 Running the Pipeline

1. **Start Airflow webserver:**
   ```sh
   source venv/bin/activate
   export AIRFLOW_HOME=$(pwd)/airflow_home
   airflow webserver
   ```
   *(On Windows: use `venv\Scripts\activate` and `set AIRFLOW_HOME=%cd%\airflow_home`)*

2. **Start Airflow scheduler (in another terminal):**
   ```sh
   source venv/bin/activate
   export AIRFLOW_HOME=$(pwd)/airflow_home
   airflow scheduler
   ```

3. **Open Airflow UI:**  
   Go to [http://localhost:8080](http://localhost:8080) and log in with your admin credentials.

4. **Trigger the DAG:**  
   - Find `retail_etl_dag` in the UI.
   - Turn it “on” (toggle switch).
   - Click the “play” button to trigger a run manually.

5. **Check Results:**  
   - After the DAG runs, check `output/final_report.csv` for your results.

---

## 🧪 Testing

- You can manually trigger the DAG from the Airflow UI.
- Check task logs in the UI for debugging.
- Inspect `output/final_report.csv` for the final aggregated results.

---

## 📝 What This Project Demonstrates

- **End-to-end orchestration** of a data pipeline using Airflow.
- **Data cleaning and aggregation** using PySpark.
- **Separation of concerns**: modular Spark jobs for each ETL step.
- **Portability**: runs on macOS, Windows, or Linux.
- **Best practices** for local data engineering projects.

---

## 🙋‍♂️ Author

- Vaishnavi Arya ([VaishArya on GitHub](https://github.com/VaishArya))

---

## 📄 License

MIT License



---


---

## 📄 License

MIT License
