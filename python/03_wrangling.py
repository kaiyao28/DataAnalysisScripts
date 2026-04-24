import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

# ── FILTER / SELECT ────────────────────────────────────────────────────────────
df[df["col"] > 10]
df[(df["col1"] > 10) & (df["col2"] == "A")]
df[df["col"].isin(["A", "B", "C"])]
df[~df["col"].isin(["X"])]                # NOT in
df[df["col"].notna()]                      # exclude NaN
df[df["col"].str.contains("pattern")]

df.query("col1 > 10 and col2 == 'A'")     # query string syntax

# ── SELECT COLUMNS ─────────────────────────────────────────────────────────────
df[["col1", "col2"]]
df.select_dtypes(include="number")
df.select_dtypes(include=["object", "category"])
df.filter(like="prefix")                  # cols whose name contains string
df.filter(regex=r"^col_\d+$")

# ── SORT ───────────────────────────────────────────────────────────────────────
df.sort_values("col")
df.sort_values("col", ascending=False)
df.sort_values(["col1", "col2"], ascending=[True, False])
df.nlargest(10, "col")
df.nsmallest(10, "col")

# ── ADD / TRANSFORM COLUMNS ────────────────────────────────────────────────────
df["new"] = df["col1"] + df["col2"]
df["log_col"] = np.log1p(df["col"])       # log(1+x) — safe for zeros
df["z_score"] = (df["col"] - df["col"].mean()) / df["col"].std()
df["binned"] = pd.cut(df["col"], bins=5)
df["binned"] = pd.cut(df["col"], bins=[0, 18, 35, 60, 100], labels=["<18", "18-35", "35-60", "60+"])
df["rank"] = df["col"].rank(pct=True)     # percentile rank

df["new"] = df["col"].map({"A": 1, "B": 2, "C": 3})          # map values
df["new"] = df["col"].apply(lambda x: x * 2 if x > 0 else 0)  # apply function

# ── GROUPBY & AGGREGATE ────────────────────────────────────────────────────────
df.groupby("group")["val"].sum()
df.groupby("group")["val"].transform("mean")   # keep original index (for new col)
df.groupby("group")["val"].cumsum()
df.groupby("group").apply(lambda g: g.nlargest(3, "val"))  # top 3 per group

# named aggregations
df.groupby("group").agg(
    mean_val=("val", "mean"),
    total=("val", "sum"),
    count=("val", "count"),
)

# ── MERGE / JOIN ───────────────────────────────────────────────────────────────
pd.merge(df1, df2, on="key")                        # inner join
pd.merge(df1, df2, on="key", how="left")            # left join
pd.merge(df1, df2, on="key", how="outer")           # full outer join
pd.merge(df1, df2, left_on="id", right_on="user_id")
pd.merge(df1, df2, on=["key1", "key2"])             # multiple keys

pd.concat([df1, df2])                               # stack rows
pd.concat([df1, df2], axis=1)                       # stack columns
pd.concat([df1, df2], ignore_index=True)

# ── PIVOT / RESHAPE ────────────────────────────────────────────────────────────
df.pivot_table(values="val", index="row", columns="col", aggfunc="mean")

df.melt(id_vars=["id"], value_vars=["col1", "col2"],
        var_name="variable", value_name="value")    # wide → long

df.pivot(index="id", columns="variable", values="value")  # long → wide

# ── DATETIME ───────────────────────────────────────────────────────────────────
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["dayofweek"] = df["date"].dt.dayofweek  # 0=Monday
df["quarter"] = df["date"].dt.quarter

df.set_index("date").resample("M").mean()  # monthly average
df.set_index("date").resample("W").sum()   # weekly sum

df["days_since"] = (pd.Timestamp.today() - df["date"]).dt.days

# ── INDEX ──────────────────────────────────────────────────────────────────────
df.set_index("id")
df.reset_index()
df.reset_index(drop=True)
