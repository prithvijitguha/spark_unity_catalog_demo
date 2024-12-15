# Download the spark tarball
wget https://dlcdn.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz;
# Unzip the file
tar -xvzf spark-3.5.3-bin-hadoop3.tgz;
# Move it to opt
sudo mv spark-3.5.3-bin-hadoop3 /opt/;
# Rename from the Spark version to just 'spark'
sudo mv /opt/spark-3.5.3-bin-hadoop3 /opt/spark;
