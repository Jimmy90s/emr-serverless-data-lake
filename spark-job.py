#
# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at
#
#      http://aws.amazon.com/asl/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#

import os
import sys
import pyspark.sql.functions as F
from pyspark.sql import SparkSession

from pyspark import SparkContext
sc = SparkContext.getOrCreate()

from pyspark.sql.functions import  substring ,to_date, col, lit


if __name__ == "__main__":
    """
        Usage: wordcount [destination path]
    """
    spark = SparkSession\
        .builder\
        .appName("Data-Processing")\
        .getOrCreate()

    output_path = 's3://james-laurie-emr/output'

    #if len(sys.argv) > 1:
    #    output_path = sys.argv[1]
    #else:
    #    print("S3 output location not specified printing top 10 results to output stream")
    region = os.getenv("AWS_REGION")

    # Convert date from string to date data type & Clean Block Coloumn
    text_file = spark.read.csv('s3://james-laurie-emr/input/Crimes_-_2001_to_Present.csv',header=True).withColumn('Date',to_date(col('Date'), 'MM/dd/yyyy hh:mm:ss a') ).withColumn('Block',substring('Block', 7,99))
    
 
    # Select only important columns
    cols = [
 'ID',
 'Case Number',
 'Date',
 'Block',
 'Primary Type',
 'Description',
 'Location Description',
 'Arrest',
 'Domestic',
 'Beat',
 'District',
 'Ward',
 'Community Area',
 'FBI Code',
 'Latitude',
 'Longitude',
]
    counts = text_file.select(cols)
    # Convert to DataFrame
    counts_df = counts.toDF('ID',
 'Case Number',
 'Date',
 'Block',
 'Primary Type',
 'Description',
 'Location Description',
 'Arrest',
 'Domestic',
 'Beat',
 'District',
 'Ward',
 'Community Area',
 'FBI Code',
 'Latitude',
 'Longitude',)

    if output_path:
        counts_df.write.mode("overwrite").csv(output_path)
        print("WordCount job completed successfully. Refer output at S3 path: " + output_path)
    else:
        counts_df.show(10, False)
        print("WordCount job completed successfully.")

    spark.stop()
    