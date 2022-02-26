# AWS EMR 6.4 - Spark 3.1.2 - Python3.7.5

You must export the variables indicating the source bucket name for JSON files and target bucket name for raw files.

export ENVIRON=PROD
export SRC_DIR=s3://bucket_src_name/
export SRC_FILE_FORMAT=json
export TGT_DIR=s3://bucket_target_name/
export TGT_FILE_FORMAT=parquet
export SRC_FILE_PATTERN=2021-01-1*

# Zip file

Generate Zip file of python files.

# Running Spark-Submit

Use one of these options to submit spark job.

spark-submit \
--master yarn \
--py-files zipfile.zip \
app.py

In case of the variables have not been previously set, use this command when submit spark.

spark-submit \
--master yarn \
--deploy-mode cluster \
--conf "spark.yarn.appMasterEnv.ENVIRON=PROD" \
--conf "spark.yarn.appMasterEnv.SRC_DIR=s3://SRC_Bucket_Name" \
--conf "spark.yarn.appMasterEnv.SRC_FILE_FORMAT=json" \
--conf "spark.yarn.appMasterEnv.TGT_DIR=s3://DST_Bucket_Name" \
--conf "spark.yarn.appMasterEnv.TGT_FILE_FORMAT=parquet" \
--conf "spark.yarn.appMasterEnv.SRC_FILE_PATTERN=2021-01-1*" \
--py-files zipfilename.zip \
app.py