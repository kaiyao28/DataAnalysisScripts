import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

# ── INSPECT ────────────────────────────────────────────────────────────────────
df.shape
nrows, ncols = df.shape                    # or df.shape[0], df.shape[1]
df.dtypes
df.head()
df.tail()
df.info()
df.describe(include="all")

# ── MISSING VALUES ─────────────────────────────────────────────────────────────
df.isnull().sum()                          # count per column
df.isnull().mean() * 100                   # % missing per column

df.dropna()                                # drop any row with NaN
df.dropna(subset=["col1", "col2"])         # drop only if specific cols are NaN
df.dropna(thresh=5)                        # keep rows with at least 5 non-NaN

df["col"].fillna(0)                        # fill with constant
df["col"].fillna(df["col"].mean())         # fill with mean
df["col"].fillna(df["col"].median())       # fill with median
df["col"].fillna(method="ffill")           # forward fill
df["col"].fillna(method="bfill")           # backward fill
df.fillna(df.mean(numeric_only=True))      # fill all numeric cols with their mean

# ── DUPLICATES ─────────────────────────────────────────────────────────────────
df.duplicated().sum()                      # count duplicate rows
df.drop_duplicates()                       # remove duplicate rows
df.drop_duplicates(subset=["id"])          # deduplicate by column(s)
df.drop_duplicates(keep="last")            # keep last occurrence

# ── DATA TYPES ─────────────────────────────────────────────────────────────────
df["col"].astype(int)
df["col"].astype(float)
df["col"].astype(str)
df["col"].astype("category")

pd.to_numeric(df["col"], errors="coerce") # non-numeric → NaN
pd.to_datetime(df["date_col"])
pd.to_datetime(df["date_col"], format="%Y-%m-%d")

# ── OUTLIERS ───────────────────────────────────────────────────────────────────
# IQR method
Q1 = df["col"].quantile(0.25)
Q3 = df["col"].quantile(0.75)
IQR = Q3 - Q1
df_clean = df[(df["col"] >= Q1 - 1.5 * IQR) & (df["col"] <= Q3 + 1.5 * IQR)]

# Z-score method
from scipy import stats
z = np.abs(stats.zscore(df["col"].dropna()))
df_clean = df[z < 3]

# clip instead of remove
df["col"] = df["col"].clip(lower=0, upper=100)

# ── STRING CLEANING ────────────────────────────────────────────────────────────
df["col"].str.strip()                      # remove whitespace
df["col"].str.lower()
df["col"].str.upper()
df["col"].str.replace(" ", "_")
df["col"].str.replace(r"[^a-zA-Z0-9]", "", regex=True)  # remove special chars
df["col"].str.contains("pattern")
df["col"].str.startswith("prefix")
df["col"].str.split(",").str[0]            # split and take first part
df["col"].str.extract(r"(\d+)")            # extract with regex

# ── COLUMN OPERATIONS ──────────────────────────────────────────────────────────
df.rename(columns={"old": "new"})
df.drop(columns=["col1", "col2"])
df.columns = df.columns.str.lower().str.replace(" ", "_")  # clean all col names

# reorder columns
cols = ["id", "name"] + [c for c in df.columns if c not in ["id", "name"]]
df = df[cols]
