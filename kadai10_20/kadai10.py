# 10
import pandas as pd

df = pd.read_table(
    "/Users/hide/100knocks/popular-names.txt",
    header=None,
    sep="\t",
    names=["name", "sex", "number", "year"],
)
print(len(df))


print(pd.__version__)