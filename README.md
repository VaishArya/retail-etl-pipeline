# Retail ETL Pipeline Project

A simple, real-world ETL pipeline using **Apache Airflow** and **PySpark** to process retail transaction data. This project is designed to run locally on macOS using only open-source tools.

---

## 📦 Project Structure

```
etl_pipeline_project/
├── dags/
│   └── retail_etl_dag.py
├── spark_jobs/
│   ├── clean_data.py
│   └── aggregate_data.py
├── data/
│   ├── raw/
│   └── processed/
├── output/
│   └── final_report.csv
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup Instructions (macOS)

1. **Clone this repository and navigate to the project folder:**
   ```sh
   cd etl_pipeline_project
   ```

2. **Create a Python virtual environment (recommended):**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Install Apache Airflow (initialize DB):**
   ```sh
   export AIRFLOW_HOME=$(pwd)/airflow_home
   airflow db init
   airflow users create \
      --username admin \
      --firstname Admin \
      --lastname User \
      --role Admin \
      --email admin@example.com \
      --password admin
   ```

5. **Download the dataset:**
   - Download `OnlineRetail.csv` from [UCI ML Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx).
   - Open the Excel file and save the first sheet as `OnlineRetail.csv`.
   - Place `OnlineRetail.csv` in `data/raw/`.

---

## 🚀 Running the Pipeline

1. **Start Airflow webserver and scheduler (in separate terminals):**
   ```sh
   export AIRFLOW_HOME=$(pwd)/airflow_home
   airflow webserver
   # In another terminal:
   airflow scheduler
   ```

2. **Trigger the DAG manually:**
   - Open [http://localhost:8080](http://localhost:8080) in your browser.
   - Enable and trigger the `retail_etl_dag`.

3. **Check the output:**
   - The final aggregated CSV will be saved as `output/final_report.csv`.

---

## 🧪 Testing

To test the pipeline end-to-end:
- Place the raw dataset in `data/raw/`.
- Trigger the DAG as above.
- Check `output/final_report.csv` for results.

---

## 🛠️ Tools Used
- Apache Airflow
- PySpark
- pandas
- macOS Terminal

---

## 📄 License
Open-source, for educational/demo purposes. 