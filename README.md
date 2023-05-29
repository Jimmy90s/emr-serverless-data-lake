# AWS: EMR Serverless Data Lake 
#### Skills: AWS - EMR - S3 - Athena - IAM - Spark - Hive - Tableau - Python - SQL - Data Pipeline 
[Data Link](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)
- Created an S3 bucket with scripts, input and output folders where Chicago Crime data from 2001 to present with over 7 million rows was uploaded to the input folder, pulled from by a Spark job then a Hive job from the cleaned output folder to create a database and table that can have SQL queries ran against it.
- Used IAM to create multiple roles with a custom policy for permissions to use S3, EMR and Tableau or  PowerBi through Athena.
- Submitted a Spark job through the EMR Studio to pull from the S3 bucket to clean the dataset by properly casting and selecting only the important information.,
- Submitted a Hive job through the EMR Studio to create a database and table from the cleaned output in the S3 bucket.
- Designed a dashboard with Tableau from the cleaned data to explore and analyze.
