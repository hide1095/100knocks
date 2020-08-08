import pandas as pd

df = pd.read_table(
    "./popular-names.txt",
    header=None,
    sep="\t",
    names=["name", "sex", "number", "year"],
)
df = df.groupby("name")
print(len(df))
