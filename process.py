import pandas as pd
import numpy as np
import os
import datetime

os.chdir("raw")
files = [n for n in os.listdir() if n.startswith("c")]
files.sort()

df = pd.DataFrame()

count_ = 1

for file in files:
    print(f"Processing file {count_} of {len(files)}")
    dicto = pd.read_excel(file, sheet_name=None)
    if "1b" in dicto.keys():
        sheet = pd.read_excel(file, sheet_name="1b")
    elif "1b " in dicto.keys():
        sheet = pd.read_excel(file, sheet_name="1b ")
    elif "2" in dicto.keys():
        sheet = pd.read_excel(file, sheet_name="2")
    else:
        raise (IndexError)
    df = df.append(sheet.iloc[5:-10, :2].copy().dropna(), ignore_index=True)
    count_ += 1

df.columns = ["dte", "pc"]
df["dte"] = pd.to_datetime(df["dte"]).dt.date
output = df.drop_duplicates(subset="dte", keep="last").copy().reset_index(drop=True)
output["pc"] = np.where(
    output["dte"] >= datetime.date(2021, 5, 10), output["pc"] / 100, output["pc"]
)

output.to_csv("output.csv", index=False)
