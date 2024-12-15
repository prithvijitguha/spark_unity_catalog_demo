# %%

# %%
from pyspark.sql import SparkSession
from datetime import datetime

curr_timestamp = datetime.now()
spark = SparkSession.builder.appName(f"{curr_timestamp}").getOrCreate()

spark.version

# %%
df = spark.createDataFrame(
    [
        ("jedi", "master", "anakin", ),
        ("jedi", "master", "yoda", ),
        ("jedi", "master", "obiwan", ),
        ("sith", "master", "palpatine", ),
    ],
    ["team", "rank", "name"]
)

df.show()

df.write.format("parquet").save("data/jedi_table", mode="overwrite")

# %%
jedi_df = spark.read.parquet("data/jedi_table")

jedi_df.show()

# %%
spark.stop()

# %%



