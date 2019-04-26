#!/bin/bash

hadoop fs -rm -r /user/liyunfan/output
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.8.5.jar \
        -input hdfs://localhost:8000/user/liyunfan/input/N1.txt \
        -input hdfs://localhost:8000/user/liyunfan/input/D1.txt \
        -output ./output \
        -file map.py \
        -file red.py \
        -mapper "python map.py" \
        -reducer "python red.py" \
        -jobconf mapred.reduce.tasks=1 \
        -jobconf mapred.job.name="streaming_test"
