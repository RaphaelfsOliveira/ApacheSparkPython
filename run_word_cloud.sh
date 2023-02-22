#!/bin/bash

echo '\n'
echo '[ ativando listener twitter ] \n'

python ./aula03_projeto_spark_streaming/listener_twitter.py 

echo '\n'
echo '[ armazenando dados parquet ] \n'

python ./aula05_projeto_spark_streaming/client_parquet.py

