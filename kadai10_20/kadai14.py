import pandas as pd

print("表示したい行数を指定してください")
number = int(input())
df = pd.read_table("./popular-names.txt", header=None)
print(df.head(number))
