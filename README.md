# kafka-lab
Windows instruction

Instructions for downloading and setting up kafka are taken from the video: https://www.youtube.com/watch?v=BwYFuhVhshI

1.Download kafka from https://downloads.apache.org/kafka/3.6.0/kafka_2.13-3.6.0.tgz

2.Extract archive and rename folder to “kafka”.

3.Open file kafka/config/server.properties and change log.dirs to path_to_kafka/kafka/kafka-logs.

4.Open file kafka/config/zookeeper.properties and change dataDir to path_to_kafka/kafka/zookeeper-data.

5.Open command line as administrator and run next commands for running zookeeper server:

cd path_to_kafka

.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

6.Don’t close command window.

7.Open command line as administrator and run next commands for running kafka server:

cd path_to_kafka

.\bin\windows\kafka-server-start.bat .\config\server.properties

8.Don’t close command window.

9.Install python libraries from requirements.txt
pip install -r requirements.txt

10.Run producer.py

11.Run consumer.py
