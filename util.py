from pyspark.sql import SparkSession


def get_spark_session(env, app_name):
    # Supposedly you are running on local environment, you gotta check that
    if env == 'DEV':
        spark = SparkSession. \
            builder. \
            master('local'). \
            appName(app_name). \
            getOrCreate()
        return spark
    # With this additional code we will be able to run this code in prod
    # Even though in AWS ERM or Cloudera
    elif env == 'PROD':
        spark = SparkSession. \
            builder. \
            master('yarn'). \
            appName(app_name). \
            getOrCreate()
        return spark
