from pyspark.sql import SparkSession
import shutil

HOST = '127.0.0.1'
PORT = 9009
PATH = '../datalake/twitter'

for item in [f'{PATH}/parquet/', f'{PATH}/check/']:
    try:
        shutil.rmtree(item)
    except OSError as err:
        print(f'Erro: {err.strerror}')

spark = SparkSession.builder\
    .config('spark.driver.host', '127.0.0.1')\
    .appName('SparkStreaming')\
    .getOrCreate()

dfTweets = spark.readStream\
    .format('socket')\
    .option('host', HOST)\
    .option('port', PORT)\
    .load()

query = dfTweets.writeStream\
    .outputMode('append')\
    .option('encoding', 'utf-8')\
    .format('csv')\
    .option('path', f'{PATH}/parquet')\
    .option('checkpointLocation', f'{PATH}/check')\
    .start()

query.awaitTermination()