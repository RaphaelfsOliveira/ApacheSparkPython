from pyspark.sql import SparkSession
from pyspark.sql import functions as f

spark = SparkSession.builder\
    .config('spark.driver.host', '127.0.0.1')\
    .appName('SparkStreaming')\
    .getOrCreate()

lines = spark.readStream\
    .format('socket')\
    .option('host', 'localhost')\
    .option('port', 9009) \
    .load()

words = lines.select(
    f.explode(
        f.split(lines.value, ' ')
    ).alias('word')
)

wordCounts = words.groupBy('word').count()

query = wordCounts.writeStream \
    .outputMode('complete') \
    .format('console') \
    .start()

query.awaitTermination()