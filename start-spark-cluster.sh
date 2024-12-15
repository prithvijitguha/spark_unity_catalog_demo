# Start Spark Master
$SPARK_HOME/sbin/start-master.sh


# Incase you want to add a worker node for reference
# Start Spark Worker

# We need to give it time to execute the command, otherwise they may remain disconnected
# sleep 10
# Start the Spark Worker with hostname to spark master
# $SPARK_HOME/sbin/start-worker.sh spark://$(hostname).:7077

# Create the temp directory for events if it does exist
mkdir -p /tmp/spark-events;

# We need to give it time to execute the command, otherwise they may remain disconnected
sleep 10

# Start The Spark History server
$SPARK_HOME/sbin/start-history-server.sh