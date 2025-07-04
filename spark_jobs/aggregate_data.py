import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum
import os

def main(input_path, output_path):
    spark = SparkSession.builder.appName('AggregateRetailData').getOrCreate()
    df = spark.read.option('header', True).option('inferSchema', True).csv(input_path)

    # Calculate total sales per country
    df = df.withColumn('total_sales', col('quantity') * col('unitprice'))
    agg_df = df.groupBy('country').agg(_sum('total_sales').alias('total_sales'))

    # Sort by total_sales descending
    agg_df = agg_df.orderBy(col('total_sales').desc())

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save aggregated data
    agg_df.coalesce(1).write.option('header', True).mode('overwrite').csv(os.path.dirname(output_path))

    # Move the part file to the desired output path
    import glob, shutil
    part_file = glob.glob(os.path.join(os.path.dirname(output_path), 'part-*.csv'))[0]
    shutil.move(part_file, output_path)
    # Remove Spark metadata files
    for f in glob.glob(os.path.join(os.path.dirname(output_path), '_*')):
        os.remove(f)

    spark.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Aggregate cleaned retail data')
    parser.add_argument('--input', required=True, help='Path to cleaned input CSV')
    parser.add_argument('--output', required=True, help='Path to save aggregated CSV')
    args = parser.parse_args()
    main(args.input, args.output) 