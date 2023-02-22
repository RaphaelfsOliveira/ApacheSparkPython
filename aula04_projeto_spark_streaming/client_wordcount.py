from pyspark.sql import SparkSession
from pyspark.sql import functions as f

spark = SparkSession.builder\
    .config('spark.driver.host', '127.0.0.1')\
    .appName('SparkStreaming')\
    .getOrCreate()

dflines = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9009) \
    .load()

# explode separa em linhas 
# split separar palavra por palavra
dfWords = dflines.select(f.explode(f.split(dflines.value, ' ')).alias('word'))

dfWordCounts = dfWords.groupBy('word').count()

query = dfWordCounts.writeStream \
    .outputMode('complete') \
    .format('console') \
    .start()

query.awaitTermination()