import pandas as pd

df = pd.read_table(
    "./popular-names.txt",
    header=None,
    sep="\t",
    names=["name", "sex", "number", "year"],
)
df_s = df.sort_values("number")
df_s.to_csv("./kada18.txt", sep=" ", header=None, index=False)
