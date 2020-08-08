import pandas as pd

print("分割したい数を指定してください")
number = int(input())
df = pd.read_table("./popular-names.txt", header=None)
n = int(2780 / number)
start = 0
end = n
df_cut = pd.DataFrame()

for i in range(number):
    df_label = df[start : end - 1]
    df_label["label"] = i
    start += n
    end += n
    df_cut = pd.concat([df_cut, df_label], axis=0)


df_cut.to_csv("./kadai16.txt", sep=" ", header=None, index=False)
