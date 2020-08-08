# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．
import pandas as pd

df = pd.read_table(
    "/Users/hide/100knocks/kadai10_20/popular-names.txt",
    header=None,
    sep="\t",
    names=["name", "sex", "number", "year"],
)
col1 = df["name"]
col1.to_csv("./col1.txt", index=False, header=None)
print(col1.head())
col2 = df["sex"]
col2.to_csv("./col2.txt", index=False, header=None)
