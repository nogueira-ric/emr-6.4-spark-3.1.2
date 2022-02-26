import os
# Spark session is imported from util.py
from util import get_spark_session
from read import from_files
from process import transform
from write import to_files


# Defining the main function
def main():
    env = os.environ.get('ENVIRON')
    src_dir = os.environ.get('SRC_DIR')
    # In the production environment you may need to read different pattern of file at the same time
    # So that, you can use the option -* at the end of the src_file_pattern variable as shown below.
    src_file_pattern = f'{os.environ.get("SRC_FILE_PATTERN")}-*'
    src_file_format = os.environ.get('SRC_FILE_FORMAT')
    tgt_dir = os.environ.get('TGT_DIR')
    tgt_file_format = os.environ.get('TGT_FILE_FORMAT')
    spark = get_spark_session(env, 'GitHub Activity - Getting Started')
    df = from_files(spark, src_dir, src_file_pattern, src_file_format)
    df_transformed = transform(df)
    # df_transformed.printSchema()
    # df_transformed.select('repo.*', 'created_at', 'year', 'month', 'day'). \
    # show()
    to_files(df_transformed, tgt_dir, tgt_file_format)


# In case of the main function is required, it will be requested.
if __name__ == '__main__':
    main()
