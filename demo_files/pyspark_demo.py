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
        ("Jedi", "master"),
        ("Jedi", "master"),
        ("Jedi", "master"),
    ]
)

df.show()

df.write.format("parquet").save("jedi_table", mode="overwrite")

# %%
jedi_df = spark.read.parquet("jedi_table")

jedi_df.show()

# %%
spark.stop()

# %%



