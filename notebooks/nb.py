# Databricks notebook source
with open("/dbfs/mnt/man/image.txt", "r") as f_read:
    for line in f_read:
        print(line)

# COMMAND ----------

dbutils.fs.ls("/dbfs/FileStore")

# COMMAND ----------

from smart_open import smart_open
for line in smart_open('/dbfs/FileStore/image.txt', 'rb'):
    print(line.decode('utf8'))

# COMMAND ----------

pip install smart_open

# COMMAND ----------

dbutils.fs.ls("s3://ankitha-s3-test/")

# COMMAND ----------

dbutils.fs.mount(f"s3a://ankitha-s3-test", f"/mnt/man")

# COMMAND ----------

dbutils.fs.ls("/mnt/man/us_500.csv")

# COMMAND ----------

us_500.csv