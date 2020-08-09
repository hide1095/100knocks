import re
import pandas as pd


df = pd.read_json("jawiki-country.json", lines=True)
uk_text = df.query('title=="イギリス"')["text"].values[0]
for section in re.findall(r"(=+)([^=]+)\1\n", uk_text):
    print(f"{section[1].strip()}\t{len(section[0]) - 1}")
