# 13
import pandas as pd

col1 = pd.read_table("./col1.txt")
col2 = pd.read_table("./col2.txt")
merged_kadai13 = pd.concat([col1, col2], axis=1)
merged_kadai13.to_csv("./kadai13.txt", sep="\t", index=False)
