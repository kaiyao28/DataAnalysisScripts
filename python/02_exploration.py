import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

# ── QUICK OVERVIEW ─────────────────────────────────────────────────────────────
df.shape                                   # (rows, cols)
df.dtypes                                  # column types
df.nunique()                               # unique values per column
df.describe()                              # numeric stats
df.describe(include="object")             # string/categorical stats

# ── VALUE COUNTS ───────────────────────────────────────────────────────────────
df["col"].value_counts()
df["col"].value_counts(normalize=True)     # as proportions
df["col"].value_counts(dropna=False)       # include NaN

# ── DISTRIBUTIONS ──────────────────────────────────────────────────────────────
df["col"].mean()
df["col"].median()
df["col"].std()
df["col"].var()
df["col"].min()
df["col"].max()
df["col"].quantile([0.25, 0.5, 0.75])
df["col"].skew()
df["col"].kurt()

# ── CORRELATIONS ───────────────────────────────────────────────────────────────
df.corr(numeric_only=True)                # pairwise Pearson correlation
df.corr(method="spearman", numeric_only=True)
df["col1"].corr(df["col2"])               # single pair

# strongest correlations with target
corr = df.corr(numeric_only=True)["target"].drop("target").abs()
corr.sort_values(ascending=False).head(10)

# ── GROUPBY SUMMARY ────────────────────────────────────────────────────────────
df.groupby("group_col")["value_col"].mean()
df.groupby("group_col")["value_col"].agg(["mean", "std", "count"])
df.groupby("group_col").agg({"col1": "mean", "col2": "sum"})

# ── CROSS-TABULATION ───────────────────────────────────────────────────────────
pd.crosstab(df["cat1"], df["cat2"])
pd.crosstab(df["cat1"], df["cat2"], normalize="index")  # row proportions

# ── SAMPLING ───────────────────────────────────────────────────────────────────
df.sample(n=100)                           # random 100 rows
df.sample(frac=0.1, random_state=42)      # random 10%

# ── QUICK PLOTS (requires matplotlib) ─────────────────────────────────────────
import matplotlib.pyplot as plt

df["col"].hist(bins=30)
df.boxplot(column="value", by="group")
df.plot(kind="scatter", x="col1", y="col2")
df["col"].value_counts().plot(kind="bar")
df.corr(numeric_only=True).style.background_gradient(cmap="coolwarm")  # in Jupyter
