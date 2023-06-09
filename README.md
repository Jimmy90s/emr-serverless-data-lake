# AWS: EMR Serverless Data Lake 
#### Skills: AWS - EMR - S3 - Athena - IAM - Spark - Hive - Tableau - Python - SQL - Data Pipeline 
[Dashboard Link](https://public.tableau.com/views/AWSDataLakeCrimeData/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link)
<div class='tableauPlaceholder' id='viz1685332763842' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;AW&#47;AWSDataLakeCrimeData&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='AWSDataLakeCrimeData&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;AW&#47;AWSDataLakeCrimeData&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>               


[Data Link](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)
- Created an S3 bucket with scripts, input and output folders where Chicago Crime data from 2001 to present with over 7 million rows was uploaded to the input folder, pulled from by a Spark job then a Hive job from the cleaned output folder to create a database and table that can have SQL queries ran against it.
- Used IAM to create multiple roles with a custom policy for permissions to use S3, EMR and Tableau or  PowerBi through Athena.
- Submitted a Spark job through the EMR Studio to pull from the S3 bucket to clean the dataset by properly casting and selecting only the important information.,
- Submitted a Hive job through the EMR Studio to create a database and table from the cleaned output in the S3 bucket.
- Designed a dashboard with Tableau from the cleaned data to explore and analyze.

![Welcome_Board](https://github.com/Jimmy90s/emr-serverless-data-lake/assets/103063112/5507f901-90a5-47af-9eb5-ab3d14d75697)
