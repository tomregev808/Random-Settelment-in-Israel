import pandas as pd

# Relative path to the file
df = pd.read_csv("data/raw_table.csv", encoding="utf-8", header=2)
df = df[df["StatArea"].isna()]
df = df.reset_index(drop=True)
df = df.drop(0)
df = df [["LocNameHeb", "pop_approx", "ReligionHeb", "hh_MidatDatiyut"]]

df.to_csv("data/settlements_clean.csv")