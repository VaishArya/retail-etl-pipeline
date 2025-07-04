import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import re
import os

def standardize_col(col_name):
    col_name = col_name.strip().lower()
    col_name = re.sub(r'[^a-z0-9]+', '_', col_name)
    col_name = re.sub(r'_+', '_', col_name)
    return col_name.strip('_')

def main(input_path, output_path):
    spark = SparkSession.builder.appName('CleanRetailData').getOrCreate()
    df = spark.read.option('header', True).option('inferSchema', True).csv(input_path)

    # Standardize column names
    df = df.toDF(*[standardize_col(c) for c in df.columns])

    # Drop rows with any nulls
    df = df.dropna(how='any')

    # Remove duplicates
    df = df.dropDuplicates()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save cleaned data
    df.coalesce(1).write.option('header', True).mode('overwrite').csv(os.path.dirname(output_path))

    # Move the part file to the desired output path
    import glob, shutil
    part_file = glob.glob(os.path.join(os.path.dirname(output_path), 'part-*.csv'))[0]
    shutil.move(part_file, output_path)
    # Remove Spark metadata files
    for f in glob.glob(os.path.join(os.path.dirname(output_path), '_*')):
        os.remove(f)

    spark.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Clean raw retail data')
    parser.add_argument('--input', required=True, help='Path to raw input CSV')
    parser.add_argument('--output', required=True, help='Path to save cleaned CSV')
    args = parser.parse_args()
    main(args.input, args.output) 